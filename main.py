from interface import BgRemoverWindow


def main():
    window = BgRemoverWindow("720x480")
    window.get_root().mainloop()


if __name__ == "__main__":
    main()
