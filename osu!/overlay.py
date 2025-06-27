from tkinter import *
class OsuOverlay():
    def __init__(self):
        pass
    def initialize_script(self) -> None:
        self.master = Tk()
        self.master.overrideredirect(True)
        self.master.attributes("-topmost", True)
        self.master.configure(bg="black")
        self.master.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}")
        # self.canvas = Canvas(self.master,bg="black",highlightthickness=0)
        # self.canvas.pack(fill=BOTH, expand=True) #Fill in both
        
        self.canvas = Canvas(self.master,bg="black",highlightthickness=0)
        self.canvas.pack(fill=BOTH,expand=True)
        self.master.update() #Update it NOW, you dont need to wait for mainloop
        self.master.bind("<F>", lambda e: (self.master.destroy(),print("Window Destroyed")))
        self.master.mainloop()