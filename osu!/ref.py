from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import filedialog
def main():
    window_width = 1400
    window_height = 650
    master = Tk()
    master.minsize(width=window_width, height=window_height)
    master.config(bg="#303030")
    master.title("Image Watermarker")
    class AddLogoWindow(Toplevel):
        def __init__(self,canvas_height,canvas_width,image_canvas ,master = None,**kwargs):
            super().__init__(master)
            self.minsize(400,475)
            self.config(bg="#303030")
            self.title("Add Logo")
            
            self.logo_size = None
            self.logo_transparency = None
            
            self.size_block = Frame(self,style="ControlBlock.TFrame")
            self.size_slider = Scale(self.size_block,from_=1,to=100,value=50,command=self.adjust_size)
            self.size_label = Label(self.size_block,text="Size",style="ControlLabel.TLabel")
            self.size_info = Label(self.size_block,text=f"{self.size_slider.get()}%",style="ValueLabel.TLabel")
            self.size_label.pack(side=LEFT,padx=10)
            self.size_slider.pack(side=LEFT,padx=10)
            self.size_info.pack(side=LEFT,padx=10)
            self.size_block.grid(row=0,column=0,padx=15,pady=12)
            
            self.transparency_block = Frame(self, style="ControlBlock.TFrame")
            self.transparency_slider = Scale(self.transparency_block, from_=0, to=100, value=0, command=self.adjust_transparency)
            self.transparency_label = Label(self.transparency_block, text="Transparency", style="ControlLabel.TLabel")
            self.transparency_info = Label(self.transparency_block, text=f"{self.transparency_slider.get()}%", style="ValueLabel.TLabel")
            self.transparency_label.pack(side=LEFT, padx=10)
            self.transparency_slider.pack(side=LEFT, padx=10)
            self.transparency_info.pack(side=LEFT, padx=10)
            self.transparency_block.grid(row=1, column=0, padx=15, pady=12)
            
            
            self.rotation_block = Frame(self, style="ControlBlock.TFrame")
            self.rotation_slider = Scale(self.rotation_block, from_=-180, to=180, value=0, orient=HORIZONTAL, command=self.adjust_rotation)
            self.rotation_label = Label(self.rotation_block, text="Rotation", style="ControlLabel.TLabel")
            self.rotation_info = Label(self.rotation_block, text=f"{self.rotation_slider.get()}°", style="ValueLabel.TLabel")
            self.rotation_label.pack(side=LEFT, padx=10)
            self.rotation_slider.pack(side=LEFT, padx=10)
            self.rotation_info.pack(side=LEFT, padx=10)
            self.rotation_block.grid(row=2, column=0, padx=15, pady=12)

            
            self.filename = filedialog.askopenfilename(initialdir="r", title="Open an Image",
                                              filetypes=(("Image Files", "*.jpg *.jpeg *.png *.webp"), ("All Files", "*.*")))
            self.original_logo_image = None #untouched og image
            self.image = None #Modifiable Image
            
            self.canvas_width = canvas_width
            self.canvas_height = canvas_height
            self.image_canvas = image_canvas
            self.image_width,self.image_height = None,None
            #Sets logo to be half the widht and height of the canvas
             #Checks if there is already a logo
            if self.filename:
                self.original_logo_image = Image.open(self.filename).convert("RGBA")
                self.image = self.original_logo_image.copy()
                self.image_width,self.image_height = self.original_logo_image.size
                
                scale_factor = min(self.canvas_width / 2 / self.image_height,self.canvas_height / 2 / self.image_width) #Sets the slider value so the image is half the canvas
                target_size = (int(self.image_width * scale_factor),int(self.image_height * scale_factor))
                self.original_logo_image.thumbnail(target_size)
                user_img = ImageTk.PhotoImage(self.original_logo_image)
                self.image_canvas.logo = user_img
                center_x = self.image_canvas.winfo_width() // 2
                center_y = self.image_canvas.winfo_height() // 2
                self.logo_image = self.image_canvas.create_image(center_x,center_y,image=user_img,anchor=CENTER)
                self.size_slider.set(int(scale_factor * 100)) #The slider scales from 0-100
                self.size_info.config(text=f"{self.size_slider.get():.0f}%")
                
            
                
        # def make_draggable(widget):
        #     widget.bind("<Button-1>", on_drag_start)
        #     widget.bind("<B1-Motion>", on_drag_motion)

        # def on_drag_start(event):#Tracks the current position of the cursor relative to the center of the image(?)
        #     widget = event.widget
        #     widget._drag_start_x = event.x
        #     widget._drag_start_y = event.y

        # def on_drag_motion(event):
        #     widget = event.widget
        #     x = widget.winfo_x() - widget._drag_start_x + event.x #winfo for current coord, subtract this with the cursor offset
        #     #in order to center the image, event.x and event.y is just how much it moved (?)
        #     y = widget.winfo_y() - widget._drag_start_y + event.y
        #     widget.place(x=x, y=y)
        
        def display_image(self,*args):
            self.image_tkinter = ImageTk.PhotoImage(self.image)
            self.image_canvas.itemconfig(self.logo_image,image=self.image_tkinter)
            
        def adjust_size(self,*args):
            logo_img = self.original_logo_image.copy()
            scale_factor = self.size_slider.get() / 100
            self.size_info.config(text=f"{self.size_slider.get():.0f}%") 
            self.logo_size = (int(self.image_width * scale_factor),int(self.image_height * scale_factor))
            logo_img = logo_img.resize(self.logo_size, Image.LANCZOS)
            self.image = logo_img
            self.display_image()
        
        def adjust_transparency(self,*args):
            logo_img = self.image.copy() #Ofc you need to do this so multiple effects can be added(trans,size,spacing,...)
            scale_factor = 255 - int(255 * self.transparency_slider.get() /100) #Percentage, also putalpha() only accepts ints
            self.transparency_info.config(text=f"{self.transparency_slider.get():.0f}%")
            logo_img.putalpha(scale_factor)
            self.image = logo_img
            self.display_image()
         
        def adjust_rotation(self,*args):
            logo_img = self.image.copy()
            angle = self.rotation_slider.get()
            self.rotation_info.config(text=f"{angle:.0f}°")
            img = logo_img.rotate(angle,expand=True,fillcolor=(0,0,0,0))
            self.image = img
            self.display_image()
    class AddTextWindow(Toplevel):
        def __init__(self, master = None,**kwargs):
            super().__init__(master)
            self.minsize(400,475)
            self.config(bg="#303030")
            self.title("Add Text")
            
    def open_file():
        #Opens File Explorer
        filename = filedialog.askopenfilename(initialdir="r", title="Open an Image",
                                              filetypes=(("Image Files", "*.jpg *.jpeg *.png *.webp"), ("All Files", "*.*")))
        if filename:
            user_img_PIL = Image.open(filename)
            canvas_width = window_width
            canvas_height = window_height - 125
            user_img_PIL.thumbnail((canvas_width, canvas_height))
            user_img = ImageTk.PhotoImage(user_img_PIL) #ImageTk is a module lol, the file kw expects a file path??
            image_canvas.configure(width=canvas_width, height=canvas_height)
            image_canvas.itemconfig(canvas_image, image=user_img)
            image_canvas.coords(canvas_image, canvas_width // 2, canvas_height // 2)
            #Keeps reference to the image otherwise it gets garbage collected
            image_canvas.im = user_img #https://stackoverflow.com/questions/57049722/unable-to-update-image-in-tkinter-using-a-function
            upload_file_button.destroy()
            top_toolbar.grid(row=0, column=0, sticky="ew")
            return user_img
        else:
            print("No file selected.")
    
    def add_logo():
        logo_window = AddLogoWindow(master=master,canvas_height=canvas_height,canvas_width=canvas_width,image_canvas=image_canvas)
    def add_text():
        text_window = AddTextWindow(master=master)
    def revert():
        pass

    style = Style()
    style.theme_use("clam")
    style.configure("UploadFile.TButton", foreground="white", background="#196bf7",
                    relief="flat", borderwidth=0, padding=3,font=("Helvetica",9))
    style.configure("Add.TButton", foreground="white", background="#303030",
                     relief = "flat", padding=3,font=("Helvetica",10),
                      darkcolor="white",
                      lightcolor="gray",
                     bordercolor="white",
                    )
    style.configure("TFrame",  background="#303030",
                    relief="flat", borderwidth=0, padding=3)
    style.configure("Toolbar.TFrame",background = "#404040",height=300)#Toolbar at top
    style.configure("ControlBlock.TFrame",background="#202020")
    style.configure("ControlLabel.TLabel",background = "#202020",font=("Segoe UI",13,),foreground="#f0f0f0")
    style.configure("ValueLabel.TLabel", font=("Segoe UI", 11),background = "#202020",foreground="#f0f0f0")
    style.map("UploadFile.TButton",
              foreground=[("pressed", "white"), ("active", "white")],
              background=[("pressed", "#003acc"), ("active", "#338aff")])
    style.map("Add.TButton",
              foreground=[("pressed", "white"), ("active", "white")],
              background=[("pressed", "#202020"), ("active", "#404040")])

    cloud_upload_img = Image.open(r"C:\Users\PC\Desktop\Programming\python_projects\100daysofpython\image_watermarker\images\cloud_upload_image.png")
    cloud_upload_width, cloud_upload_height = cloud_upload_img.size
    cloud_upload_img.thumbnail((cloud_upload_width - 200, cloud_upload_height - 100))
    cloud_upload_png = ImageTk.PhotoImage(cloud_upload_img)

    canvas_width = window_width - 500
    canvas_height = window_height - 425
    image_canvas = Canvas(master, width=canvas_width, height=canvas_height, highlightthickness=0,
                          bg=master["bg"])
    canvas_image = image_canvas.create_image(
        canvas_width // 2,
        canvas_height // 2,
        image=cloud_upload_png,
        anchor="center"
    )
    
    image_canvas.grid(row=1, column=0)

    upload_file_button = Button(master, text="Upload File", padding=(20, 8),
                                style="Upload_File.TButton", command=open_file)
    upload_file_button.grid(row=2, column=0, pady=10)

    top_toolbar = Frame(master, style="Toolbar.TFrame",height=300,width=window_width)
    # Don't grid it until after upload
    button_container = Frame(top_toolbar, style="Toolbar.TFrame")
    button_container.pack(anchor="center", pady=10)

    add_text_button = Button(button_container, text="Add Text", padding=(20, 8),
                            style="UploadFile.TButton", command=add_text)
    add_logo_button = Button(button_container, text="Add Logo", padding=(20, 8),
                         style="UploadFile.TButton", command=add_logo)
    add_text_button.pack(side=LEFT, padx=10)
    add_logo_button.pack(side=LEFT, padx=10) #Packs them side-by-side in the frame
    
    master.grid_rowconfigure(0, weight=1)
    master.grid_rowconfigure(1, weight=1)
    master.grid_columnconfigure(0, weight=1)
    master.grid_rowconfigure(2, weight=1)
    master.mainloop()

if __name__ == "__main__":
    main()
