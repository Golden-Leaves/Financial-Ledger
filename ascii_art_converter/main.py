import PIL
from PIL import Image
import os
import numpy as np
from numpy.typing import NDArray
from PIL.Image import Image as PILImage

ASCII_CHARS = "@%#*+=-:. "

def asciify(arr: NDArray,character_set : str = "@%#*+=-:. "):
    """Asciifies an image's greyscale numpy array\n
    You can specify your own character set
    """
    ascii_arr = arr.flatten() #Numpy arrays are 2D by default????
    ascii_pixels = [character_set[int(pixel) * len(character_set) // 256] for pixel in ascii_arr] #uint8 sucks so u need to int()
    #reshape() prevents the ascii from being dumped into a single line, litreal spaghetti
    return np.array(ascii_pixels).reshape(arr.shape)

def output_ascii(ascii_img: NDArray):
    """Outputs an ascii image, from an ascii grid"""
    for row in ascii_img:
        print("".join(row))

def resize_image(img: PILImage,width : int = 55) -> PILImage: #Makes the image smaller(while still keeping aspect ratio)
    """Resizes an image to fit into smaller resolutions while still keeping aspect ratio
    Used for stuff such as for terminals\n
    Width is optional, defaults to 55"""
    img_width, img_height = img.size
    new_width = width
    new_height = int(new_width * img_height/img_width * 0.55) #Custom thumbnail() with fudge factor
    #Convert to Grayscale　and Resize
    img = img.resize((new_width, new_height)) #Fudge factor, turns width:height ratio to 1:1 for characters
    return img

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Choose images with high contrast or low res for best results.")
    file_path = input("Input a valid file path(must be an image) here: ").strip('"')
    #Brightness Levels

    try:
        img = Image.open(file_path)
    except FileNotFoundError: #Path doesn't exist
        print("That path doesn't exist...")
        return
    except PIL.UnidentifiedImageError: #File not an image
        print("Specified path is not an image...")
        return
        
    img = resize_image(img)
    ascii_img = asciify(np.array(img.convert("L"))) 
    output_ascii(ascii_img)
    

if __name__ == "__main__":
    main()
