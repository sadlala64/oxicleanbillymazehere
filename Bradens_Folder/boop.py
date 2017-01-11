from __future__ import print_function
import PIL
from PIL import Image
import os  
directory = os.path.dirname(os.path.realpath(__file__))
new_directory = os.path.join(directory, 'modified')
im = Image.open("oxicleanorangebar.png") 
directory_list = os.listdir(directory)

def get_images(directory=None):
    image_list = [] 
    file_list = []
    if directory == None:
        directory = os.getcwd() 
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass 
    return image_list, file_list          

def orange_logo(x,y,directory=None):
    if directory == None:
        directory = os.getcwd()
    new_directory = os.path.join(directory, 'modified') 
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    image_list,file_list = get_images(directory) 
    for n in range(len(file_list)):
        new_image= image_list[n]
        new_image.paste(im,(x,y))
        filename, filetype = os.path.splitext(file_list[n])
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    