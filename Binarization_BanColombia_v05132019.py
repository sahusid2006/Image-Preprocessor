#!/usr/bin/env python
# coding: utf-8

# In[90]:


#Importing relevant libraries
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

#Defiing Function for creating folder structure
def assure_path_exists(path):
        if not os.path.exists(path):
                os.makedirs(path)

###/////////////////////FUNCTION FOR BINARIZING IMAGES - OTSU BINARIZATION///////////////////////###
def binarizer(inputpath, bzpath):
    
    #Assigining arguements
    gspath = inputpath + '/Grayscale/'
    
    #Calling Directory Creation function for creating folder for Grayscale images
    assure_path_exists(gspath)
    
    #Looping through each file in a folder
    listing = os.listdir(inputpath)
    for infile in listing:
        #Building paths for individual files
        imgpath = inputpath + '/' + infile
        gsimgpath = gspath + '/' + infile
        
        #Checking whether the files are relevant
        filecheck = os.path.isfile(imgpath)
        if filecheck == True:
            image = cv2.imread(imgpath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(gsimgpath,gray)
            #Reinitializing gray variable
            gray = ''
        else:
            continue

    #Looping through each file in a folder
    listing = os.listdir(gspath)
    for infile in listing:
        gsimgpath = gspath + '/' + infile
        bzimgpath = bzpath + '/' + infile
        img = cv2.imread(gsimgpath,0)

        #Applying default OTSU's Binarization
        ret,thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imwrite(bzimgpath,thresh1)
        # Reinitializing thresh1
        thresh1 = ''
        
##/////////////////END OF FUNCTION//////////////////////////////////##


# In[ ]:




