from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    return file_path

def save_file(content, file_ext=".jpg"):
    file_path = filedialog.asksaveasfilename(defaultextension=file_ext, filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
    if file_path:
        with open(file_path, 'wb') as file:
            file.write(content)
    return file_path

