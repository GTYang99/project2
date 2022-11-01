from sre_parse import State
import tkinter as tk

#建立一個ColorCanvas的物件，父母繼承tk.Canvas
class ColorCanvas(tk.Canvas):
    def __init__(self,parent,rec_color,**kwargs):
        # 關鍵字引數解壓縮給物件內的width與height
        self.width = kwargs['width']
        self.height = kwargs['height']
        super().__init__(parent,**kwargs)
        self.rec_color = rec_color
        # 給出初始的屬性
        self.__state = False
        # space = 10
        self.space = self.width / 7
        rec_width = self.width - 2 * self.space
        rec_heigh = self.width - 2 * self.space
        # self.create_rectangle(space, space, width - space, height - space,fill=self.rec_color)
        # self.create_rectangle(space,space,self.width - space,self.width - space,fill=self.rec_color)
        # print(rec_color)
        self.create_rectangle(self.space, self.space, self.width - self.space, self.height - self.space,fill=self.rec_color)

    # 建立物件屬性回傳
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self,s):
        self.__state = s
        self.delete()
        self.create_rectangle(self.space, self.space, self.width - self.space, self.height - self.space,fill=self.rec_color)        
        if self.__state == True:
            #多加小圓點
            print("多加小圓點")

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        # red = ColorCanvas(self,width=70,height=70,relief='ridge')
        # red.create_rectangle(10,10,60,60,fill="red")
        # 原點所在的座標位置
        # x  = 70*1/5
        # y  = 70*4/6
        # width = 10
        # red.create_oval(x,y,x+10,y+10,fill="white",outline='white')
        # red = ColorCanvas(self,"red",width=70,height=70)
        red = ColorCanvas(self,"red",width=100,height=100)
        red.bind('<ButtonRelease-1>',self.mouse_click)
        red.grid(row=0, column=0)
        red.state = True
        print(f'red狀態:{red.state}')

        # green = tk.Canvas(self,width=70,height=70)
        # green.create_rectangle(10,10,60,60,fill="green")
        green = ColorCanvas(self,"green",width=100,height=100)       
        green.grid(row=0, column=1)

        # blue = tk.Canvas(self,width=70,height=70)
        # blue.create_rectangle(10,10,60,60,fill="blue")
        blue = ColorCanvas(self,"blue",width=100,height=100)   
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
