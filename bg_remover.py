import cv2
import numpy


class BgRemover:
    def __init__(self):
        pass

    def remove(self, image: numpy.ndarray):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return gray
