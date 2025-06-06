import os
import subprocess
file_path = r'C:\Users\PC\Downloads\osu songs beatmap starter pack'
for file in file_path:
    file_name = os.path.join(file_path,file)
    if os.path.isfile(file_path):
        # Open the file in VS Code
        subprocess.run(["code", file_path])