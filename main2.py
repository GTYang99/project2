import tkinter as tk

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        red = tk.Canvas(self,width=70,height=70)
        red.create_rectangle(10,10,60,60,fill="red")
        red.bind('<ButtonRelease-1>',self.mouse_click)
        red.grid(row=0, column=0)

        green = tk.Canvas(self,width=70,height=70)
        green.create_rectangle(10,10,60,60,fill="green")
        green.grid(row=0, column=1)

        blue = tk.Canvas(self,width=70,height=70)
        blue.create_rectangle(10,10,60,60,fill="blue")
        blue.grid(row=0, column=2)

    def mouse_click(self,event):
        print(event)


def main():
    windows = Windows()
    windows.title('RGB LED LIGHT')
    windows.mainloop()

if __name__ == "__main__":
    main()
