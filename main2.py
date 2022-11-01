import tkinter as tk

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        red = tk.Canvas(self,width=70,height=70,relief='ridge')
        red.create_rectangle(10,10,60,60,fill="red")
        # 原點所在的座標位置
        x  = 70*1/5
        y  = 70*4/6
        width = 10
        red.create_oval(x,y,x+10,y+10,fill="white",outline='white')
        red.bind('<ButtonRelease-1>',self.mouse_click)
        red.grid(row=0, column=0)

        green = tk.Canvas(self,width=70,height=70)
        green.create_rectangle(10,10,60,60,fill="green")
        green.grid(row=0, column=1)

        blue = tk.Canvas(self,width=70,height=70)
        blue.create_rectangle(10,10,60,60,fill="blue")
        blue.grid(row=0, column=2)

    def mouse_click(self,event):
        print(event.__dict__)
        # 圖斑做出邊框
        # event.widget.config(borderwidth=5)
        # event.widget.delete()
        event.widget.create_rectangle(10,10,60,60,fill='white')
        event.widget.create_rectangle(20,20,50,50,fill='red')
        # event.widget.update()


def main():
    windows = Windows()
    windows.title('RGB LED LIGHT')
    windows.mainloop()

if __name__ == "__main__":
    main()
