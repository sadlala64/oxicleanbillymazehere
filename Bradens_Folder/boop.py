
from __future__ import print_function
import PIL
from PIL import Image
import os  
x = input('What do you want to do?\n1:Paste Logo\n2:End\n')
x == int(x)
directory = os.path.dirname(os.path.realpath(__file__))
new_directory = os.path.join(directory, 'modified')
orange = Image.open("oxicleanorangebar.png")
memory = Image.open("logo.png") 
directory_list = os.listdir(directory)
#sets up directorys and constants

if x == 1:
    y = input('Which Logo Would you like to use?\n1:Oxiclean Orange Bar\n2:In memory of Billy Maze\n')
    y == int(y)
    if y == 1: 
        xc = input('X-Coordinate?\n')
        yc = input('Y-Coordinate?\n')
        xc == int(xc)
        yc == int(yc)
        #has to ask for x and y cooridinates 
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
                #Gets images to paste on
        def paste_logo(x,y,directory=None):
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
                new_image.paste(orange,(xc,yc))
                filename, filetype = os.path.splitext(file_list[n])
                new_image_filename = os.path.join(new_directory, filename + '.png')
                new_image.save(new_image_filename)
                #Pastes logo on all images in folder
    if y == 2: 
        xc = input('X-Coordinate?\n')
        yc = input('Y-Coordinate?\n')
        xc == int(xc)
        yc == int(yc)
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

        def paste_logo(x,y,directory=None):
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
                new_image.paste(memory,(xc,yc))
                filename, filetype = os.path.splitext(file_list[n])
                new_image_filename = os.path.join(new_directory, filename + '.png')
                new_image.save(new_image_filename)
if x == 2:
    exit()
paste_logo(xc,yc)
#Pastes Logo