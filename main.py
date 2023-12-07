import cv2
from bg_remover import BgRemover


def main():
    print()

    image = cv2.imread("input.png")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


if __name__ == "__main__":
    main()
