import curses


def split_words(text: str) -> list[str]:
    return text.split()


def main() -> None:
    with open("book.txt") as f:
        text = f.read()

    words = split_words(text)

    curses.wrapper(curses_main, words)


def curses_main(w, words):
    i = 0
    while True:
        w.addstr(curses.LINES // 2, curses.COLS // 2 - len(words[i]), words[i])

        key = w.getch()

        if key == curses.KEY_LEFT and i != 0:
            i -= 1
        if key == curses.KEY_RIGHT and i != len(words) - 1:
            i += 1
        if key == ord("q"):
            exit()

        w.clear()

    w.addstr("\nPress q to exit...")

    w.refresh()
    w.getch()


if __name__ == "__main__":
    main()
