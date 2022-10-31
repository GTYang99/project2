from gpiozero import Button

button = Button(18)   #第18針腳建立一個按鈕

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")