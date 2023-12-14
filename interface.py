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
        file_path = filedialog.askopenfilename(filetypes=[("High resolution image files", "*.png"), ("JPEG image files", "*.jpg"), ("All files", "*.*")])
        if not file_path:
            return

        image = cv2.imread(file_path)

        remover = BgRemover()
        removed_image = remover.remove(image)

        photo_image = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(removed_image, cv2.COLOR_BGR2RGB)))

        label = tkinter.Label(image=photo_image)
        label.image = photo_image
        label.pack(side=tkinter.TOP)

        self.result = removed_image

    def _on_image_save_pressed(self):
        if not self.result:
            return
