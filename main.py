import cv2
from bg_remover import BgRemover


def main():
    image = cv2.imread("input.png")

    remover = BgRemover()
    removed_image = remover.remove(image)

    cv2.imshow("Edited image", removed_image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
