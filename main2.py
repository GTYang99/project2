import tkinter as tk

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()


def main():
    windows = Windows()
    windows.title('RGB LED LIGHT')
    windows.mainloop()

if __name__ == "__main__":
    main()
