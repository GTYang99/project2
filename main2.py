import tkinter as tk
from gpiozero import RGBLED
from gpiozero import Button

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

    light_state = False
    # @classmethod
    # def get_current_state(cls):
    #     return cls.light_state

    # @classmethod
    # def set_current_state(cls,state):
    #     cls.light_state = state

    def __init__(self):
        super().__init__()
        # ---- start title_frame -----
        # 建立一個tilte實體，再填內容
        title_frame = tk.Frame(self)
        title_frame.pack(pady=(30,0))
        tk.Label(title_frame,text="RGB燈光顏色控制器",font=('Arial',20)).pack()   
        # ----- end title_frame ------
        #---- start color_frame -----
        # 製作一個frame，按鈕放進去
        color_frame = tk.Frame(self,borderwidth=2,relief=tk.GROOVE)
        color_frame.pack(padx=50,pady=50) 
        # 製作frame的標題
        # tk.Label(color_frame,text="請選擇顏色:",font=("Arial",16)).grid(row=0,column=0,columnspan=3,sticky=tk.W,padx=10,pady=10)
        color_chose_label = tk.Label(color_frame,text="請選擇顏色:",font=("Arial",16))
        color_chose_label.grid(row=0,column=0,columnspan=3)
        red = ColorCanvas(color_frame,"red",width=100,height=100)
        red.bind('<ButtonRelease-1>',self.mouse_click)
        # gird放到第1行去
        red.grid(row=1, column=0)
        print(f'red狀態:{red.state}')

        green = ColorCanvas(color_frame,"green",width=100,height=100)       
        green.bind('<ButtonRelease-1>',self.mouse_click)        
        green.grid(row=1, column=1)        

        blue = ColorCanvas(color_frame,"blue",width=100,height=100)   
        blue.bind('<ButtonRelease-1>',self.mouse_click)
        blue.grid(row=1, column=2)

        Windows.set_select_convas(red)
        select_convas = Windows.get_select_convas()
        #---- end color_frame -----
        # print(select_convas.rec_color)
        #---- start light_state_frame -----
        light_state_frame = tk.Frame(self,borderwidth=2,relief=tk.GROOVE)
        self.state_label = tk.Label(light_state_frame,text='目前燈光:',font=('ariel,16'),anchor=tk.W)
        self.state_label.pack(fill=tk.X,padx=10,pady=10)
        light_state_frame.pack(fill=tk.X,padx=50,pady=(0,30))
        #---- end light_state_frame -----
        
        #gpiozero->一定要self
        self.button = Button(18)
        self.button.when_released = self.button_released

        #led
        self.led = RGBLED(red=17, green=27, blue=22)
        self.led.color=(0,0,0)

    def mouse_click(self,event):
        Windows.set_select_convas(event.widget)

    def button_released(self):
        # print("button release")
        # 修改釋放按鈕時候，會出現對應字樣
        Windows.light_state = not Windows.light_state
        if Windows.light_state == True:
            print("開燈")
            self.state_label.config(text="目前燈光:開")
            canvas = Windows.get_select_convas()
            if canvas.rec_color == "red":
                # 燈號顏色的方法是(R,G,B)
                self.led.color=(1,0,0)
            elif canvas.rec_color == "green":
                self.led.color=(0,1,0)
            elif canvas.rec_color == "blue":
                self.led.color=(0,0,1)
        else:
            print("關燈")
            self.state_label.config(text="目前燈光:關")
            self.led.color=(0,0,0)


def main():
    windows = Windows()
    windows.title('RGB LED LIGHT')
    windows.mainloop()

if __name__ == "__main__":
    main()
