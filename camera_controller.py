# camera_controller.py

import json
import os
import requests

class CameraController:
    def __init__(self, storage_path="cameras.json"):
        self.storage_path = storage_path
        self.settings = {
            "server_url": "http://192.168.1.159:5000",
            "default_save_path": "/path/to/default/save/directory"
        }
        self.cameras = []
        self.connected = False
        self.load_data()
        self.window_geometry = self.settings.get("window_geometry", "600x400")  # Default size

    def save_window_geometry(self, geometry):
        self.settings["window_geometry"] = geometry
        self.save_data()

    def load_window_geometry(self):
        return self.settings.get("window_geometry", "600x400")
    
    def update_server_url(self, new_url):
        self.settings["server_url"] = new_url
        self.save_data()

    def check_connection(self):
        url = self.settings["server_url"]
        try:
            response = requests.get(url)
            self.connected = response.status_code == 200
        except:
            self.connected = False
        return self.connected

    def add_camera(self, camera_name, camera_type, path="/dev/video0", resolution="1920x1080", framerate=30):
        if camera_name and camera_type:
            camera = {
                "name": camera_name,
                "camera_type": camera_type,
                "path": path,
                "resolution": resolution,
                "framerate": framerate
            }
            self.cameras.append(camera)
            self.save_data()
            return True, f"Camera '{camera_name}' of type '{camera_type}' added."
        return False, "Invalid Camera Name or Type."

    def configure_camera(self):
        if not self.cameras:
            return False, "No cameras available to configure."
        
        camera_list = "\n".join([f"{camera['name']}: {camera['camera_type']} at {camera['path']}" for camera in self.cameras])
        return True, camera_list

    def take_photo(self, camera_name):
        camera = next((cam for cam in self.cameras if cam["name"] == camera_name), None)
        if camera:
            file_path = f"/simulated/path/{camera_name}_photo.jpg"
            return True, f"Simulated: Photo saved to {file_path}"
        return False, "Invalid Camera Name"

    def get_cameras(self):
        return self.cameras

    def save_data(self):
        data = {
            "settings": self.settings,
            "cameras": self.cameras
        }
        try:
            with open(self.storage_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Failed to save data: {e}")

    def load_data(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as file:
                    data = json.load(file)
                    self.settings = data.get("settings", self.settings)
                    self.cameras = data.get("cameras", [])
            except Exception as e:
                print(f"Failed to load data: {e}")
                self.settings = {
                    "server_url": "http://192.168.1.159:5000",
                    "default_save_path": "/path/to/default/save/directory"
                }
                self.cameras = []
        else:
            self.settings = {
                "server_url": "http://192.168.1.159:5000",
                "default_save_path": "/path/to/default/save/directory"
            }
            self.cameras = []
