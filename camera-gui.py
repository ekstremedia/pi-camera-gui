import customtkinter as ctk
from camera_controller import CameraController
from ui_elements import add_camera_dialog
from utils import show_messagebox, save_file_dialog

class CameraApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Raspberry Pi Camera Controller")
        self.geometry("600x400")
        self.grid_columnconfigure(1, weight=1)

        self.camera_controller = CameraController()
        self.server_url = ctk.StringVar(value=self.camera_controller.settings["server_url"])
        self.connection_status = ctk.StringVar(value="Disconnected")  # Default status

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Server URL Entry
        ctk.CTkLabel(self, text="Server URL:").grid(row=0, column=0, padx=20, pady=10, sticky="w")
        server_url_entry = ctk.CTkEntry(self, textvariable=self.server_url)
        server_url_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        server_url_entry.bind("<FocusOut>", self.update_server_url)  # Update on focus out

        # Connect Button and Status
        connect_frame = ctk.CTkFrame(self)
        connect_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        
        self.status_label = ctk.CTkLabel(connect_frame, textvariable=self.connection_status)
        self.status_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        connect_button = ctk.CTkButton(connect_frame, text="Connect", command=self.connect_to_server)
        connect_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Frame for Camera Operations
        camera_frame = ctk.CTkFrame(self)
        camera_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        ctk.CTkButton(camera_frame, text="Add Camera", command=self.add_camera).grid(row=0, column=0, pady=10, padx=10)
        ctk.CTkButton(camera_frame, text="Configure Camera", command=self.configure_camera).grid(row=0, column=1, pady=10, padx=10)
        ctk.CTkButton(camera_frame, text="Take Photo", command=self.take_photo).grid(row=0, column=2, pady=10, padx=10)

        # Frame for Photo Operations
        photo_frame = ctk.CTkFrame(self)
        photo_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        ctk.CTkButton(photo_frame, text="View Photos", command=self.view_photos).grid(row=0, column=0, pady=10, padx=10)

    def update_server_url(self, event):
        new_url = self.server_url.get()
        self.camera_controller.update_server_url(new_url)

    def connect_to_server(self):
        if self.camera_controller.check_connection():
            self.connection_status.set("Connected")
            self.status_label.configure(fg_color="green")
        else:
            self.connection_status.set("Disconnected")
            self.status_label.configure(fg_color="red")

    def add_camera(self):
        add_camera_window, camera_name_entry, camera_type = add_camera_dialog(self)

        def on_add():
            camera_name = camera_name_entry.get()
            camera_type_selected = camera_type.get()

            # Add camera with default path, resolution, and framerate
            success, message = self.camera_controller.add_camera(camera_name, camera_type_selected)
            show_messagebox("Add Camera", message, "info" if success else "error")
            if success:
                add_camera_window.destroy()

        ctk.CTkButton(add_camera_window, text="Add Camera", command=on_add).pack(pady=20)

    def configure_camera(self):
        success, message = self.camera_controller.configure_camera()
        show_messagebox("Configure Camera", message, "info" if success else "error")

    def take_photo(self):
        cameras = self.camera_controller.get_cameras()
        if not cameras:
            show_messagebox("Error", "No cameras available to take a photo.", "error")
            return

        camera_name_dialog = ctk.CTkInputDialog(text=f"Enter Camera Name ({', '.join([cam['name'] for cam in cameras])})", title="Take Photo")
        camera_name = camera_name_dialog.get_input()

        success, message = self.camera_controller.take_photo(camera_name)
        show_messagebox("Take Photo", message, "info" if success else "error")

    def view_photos(self):
        photos = [
            {"file_name": "photo1.jpg", "path": "/simulated/path/photo1.jpg"},
            {"file_name": "photo2.jpg", "path": "/simulated/path/photo2.jpg"}
        ]
        
        for photo in photos:
            if messagebox.askyesno("Download Photo", f"Do you want to simulate downloading {photo['file_name']}?"):
                save_path = save_file_dialog([("JPEG files", "*.jpg")])
                if save_path:
                    show_messagebox("Download Complete", f"Simulated: Photo saved to {save_path}")

if __name__ == "__main__":
    app = CameraApp()
    app.mainloop()
