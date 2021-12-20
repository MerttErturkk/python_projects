import numpy as np
from PIL import Image

from skimage import color
from skimage.filters import threshold_otsu
from skimage.transform import rescale


"""
This code is going to reduce 19 MB of pictures into 1 MB of thresholded binary images

Pictures are taken by me, They are the notes i took while i was studying SQL queries, 
PDF file that i included can be useful for whomever interested.

"""



def get_image(filename,root):
    img = Image.open(root+"/"+filename)
    return np.array(img)

# pipeline each of the pictures
for i in range(10):      
    photo =get_image("P"+str(i+1)+".jpg","photos")
    photo_rescaled = rescale(photo, 3/4, 
                         anti_aliasing=True,
                         multichannel=True)
    
    gray = color.rgb2gray(photo_rescaled)
    thresh = threshold_otsu(gray)
    binary_global = gray > thresh + 0.06
    img= Image.fromarray(binary_global)
    img.save("photos_new/b"+str(i)+".jpg")


