# ui_elements.py

import customtkinter as ctk

def add_camera_dialog(parent):
    # Create the dialog window
    add_camera_window = ctk.CTkToplevel(parent)
    add_camera_window.title("Add Camera")
    add_camera_window.geometry("350x400")  # Set default size
    
    # Center the dialog window relative to the parent
    center_window(add_camera_window, parent)
    
    # Create and position the input fields and radio buttons
    camera_name_entry = create_camera_name_entry(add_camera_window)
    camera_type = create_camera_type_radio_buttons(add_camera_window)

    return add_camera_window, camera_name_entry, camera_type

def center_window(window, parent):
    # Get the parent window position and size
    parent_x = parent.winfo_x()
    parent_y = parent.winfo_y()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    # Calculate the center position for the dialog window
    window.update_idletasks()  # Update window "requested" size information
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    x = parent_x + (parent_width // 2) - (window_width // 2)
    y = parent_y + (parent_height // 2) - (window_height // 2)

    # Set the position of the dialog window
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def create_camera_name_entry(parent):
    ctk.CTkLabel(parent, text="Camera Name:").pack(pady=(20, 10))
    camera_name_entry = ctk.CTkEntry(parent)
    camera_name_entry.pack(pady=(0, 20))
    return camera_name_entry

def create_camera_type_radio_buttons(parent):
    ctk.CTkLabel(parent, text="Select Camera Type:").pack(pady=(10, 10))
    camera_type = ctk.StringVar(value="v3")

    ctk.CTkRadioButton(parent, text="v2", variable=camera_type, value="v2").pack(pady=5)
    ctk.CTkRadioButton(parent, text="v2 noir", variable=camera_type, value="v2_noir").pack(pady=5)
    ctk.CTkRadioButton(parent, text="v3", variable=camera_type, value="v3").pack(pady=5)
    ctk.CTkRadioButton(parent, text="v3 noir", variable=camera_type, value="v3_noir").pack(pady=5)
    ctk.CTkRadioButton(parent, text="hq", variable=camera_type, value="hq").pack(pady=5)

    return camera_type
