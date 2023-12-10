import cv2
import numpy


class BgRemover:
    def __init__(self, deviation_threshold: int = 0):
        pass

    def remove(self, image: numpy.ndarray):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        _ret, threshold_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)

        threshold_image = cv2.bitwise_not(threshold_image)

        result_image = cv2.bitwise_and(image, image, mask=threshold_image)
        return result_image
