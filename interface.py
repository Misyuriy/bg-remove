import tkinter
from tkinter import ttk
from tkinter import filedialog

import numpy
import cv2

from bg_remover import BgRemover
from PIL import Image, ImageTk


class BgRemoverWindow:
    def __init__(self, geometry: str):
        self.root = tkinter.Tk()

        self.geometry = list(map(int, geometry.split("x")))
        self.root.geometry(geometry)

        self.result = None

        tkinter.Label(width=8).grid(row=0, column=0)

        load_button = ttk.Button(text="Load file", command=self._on_image_load_pressed, width=32)
        load_button.grid(row=0, column=1)

        tkinter.Label(width=24).grid(row=0, column=2)

        save_button = ttk.Button(text="Save file", command=self._on_image_save_pressed, width=32)
        save_button.grid(row=0, column=3)

        tkinter.Label(text="Initial image preview:").grid(row=1, column=1)
        tkinter.Label(text="Result image preview:").grid(row=1, column=3)

    def get_root(self) -> tkinter.Tk:
        return self.root

    def _on_image_load_pressed(self):
        file_path = filedialog.askopenfilename(title="Load image", filetypes=[("High resolution image files", "*.png"), ("JPEG image files", "*.jpg"), ("All files", "*.*")])
        if not file_path:
            return

        image = cv2.imread(file_path)

        remover = BgRemover()
        removed_image = remover.remove(image)

        self.display_initial_preview(image)
        self.display_result_preview(removed_image)

        self.result = removed_image

    def _on_image_save_pressed(self):
        if self.result is None:
            return

        file_path = filedialog.asksaveasfilename(title="Save image as...", defaultextension=".png", filetypes=[("High resolution image files", "*.png")])
        if file_path[-4:] != ".png":
            file_path += ".png"

        cv2.imwrite(filename=file_path, img=self.result)

    def display_initial_preview(self, image: numpy.ndarray):
        resized_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)).resize(size=(192, 192))
        photo_image = ImageTk.PhotoImage(image=resized_image)

        label = tkinter.Label(image=photo_image)
        label.image = photo_image
        label.grid(row=2, column=1)

    def display_result_preview(self, image: numpy.ndarray):
        resized_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)).resize(size=(192, 192))
        photo_image = ImageTk.PhotoImage(image=resized_image)

        label = tkinter.Label(image=photo_image)
        label.image = photo_image
        label.grid(row=2, column=3)
