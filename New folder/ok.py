import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw

directory = os.path.dirname(os.path.abspath(__file__))  
their_file = os.path.join(directory, 'Oxiclean_36a03f_146819.jpg')

their_file = PIL.Image.open(their_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(their_file, interpolation='none')

axes[1].imshow(their_file, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)


# Open, resize, and display earth
logo_file = os.path.join(directory, 'logo.png')
logo_img = PIL.Image.open(logo_file)
logo_small = logo_img.resize((200, 100)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(logo_img)
axes2[1].imshow(logo_small)


# Paste earth into right eye and display
# Uses alpha from mask
their_file.paste(logo_small, (200, 200), mask=logo_small) 
# Display
fig3, axes3 = plt.subplots(1, 1)
axes3.imshow(their_file, interpolation='none')
fig3.show(2)