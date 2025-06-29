from tkinter import *
from PIL import Image, ImageTk
import win32gui
import win32con

def setClickthrough(hwnd):
    print("setting window properties")
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)

width = 1920 #self.winfo_screenwidth()
height = 1080 #self.winfo_screenheight()

root = Tk()
root.geometry("1920x1080")
root.config(bg='#add123')
root.wm_attributes('-transparentcolor', '#add123')
root.attributes("-fullscreen", True)
root.wm_attributes("-topmost", 1)
bg = Canvas(root, width=width, height=height)
label = Label(root, text="👁️‍🗨️ CLICK-THROUGH TESTING ZONE", 
                font=("Segoe UI", 30), fg="red", bg="white")
label.place(x=300, y=500)
setClickthrough(bg.winfo_id())

root.mainloop()