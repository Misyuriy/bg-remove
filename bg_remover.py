import cv2
import numpy


class BgRemover:
    def __init__(self, calibration_threshold: int = 241, calibration_average: float = 183.2592):
        self.calibration_threshold = calibration_threshold
        self.calibration_average = calibration_average

    def remove(self, image: numpy.ndarray, manual_threshold: int = None):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if not manual_threshold:
            boundaries_threshold = 254
            _ret, boundaries_threshold_image = cv2.threshold(gray_image, boundaries_threshold, 255, cv2.THRESH_BINARY)

            min_y, max_y, min_x, max_x = self.detect_boundaries(cv2.bitwise_not(boundaries_threshold_image))
            threshold = self.calibration_threshold * (self.calibration_average / numpy.average(image[min_y: max_y, min_x: max_x]))

        else:
            threshold = manual_threshold

        if threshold >= 255:
            threshold = 254

        _ret, threshold_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

        threshold_image = cv2.bitwise_not(threshold_image)

        result_image = cv2.bitwise_and(image, image, mask=threshold_image)
        return result_image, threshold

    def detect_boundaries(self, image: numpy.ndarray):
        contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        max_x = 0
        max_y = 0
        min_x = image.shape[0]
        min_y = image.shape[1]

        for contour in contours:
            point = list(contour[0][0])

            if point[0] < min_x:
                min_x = point[0]
            if point[1] < min_y:
                min_y = point[1]

            if point[0] > max_x:
                max_x = point[0]
            if point[1] > max_y:
                max_y = point[1]

        print((min_x, min_y), (max_x, max_y))

        return min_y, max_y, min_x, max_x
