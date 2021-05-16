from PIL import Image
import PIL
import os
import glob

def compress(filename):
    img = Image.open("test_data/masked_images/"+filename) 
    print(f"The image size dimensions are: {img.size[0]} {img.size[1]}")

    img = img.resize((int(img.size[0]/4),int(img.size[1]/4)),Image.ANTIALIAS)
    img.save("test_data/compressed_images/"+filename,optimize=True,quality=30)
