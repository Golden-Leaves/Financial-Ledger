from tkinter import *
import win32gui
import win32con
from pynput.mouse import Listener as MouseListener
class OsuOverlay():
    def __init__(self,map_file):
        #TODO: Check events to see if theres a break at the start
        try:
            self.map_file = map_file
            self.scheduled_tasks  = []
            self.sections = self.map_file.split("\n\n")
            self.mods = {"DT":False,"HR":True,"HD":False,"FL":True} #Sample data for now
            
            self.start_time = 0
            self.PLAYER_KEYBINDS = ["D","F"] #What keybind the player uses
            self.hit_objects = {}
            self.get_map_data(self.sections)
        except Exception as e:
            print(f"Exception: {e}")
    def initialize_script(self):
        self.root = Tk()
        self.root.geometry("1920x1080")
        self.root.overrideredirect(True)
        self.root.overrideredirect(1)
        self.root.attributes("-alpha", 0.3)
        self.root.attributes('-transparentcolor', 'black', '-topmost', 1)
        self.bg = Canvas(self.root, bg='black', highlightthickness=0)
        # self.bg.create_oval(
        #     70, 70, 130, 130,  # (x0, y0, x1, y1)
        #     fill='red',
        #     outline=''
        # )
        self.bg.pack(fill=BOTH, expand=True)
        self.root.config(bg='black')
        self.setClickthrough(self.root.winfo_id())
        self.mouse_listener = MouseListener(on_click=self.remove_circle)
        self.mouse_listener.start()
        self.circles_info = self.load_circles_info(self.timing_info)
        self.start_sequence()
        
        self.root.mainloop()
        
        
    def setClickthrough(self,hwnd):
        print("setting window properties")
        try:
            styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
            styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
            win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
            win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
        except Exception as e:
            print(e)


    def get_map_data(self,sections) -> None:
            try:
                #Some default values so the program doesnt fumble when doing old maps
                
                for section in sections:
                    if "[Difficulty]" in section:
                        self.difficulty_data = section
                        for line in self.difficulty_data.split("\n"):
                            
                            if "CircleSize" in line:
                                self.CS = float(line.split(":")[1])
                                self.radius = int(109 - 9 * self.CS) #https://osu.ppy.sh/wiki/en/Beatmap/Circle_size
                                
                            if "ApproachRate" in line:
                                AR = float(line.split(":")[1])
                                #AR time calculations: https://osu.ppy.sh/wiki/en/Beatmap/Approach_rate
                                if AR < 5: #TODO: Implement fade in animation later(I love HD)
                                    self.preempt = int(1200 + 600 * (5 - AR) / 5)
                                elif AR == 5:
                                    self.preempt = 1200
                                elif AR > 5:
                                    self.preempt = int(1200 - 750 * (AR - 5) / 5)
                                else:#AR11 lol
                                    self.preempt = 300
                            
                            if "AudioLeadIn" in line:
                                self.start_time += int(line.split(":")[1])
                                
                            
                        
                    elif "[HitObjects]" in section:
                        self.timing_info = section.split("\n")[1::] #Skips the header
                        break
                    
                        
                
                    
                   
                                
            except Exception as e:
                print(f"Exception: {e}")
    def scale_to_resolution(self,x,y): #Osu coords are weird: https://osu.ppy.sh/wiki/en/Client/Playfield
            # scale_x = self.root.winfo_width() /512
            # scale_y = self.root.winfo_height() /384 + 8
             #CS in osu!pixels https://osu.ppy.sh/community/forums/topics/311844?n=4
            scale_factor = 1080 / 480
            return int(x * scale_factor + 384), int(y*scale_factor + 126)
        
    def get_timing_info(self,parts) -> tuple: #https://osu.ppy.sh/wiki/en/Client/File_formats/osu_%28file_format%29
        def get_slider_info(slider_data) -> tuple:
            points = slider_data.rsplit(",",1)[0].split(",",1)[0].split("|")

            slider_points = [tuple(map(int,point.split(":"))) for point in points[1::]]
            return slider_points
        
        try:
            
                print(f"LINE: {parts}")
               
               
                
                x = int(parts[0])
                y = int(parts[1])
                x,y = self.scale_to_resolution(x,y)
                hit_time = int(parts[2])
                object_type = int(parts[3])
                
                if not self.found_first_hit_object:
                    if object_type != 3:                 # 3 = spinner
                        self.start_time = hit_time - self.preempt
                        self.found_first_hit_object = True
                    else:
                        pass
               
                
                    
                self.previous_object_hit_time = hit_time
                
                if parts[-1][0].isalpha(): #Slider or nah
                    slider_info = get_slider_info(parts[-1]) #Hitsounds need to get out 🗣️🔥🔥
                    object_type = "slider"
                else:
                    
                    slider_info = None
                    object_type = "circle"
              
                print(x,y,object_type,slider_info)
                return (x,y,hit_time,object_type,slider_info)
        
        except Exception as e:
            print(f"Exception: {e}")
               

    def load_circles_info(self,timing_info) -> list:
        circles_info = []
        self.found_first_hit_object = False
        for line in timing_info:
            print(line)
            parts = line.split(",",5)
            circle_info = self.get_timing_info(parts)
            circles_info.append(circle_info)
        return circles_info
    
    def start_sequence(self): #Creates a schedule for tkitner to run
        print("Start Script")
        # self.start_time = self.circles_info[0][2]
        counter = 0
        for x,y,hit_time,object_type,slider_info in self.circles_info:
            #Since Python stores reference to stuff, once this loop is closed, it points to nothing, hence the need to store vars
            #Clamping for the first hit object(since the anchor point is based on the first hit object)
            delay = max(0,hit_time + self.start_time)  #I legit do not know how i came up with this
            if counter == 0:
                delay = self.start_time
                
            self.scheduled_tasks.append(self.root.after(delay,
                                        lambda x=x,y=y,object_type=object_type,slider_info=slider_info: self.draw_circle(x,y,object_type,slider_info)))
            counter += 1
    
    def remove_circle(self,hit_object_id,*args):
        self.bg.delete(hit_object_id)
        # if premature_click:
        #     self.root.after_cancel(args[0])
        
    def draw_circle(self,x,y,object_type,slider_info):
        FILL_COLOR =  "red" if object_type == "circle" else "green"
        if object_type == "circle":
            circle_id = self.bg.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill=FILL_COLOR)
            task_id = self.root.after(self.preempt,lambda circle_id=circle_id: self.remove_circle(circle_id))
            self.hit_objects[circle_id] = {"x":x,"y":y,"task_id":task_id} #Used to track if the player clicks prematurely
            self.scheduled_tasks.append(task_id)
                
        elif object_type =="slider":
            slider_start = self.bg.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill=FILL_COLOR)
            task_id = self.root.after(self.preempt,lambda circle_id=slider_start: self.remove_circle(circle_id)) #TODO:
            self.hit_objects[slider_start] = {"x":x,"y":y,"task_id":task_id} #Used to track if the player clicks prematurely
            