import cv2
import os
from main import resize_image
def extract_video_frames(video_path: str, output_dir: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),"frames"),subfolder_name:str = "default"):
    """Extract all of the frames of a video then saves in the specified directory\n
    Defaults to saving in a frames folder in the current directory, you can further create subfolders to manage things better
    subfolder_name defaults to "default", change it to anything you'd like
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

       #Resize image if needeed
        frame = resize_image(frame)  # change size as needed

        #Save file as PNG
        final_output_dir = os.path.join(output_dir, subfolder_name)
        filename = os.path.join(final_output_dir, f"frame_{count:04d}.png") #frame_0001,...
        
        cv2.imwrite(filename, frame) #Writes the image as a png by default
        count += 1

    cap.release() #Basically a .close() but for videos instead of txt
    print(f"Extracted {count} frames to '{output_dir}/'")

if __name__ == "__main__":
    extract_video_frames("C:/Users/Admin/PycharmProjects/project_1/openCV.mp4")
