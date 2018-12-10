#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:53:16 2018

@author: aman
"""

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from keras import backend 
import os
import sys
import glob
import numpy as np

# load the model
model = VGG16()


rootkeyframes = str(sys.argv[1])

if not rootkeyframes.endswith('/'):
    rootkeyframes = rootkeyframes + "/"   

# Directory where vgg object bank is created
rootvggobjbank = str(sys.argv[2])

if not rootvggobjbank.endswith('/'):
    rootkeyframes = rootkeyframes + "/"


cat_dirs = os.walk(rootkeyframes).next()[1]

for category in cat_dirs:
    
    #print("*****"+category+"****")
    
    # Make category directory in object bank root folder
    obj_cat_dir = rootvggobjbank + category
    
    if not os.path.exists(obj_cat_dir):
            os.makedirs(obj_cat_dir)
    
    
    kfdir_path = rootkeyframes + category
    keyframe_dirs = os.walk(kfdir_path).next()[1]
    
    for kfdirs in keyframe_dirs:
        
        # Make directory for each video in each category
        obj_kf_dir = obj_cat_dir + "/" + kfdirs
        if not os.path.exists(obj_kf_dir):
            os.makedirs(obj_kf_dir)
        
        
        kf_path = kfdir_path + "/"+kfdirs
        #print(kf_path)
        
        if os.path.exists(kf_path+"/plot.png"):
            os.remove(kf_path+"/plot.png")
        
        inputdirectory = os.path.abspath(kf_path) + "/"
        outputdirectory = os.path.abspath(obj_kf_dir ) + "/"
        
        
        for fname in glob.glob(inputdirectory + "/*.jpg"):
            
            img_name = fname.split('.')[0].split('/')[-1] 
                       
            # load an image from file
            image = load_img(fname, target_size=(224, 224))
            # convert the image pixels to a numpy array
            image = img_to_array(image)
            # reshape data for the model
            image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
            # prepare the image for the VGG model
            image = preprocess_input(image)
            # predict the probability across all output classes
            yhat = model.predict(image)
            # convert the probabilities to class labels
            label = decode_predictions(yhat)
            # with a Sequential model
            get_2ndlast_layer_output = backend.function([model.layers[0].input],
                                  [model.layers[-2].output])
            layer_output = get_2ndlast_layer_output([image])[0]
            
            out_file_name = outputdirectory + img_name + "_vgg.feat"
            
            np.savetxt(out_file_name, layer_output)
            print("Generated "+ out_file_name)
