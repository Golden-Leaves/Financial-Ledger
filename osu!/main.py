import time
import os
import pyautogui
from overlay import OsuOverlay
from win32gui import GetWindowText, GetForegroundWindow 
import string
os.chdir(os.path.dirname(__file__))
def main():
    while True:
        if input("Press Enter to continue or 'q' to quit: ").lower() == 'q':
            break
        OSU_DIRECTORY = r"C:\Users\PC\AppData\Local\osu!\Songs"
        overlay = OsuOverlay()
        def normalize_name(name) -> str:#Removes any weird ahh punctuation(Windows folders can not contain most punc symbols)
            return name.lower().translate(str.maketrans("","",string.punctuation))
        
        def get_map_name() -> str:
            while True:
                time.sleep(0.1)
                active_window = GetWindowText(GetForegroundWindow())
                if "osu!" in active_window:
                    return active_window
                
        def find_map_folder() -> str:
            try:
                with os.scandir(OSU_DIRECTORY) as dirs:
                    for dir in dirs:
                        if dir.is_dir() and len(dir.name.split(" ",1)) >= 2:
                            dir_name = dir.name.split(" ",1)[1]
                            print(dir_name,map_name)
                            if normalize_name(dir_name.strip()) in normalize_name(map_name.strip()):
                                return dir.path
            except Exception as e:
                print(f"Exception: {e}")
            
        def get_map_file() -> str:
            print(map_name,diff_name)
            with os.scandir(map_directory) as dir:
                for file in dir:
                    file_name = file.name
                    if file.name.endswith(".osu") and diff_name in file_name:
                        with open(file.path,"r",encoding="utf-8") as f:
                            return f.read()
        def get_map_data():
            try:
                sections = map_file.split("\n\n") #Split into individual sections
                for section in sections:
                    if "[Difficulty]" in section:
                        difficulty_data = section
                        print(difficulty_data)
            except Exception as e:
                print(f"Exception: {e}")
                
        raw_map_name  = get_map_name().strip()
        reversed_rmname = raw_map_name[::-1]
        map_name = raw_map_name[raw_map_name.find("["):raw_map_name.rfind("]") + 1].split(" [")[0]
        # WHY THE FUCK ARE THE ARTIST's NAMES IN SQUARE BRACKETS AAAAAAAAAAAAAA, THATS WHY THIS LOOKS OVER-ENGINEERED
        diff_name = reversed_rmname[reversed_rmname.find("]"):reversed_rmname.find("[") + 1][::-1].strip()
        map_directory = find_map_folder()
        print(map_directory,"Finished scanning map directory.")
        map_file = get_map_file()
        get_map_data()
        overlay.initialize_script()
    
            
if __name__ == "__main__":
    main()