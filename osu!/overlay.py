from tkinter import *
import win32gui
import win32con
class OsuOverlay():
    def __init__(self,map_file):
        self.map_file = map_file
        self.sections = self.map_file.split("\n\n")
        self.mods = {"DT":False,"HR":True,"HD":False,"FL":True} #Sample data for now
        self.get_map_data(self.sections)
    def initialize_script(self):
        root = Tk()
        root.geometry("1920x1080")
        root.config(bg='#add123')
        root.wm_attributes('-transparentcolor', '#add123')
        root.attributes("-fullscreen", True)
        root.wm_attributes("-topmost", 1)
        bg = Canvas(root, width=1920, height=1080)
        # label = Label(root, text="👁️‍🗨️ CLICK-THROUGH TESTING ZONE", 
        #                 font=("Segoe UI", 30), fg="red", bg="white")
        # label.place(x=300, y=500)
        #Make the window click-throughable and transparent babysssssss
        self.setClickthrough(bg.winfo_id())
        
        self.load_circles_info(self.timing_info)
        root.mainloop()
    
        
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
                                
                            
                        
                    elif "[HitObjects]" in section:
                        self.timing_info = section.split("\n")[1::] #Skips the header
                        break
                    
                   
                                
            except Exception as e:
                print(f"Exception: {e}")
    
    def get_timing_info(self,parts) -> tuple: #https://osu.ppy.sh/wiki/en/Client/File_formats/osu_%28file_format%29
        def get_slider_info(slider_data) -> tuple:
            points = slider_data.split("|")
            slider_points = tuple(map(lambda point: point.split(":"),int,points))
            return slider_points
        try:
            
                print(f"LINE: {parts}")
               
                

                x = parts[0]
                y = parts[1]
                hit_time = parts[2]
                if len(parts) > 6: #Slider or nah
                    slider_info = get_slider_info(parts)
                    object_type = "slider"
                else:
                    slider_info = None
                    object_type = "circle"
              
                    slider_info = None
                print(slider_info)
                return (x,y,object_type,slider_info)
        
        except Exception as e:
            print(f"Exception: {e}")
               

    def load_circles_info(self,timing_info) -> list:
        circles_info = []
        for line in timing_info:
            parts = line.split(",")[:len(line.split(",")) - 1]
            circle_info = self.get_timing_info(parts)
            circles_info.append(circle_info)
        return circles_info