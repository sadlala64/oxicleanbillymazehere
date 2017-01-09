import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'Oxiclean_36a03f_146819.jpg')

student_file = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_file, interpolation='none')

axes[1].imshow(student_file, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.show()

# Open, resize, and display earth
earth_file = os.path.join(directory, 'logo.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
student_file.paste(earth_small, (150, 100), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_file, interpolation='none')
axes3[1].imshow(student_file, interpolation='none')
axes3[1].set_xlim(250, 300)
axes3[1].set_ylim(250, 300)
fig3.show()