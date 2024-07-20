from tkinter import *
from tkinter import filedialog, messagebox
import OperationsOnFile
import Images

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Application for performing operations on images")
        self.root.geometry("800x800")
        self.img_processor = None
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="This is a label")
        self.label.pack()

        self.open_button = Button(self.root, text="Open Image", command=self.on_open_button_click)
        self.open_button.pack()

        self.blur_button = Button(self.root, text="Blur Image", command=self.on_blur_button_click)
        self.blur_button.pack()

        self.rotate_button = Button(self.root, text="Rotate Image", command=self.on_rotate_button_click)
        self.rotate_button.pack()

        self.save_button = Button(self.root, text="Save Image", command=self.on_save_button_click)
        self.save_button.pack()

        self.degrees_entry = Entry(self.root)
        self.degrees_entry.pack()
        self.degrees_entry.insert(0, "Enter degrees to rotate")

        self.thumbnail_size_entry = Entry(self.root)
        self.thumbnail_size_entry.pack()
        self.thumbnail_size_entry.insert(0, "Enter the size as width,height")

        self.thumbnail_button = Button(self.root, text="Change size of the image", command=self.on_thumbnail_button_click)
        self.thumbnail_button.pack()

    def on_open_button_click(self):
        file_path = OperationsOnFile.open_file()
        if file_path:
            self.img_processor = Images.ImageProcessor(file_path)
            messagebox.showinfo("Image Opened", f"Image loaded from {file_path}")

    def on_blur_button_click(self):
        if self.img_processor:
            self.img_processor.blur_image()
            messagebox.showinfo("Image Blurred", "Image has been blurred")
        else:
            messagebox.showwarning("No Image", "Please open an image first")

    def on_rotate_button_click(self):
        if self.img_processor:
            try:
                degrees = int(self.degrees_entry.get())
                self.img_processor.rotate_image(degrees)
                messagebox.showinfo("Image Rotated", f"Image has been rotated by {degrees} degrees")
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter a valid number for degrees")
        else:
            messagebox.showwarning("No Image", "Please open an image first")

    def on_thumbnail_button_click(self):
        if self.img_processor:
            try:
                size_str = self.thumbnail_size_entry.get()
                width, height = map(int, size_str.split(','))
                self.img_processor.get_thumbnail((width, height))
                messagebox.showinfo("Image size changed", f"Image size has been changed to: {width}x{height}")
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter a valid size in the format width,height")
        else:
            messagebox.showwarning("No Image", "Please open an image first")

    def on_save_button_click(self):
        if self.img_processor:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
            if file_path:
                self.img_processor.save_image(file_path)
                messagebox.showinfo("Image Saved", f"Image saved to {file_path}")
        else:
            messagebox.showwarning("No Image", "Please open an image first")

def create_gui():
    root = Tk()
    app = Application(root)
    return root
