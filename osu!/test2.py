from tkinter import *
from PIL import Image, ImageTk
import win32gui
import win32con

def setClickthrough(hwnd):
    print("setting window properties")
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)

TRANSPARENT_COLOR = "#add123"

root = Tk()
root.bind("q", lambda e: (root.destroy(), print("Window qscreenheight()}")))
root.overrideredirect(1)
root.config(bg=TRANSPARENT_COLOR)
root.wm_attributes('-transparentcolor', TRANSPARENT_COLOR)
root.attributes('-topmost', True)

canvas = Canvas(root, highlightthickness=0,width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill=BOTH, expand=True)
canvas.create_text(960, 620, text="Overlay Online", font=("Segoe UI", 20), fill="black")

root.update()
setClickthrough(canvas.winfo_id())  # Pass the root HWND, not a widget
root.mainloop()
