import customtkinter as ctk

def create_camera_widget(parent, camera, edit_callback):
    # Create a frame for the camera widget
    frame = ctk.CTkFrame(parent)
    
    # Add camera icon (for simplicity, using text as a placeholder for an icon)
    icon_label = ctk.CTkLabel(frame, text="📷", font=("Arial", 24))
    icon_label.grid(row=0, column=0, padx=10, pady=10)

    # Add camera name
    name_label = ctk.CTkLabel(frame, text=camera["name"], font=("Arial", 14))
    name_label.grid(row=0, column=1, padx=10, pady=10)

    # Add a click event to open the edit dialog
    frame.bind("<Button-1>", lambda event: edit_callback(camera))

    return frame

def display_camera_widgets(parent, cameras, edit_callback):
    # Clear existing widgets
    for widget in parent.winfo_children():
        widget.destroy()

    # Create a widget for each camera
    for camera in cameras:
        widget = create_camera_widget(parent, camera, edit_callback)
        widget.pack(padx=10, pady=10, fill="x")
