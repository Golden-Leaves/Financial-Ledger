import cv2
import os
from .main import resize_image
from PIL import Image
import numpy as np
def extract_video_frames(video_path: str, output_dir: str = os.path.join(os.getcwd(), "frames"),subfolder_name:str = "default",overwrite = False):
    """Extract all of the frames of a video then saves in the specified directory\n
    Defaults to saving in a frames folder in the current directory, you can further create subfolders to manage things better
    subfolder_name defaults to "default", change it to anything you'd like\n
    Set overwrite=True to overwrite existing subfolders
    """
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise IOError("Couldn't open video file.")

    count = 0 #Counts the number of frames
    while True:
        success, frame = cap.read() 
        if not success:
            break  # end of video

        # Convert OpenCV frame (BGR) to PIL image (RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(frame_rgb)

    
        resized_pil_img = resize_image(pil_img)

        # Convert back to cv2(greyscale)
        frame = np.array(resized_pil_img)

        #Save file as PNG
        final_output_dir = os.path.join(output_dir, subfolder_name)
        
        final_output_dir = os.path.join(output_dir, subfolder_name)

        if os.path.exists(final_output_dir) and not overwrite:
            return "Subfolder already exists. Set overwrite=True to proceed."

        os.makedirs(final_output_dir, exist_ok=True)

        filename = os.path.join(final_output_dir, f"frame_{count:04d}.png")
        cv2.imwrite(filename, frame)
        count += 1
    cap.release() #Basically a .close() but for videos instead of txt
    print(f"Extracted {count} frames to '{output_dir}/'")

if __name__ == "__main__":
    extract_video_frames("C:/Users/Admin/PycharmProjects/project_1/openCV.mp4")
