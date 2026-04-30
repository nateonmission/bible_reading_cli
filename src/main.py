import os

from rich import print as printr

from textual.app import App, ComposeResult

def clear():
    # 'nt' is for Windows, 'posix' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')


class BibleReading(App):



def main():
    clear()
    printr(r"[blue]Hello[/blue] from bible-reading-cli!")


if __name__ == "__main__":
    main()
