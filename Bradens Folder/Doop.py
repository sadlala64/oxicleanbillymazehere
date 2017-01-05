from PIL import Image
import os
im = Image.open("oxiclean orange bar.png")
directory = os.path.dirname(os.path.realpath(__file__))
image_list = [] # Initialize aggregaotrs
file_list = []   
for n in range(len(image_list)):
    filename, filetype = os.path.splitext(file_list[n])
    new_image = im.past(im,(20,20))
    new_image_filename = os.path.join(new_directory, filename + '.png')
    new_image.save(new_image_filename)    