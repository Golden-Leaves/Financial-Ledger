from tkinter import *
import win32gui
import win32con
class OsuOverlay():
    def __init__(self,map_file):
        self.map_file = map_file
        self.scheduled_tasks  = []
        self.sections = self.map_file.split("\n\n")
        self.mods = {"DT":False,"HR":True,"HD":False,"FL":True} #Sample data for now
        self.get_map_data(self.sections)
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
                
                for section in sections:
                    if "[Difficulty]" in section:
                        self.difficulty_data = section
                        for line in self.difficulty_data.split("\n"):
                            
                            if "CircleSize" in line:
                                self.CS = float(line.split(":")[1])
                                self.radius = 54.4 - 4.48 * self.CS #https://osu.ppy.sh/wiki/en/Beatmap/Circle_size
                                
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
                                
                            
                        
                    elif "[HitObjects]" in section:
                        self.timing_info = section.split("\n")[1::] #Skips the header
                        break
                    
                   
                                
            except Exception as e:
                print(f"Exception: {e}")
    
    def get_timing_info(self,parts) -> tuple: #https://osu.ppy.sh/wiki/en/Client/File_formats/osu_%28file_format%29
        def get_slider_info(slider_data) -> tuple:
            points = slider_data.rsplit(",",1)[0].split(",",1)[0].split("|")

            slider_points = [tuple(map(int,point.split(":"))) for point in points[1::]]
            return slider_points
        try:
            
                print(f"LINE: {parts}")
               
                
                
                x = int(parts[0])
                y = int(parts[1])
                hit_time = int(parts[2])
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
        for line in timing_info:
            print(line)
            parts = line.split(",",5)
            circle_info = self.get_timing_info(parts)
            circles_info.append(circle_info)
        return circles_info
    
    def start_sequence(self):
        print("Start Script")
        for x,y,hit_time,object_type,slider_info in self.circles_info:
            #Since Python stores reference to stuff, once this loop is closed, it points to nothing, hence the need to store vars
            self.scheduled_tasks.append(self.root.after(hit_time,
                                        lambda x=x,y=y,object_type=object_type,slider_info=slider_info: self.draw_circle(x,y,object_type,slider_info)))
    def remove_circle(self,hit_object_id):
        self.bg.delete(hit_object_id)
        
    def draw_circle(self,x,y,object_type,slider_info):
        FILL_COLOR =  "red" if object_type == "circle" else "green"
        if object_type == "circle":
            circle_id = self.bg.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill=FILL_COLOR)
            self.scheduled_tasks.append(self.root.after(self.preempt,lambda circle_id=circle_id: self.remove_circle(circle_id)))