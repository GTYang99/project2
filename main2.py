from sre_parse import State
import tkinter as tk

#建立一個ColorCanvas的物件，父母繼承tk.Canvas
class ColorCanvas(tk.Canvas):
    # 建立Class的property
    # 建立一個Class內建的常數
    ON = True
    OFF = False
    def __init__(self,parent,rec_color,**kwargs):
        # 關鍵字引數解壓縮給物件內的width與height
        self.width = kwargs['width']
        self.height = kwargs['height']
        super().__init__(parent,**kwargs)
        self.rec_color = rec_color
        # 給出初始的屬性
        self.__state = ColorCanvas.OFF
        # space = 10
        self.space = self.width / 7
        # rec_width = self.width - 2 * self.space
        # rec_heigh = self.width - 2 * self.space
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
            rec_width = self.width - 2 * self.space
            rec_height = self.height - 2 * self.space
            cir_width = rec_width / 5
            cir_height = rec_height / 5
            cir_start_x = self.space + cir_width / 2
            cir_end_x = cir_start_x + cir_width
            cir_start_y = self.space + rec_height * 5 / 7
            cir_end_y  =  cir_start_y + cir_height
            self.create_oval(cir_start_x,cir_start_y,cir_end_x,cir_end_y,fill='white',outline='white')

class Windows(tk.Tk):
    selected_convas = None
    @classmethod
    def get_select_convas(cls):
        return cls.selected_convas

    @classmethod
    def set_select_convas(cls,convas):
        if cls.selected_convas is not None:
            cls.selected_convas.state = ColorCanvas.OFF  
        cls.selected_convas = convas
        cls.selected_convas.state = ColorCanvas.ON

    def __init__(self):
        super().__init__()
        # 製作一個frame，按鈕放進去
        color_frame = tk.Frame(self,borderwidth=2,relief=tk.GROOVE)
        color_frame.pack(padx=50,pady=50) 
        red = ColorCanvas(color_frame,"red",width=100,height=100)
        red.bind('<ButtonRelease-1>',self.mouse_click)
        red.grid(row=0, column=0)
        print(f'red狀態:{red.state}')

        green = ColorCanvas(color_frame,"green",width=100,height=100)       
        green.bind('<ButtonRelease-1>',self.mouse_click)        
        green.grid(row=0, column=1)        

        blue = ColorCanvas(color_frame,"blue",width=100,height=100)   
        blue.bind('<ButtonRelease-1>',self.mouse_click)
        blue.grid(row=0, column=2)

        Windows.set_select_convas(red)
        select_convas = Windows.get_select_convas()
        print(select_convas.rec_color)


    def mouse_click(self,event):
        Windows.set_select_convas(event.widget)



def main():
    windows = Windows()
    windows.title('RGB LED LIGHT')
    windows.mainloop()

if __name__ == "__main__":
    main()
