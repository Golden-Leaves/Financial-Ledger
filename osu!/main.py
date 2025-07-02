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
        
        def normalize_name(name) -> str:#Removes any weird ahh punctuation(Windows folders can not contain most punc symbols)
            normalized_name = name.lower().translate(str.maketrans("","",string.punctuation))
            return normalized_name
        
        def get_map_name() -> str:
            while True:
                time.sleep(0.1)
                active_window = GetWindowText(GetForegroundWindow())
                if "osu!" in active_window and len(active_window) > 4:
                    return active_window
                
        def find_map_folder(map_name) -> str:
            try:
                with os.scandir(OSU_DIRECTORY) as dirs:
                    for dir in dirs:
                        if dir.is_dir() and len(dir.name.split(" ",1)) >= 2:
                            dir_name = dir.name.split(" ",1)[1]
                            print(dir_name,map_name)
                            if normalize_name(map_name.strip()) in normalize_name(dir_name.strip()):
                                return dir.path
            except Exception as e:
                print(f"Exception: {e}")
            
        def get_map_file(map_directory) -> str:

            with os.scandir(map_directory) as dir:
                for file in dir:
                    file_name = file.name
                    if file.name.endswith(".osu") and diff_name.lower() in file_name.lower():
                        print(map_name,diff_name)
                        with open(file.path,"r",encoding="utf-8") as f:
                            return f.read().strip()
        
        retry_counter = 0
        raw_map_name  = get_map_name().strip()
        reversed_rmname = raw_map_name[::-1]
        # WHY THE FUCK IS THE ARTIST's NAMES IN SQUARE BRACKETS AAAAAAAAAAAAAqqqA, THATS WHY THIS LOOKS OVER-ENGINEERED
        map_name = reversed_rmname[reversed_rmname.find("[") + 1::].strip()[::-1].split("-",1)[1].strip()
        diff_name = raw_map_name[raw_map_name.rfind("["):raw_map_name.rfind("]") + 1].strip()
        map_directory = find_map_folder(map_name)
        print(map_directory,"Finished scanning map directory.")
        map_file = get_map_file(map_directory)
        overlay = OsuOverlay(map_file)
        overlay.initialize_script()
    
            
if __name__ == "__main__":
    main()