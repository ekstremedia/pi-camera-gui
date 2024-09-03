# utils.py

from tkinter import filedialog, messagebox

def show_messagebox(title, message, message_type="info"):
    if message_type == "info":
        messagebox.showinfo(title, message)
    elif message_type == "error":
        messagebox.showerror(title, message)
    elif message_type == "warning":
        messagebox.showwarning(title, message)

def save_file_dialog(filetypes):
    return filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=filetypes)
