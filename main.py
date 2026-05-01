import curses


def split_words(text: str) -> list[str]:
    return text.split()


def main() -> None:
    with open("book.txt") as f:
        text = f.read()

    words = split_words(text)

    curses.wrapper(curses_main, words)


def save_book_location(i: int) -> None:
    with open("save.txt", "w") as f:
        f.write(str(i))


def curses_main(w, words):
    curses.curs_set(0)

    try:
        with open("save.txt", "r") as f:
            i = int(f.read())
    except FileNotFoundError:
        i = 0

    while True:
        x = curses.COLS // 2 - len(words[i]) // 2
        y = curses.LINES // 2

        w.addstr(y, x, words[i])

        key = w.getch()

        if (key == curses.KEY_LEFT or key == ord("h")) and i != 0:
            i -= 1
        if (key == curses.KEY_RIGHT or key == ord("l")) and i != len(words) - 1:
            i += 1
        if key == ord("q"):
            exit()
        save_book_location(i)
        w.clear()

    w.addstr("\nPress q to exit...")

    w.refresh()
    w.getch()


if __name__ == "__main__":
    main()
