import tkinter
from tkinter import ttk
from tkinter import filedialog

import cv2
from bg_remover import BgRemover
from PIL import Image, ImageTk


class BgRemoverWindow:
    def __init__(self, geometry: str):
        self.root = tkinter.Tk()

        self.geometry = list(map(int, geometry.split("x")))
        print(self.geometry)
        self.root.geometry(geometry)

        button = ttk.Button(text="Load file", command=self._on_image_load_pressed)
        button.pack()

    def get_root(self) -> tkinter.Tk:
        return self.root

    def _on_image_load_pressed(self):
        file_path = filedialog.askopenfilename(filetypes=[("High resolution image files", "*.png"), ("JPEG image files", "*.jpg"), ("All files", "*.*")])

        image = cv2.imread(file_path)
        print(file_path)
        remover = BgRemover()
        removed_image = remover.remove(image)

        photo_image = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(removed_image, cv2.COLOR_BGR2RGB)))

        label = tkinter.Label(image=photo_image)
        label.image = photo_image
        label.pack(side=tkinter.TOP)
