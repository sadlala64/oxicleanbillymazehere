import PIL
from PIL import Image
import os  
directory = os.path.dirname(os.path.realpath(__file__))
new_directory = os.path.join(directory, 'modified')
im = Image.open("oxiclean orange bar.png") 
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

def paste_image():
    filename,filetype = os.path.splitext
    new_image = im.past(im,(20,20))
    new_image_filename = os.path.join(new_directory, filename + '.png')
    new_image.save(new_image_filename)    

def paste_on_all_images(directory=None):
    if directory == None:
        directory = os.getcwd()
    new_directory = os.path.join(directory, 'modified') 
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    image_list, file_list = get_images(directory)     
    for n in range(len(image_list)):
        filename, filetype = os.path.splitext(file_list[n])
        new_image = paste_image()
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    