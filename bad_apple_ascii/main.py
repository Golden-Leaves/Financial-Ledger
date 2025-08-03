from ascii_art_generator.main import asciify,output_ascii,resize_image
from ascii_art_generator.video import extract_video_frames
import os
def main():
    extract_video_frames(video_path=r"C:\Users\PC\Downloads\Touhou - Bad Apple.mp4",subfolder_name="Bad Apple")
if __name__ == "__main__":
    main()