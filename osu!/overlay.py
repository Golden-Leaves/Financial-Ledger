from tkinter import *
import win32gui
import win32con
class OsuOverlay():
    def __init__(self,map_file):
        self.map_file = map_file
        self.sections = self.map_file.split("\n\n")
        self.mods = {"DT":False,"HR":True,"HD":False,"FL":True} #Sample data for now
        self.get_map_data()
        print(self.CS,self.preempt)
    def initialize_script(self):
        self.master = Tk()
        self.master.bind("q", lambda e: (self.master.destroy(), print("Window Destroyed")))
        self.master.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}")
        self.master.overrideredirect(1)
        self.master.attributes('-topmost', True)
        self.master.config(bg='white')
        self.master.wm_attributes('-transparentcolor', 'white')
        self.canvas = Canvas(self.master, highlightthickness=0,width=self.master.winfo_screenwidth(),height = self.master.winfo_screenheight())
        self.canvas.create_text(960, 620, text="Overlay Online", font=("Segoe UI", 20), fill="black")  # This will also show
        self.canvas.pack(fill=BOTH, expand=True)
        self.master.update() #Update it NOW, you dont need to wait for mainloop
        #Make the window click-throughable and transparent babysssssss
        self.setClickthrough(self.canvas.winfo_id()) #It needs the handle, not the window itself...
        self.master.mainloop()

    def setClickthrough(self,hwnd):
        print("setting window properties")
        try:
            styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
            styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
            win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
            win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)

        except Exception as e:
            print(e)

    def get_map_data(self) -> None:
            try:
                
                for section in self.sections:
                    if "[Difficulty]" in section:
                        self.difficulty_data = section
                        for line in self.difficulty_data.split("\n"):
                            if "ApproachRate" in line:
                                AR = float(line.split(":")[1])
                                #AR time calculations: https://osu.ppy.sh/wiki/en/Beatmap/Approach_rate
                                if AR < 5: #TODO: Implement fade in animation later(I love HD)
                                    self.preempt = 1200 + 600 * (5 - AR) / 5
                                elif AR == 5:
                                    self.preempt = 1200
                                elif AR > 5:
                                    self.preempt = 1200 - 750 * (AR - 5) / 5
                                else:#AR11 lol
                                    self.preempt = 300
                            if "CircleSize" in line:
                                self.CS = float(line.split(":")[1])
                        
                    elif "[HitObjects]" in section:
                        self.timing_info = section.split("\n")[1::] #Skips the header
                        break
                    
                   
                                
            except Exception as e:
                print(f"Exception: {e}")
    
    def get_timing_info(self,section) -> tuple: #https://osu.ppy.sh/wiki/en/Client/File_formats/osu_%28file_format%29
        def get_slider_info(slider_data) -> list:
            return []
        try:
            for line in section:
                    print(f"LINE: '{line}'")
                    if not line.strip(): #Random new lines my beloved
                        continue
                    
                    object_info = line.split(",")
                    if len(object_info) > 6: #Slider or nah
                        slider_info = get_slider_info(object_info)
                    else:
                        x = line[0]
                        y = line[1]
                        hit_time = line[2] #In ms since the map started
            return (x,y,hit_time,slider_info)
        except Exception as e:
            print(f"Exception: {e}")
    
    def load_circle_info(self):
        for line in self.timing_info:
            parts = line.split(",")
            self.load_circle_info = self.get_timing_info(parts)