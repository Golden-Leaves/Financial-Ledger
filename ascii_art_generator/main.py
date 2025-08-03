import PIL
from PIL import Image
import os
import numpy as np
from numpy.typing import NDArray

def main():
    def asciify(arr: NDArray):
        ascii_arr = arr.flatten() #Numpy arrays are 2D by default????
        ascii_pixels = [ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256] for pixel in ascii_arr] #uint8 sucks so u need to int()
        #reshape() prevents the ascii from being dumped into a single line, litreal spaghetti
        return np.array(ascii_pixels).reshape(arr.shape)
    def output_ascii(ascii_img):
        for row in ascii_img:
            print("".join(row))
    def resize_image(img):
        img_width, img_height = img.size
        new_width = 55
        new_height = int(new_width * img_height/img_width * 0.55) #Custom thumbnail() with fudge factor
        #Convert to Grayscale　and Resize
        img = img.resize((new_width, new_height)).convert("L") #Fudge factor, turns width:height ratio to 1:1 for characters
        return img
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Choose images with high contrast or low res for best results.")
    file_path = input("Input a valid file path(must be an image) here: ").strip('"')
    #Brightness Levels
    ASCII_CHARS = "@%#*+=-:. "
 #len is 8 for some convinient math
    
    try:
        img = Image.open(file_path)
        
    except FileNotFoundError: #Path doesn't exist
        print("That path doesn't exist...")
    except PIL.UnidentifiedImageError: #File not an image
        print("Specified path is not an image...")
    # img_width, img_height = img.size
    # new_width = 55
    # new_height = int(new_width * img_height/img_width * 0.55) #Custom thumbnail() with fudge factor
    # #Convert to Grayscale　and Resize
    # img = img.resize((new_width, new_height)).convert("L") #Fudge factor, turns width:height ratio to 1:1 for characters
    img = resize_image(img)
    ascii_img = asciify(np.array(img)) 
    output_ascii(ascii_img)
    img.save("gray.jpg")
if __name__ == "__main__":
    main()