#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:06:07 2018

@author: aman
"""

import os
import subprocess as sp
import sys

# Directory where keyframes are located
rootkeyframes = str(sys.argv[1])

if not rootkeyframes.endswith('/'):
    rootkeyframes = rootkeyframes + "/"   

# Directory where object bank is created
rootobjbank = str(sys.argv[2])

if not rootobjbank.endswith('/'):
    rootkeyframes = rootkeyframes + "/"


rootobgen = str(sys.argv[3])
if not rootobgen.endswith('/'):
    rootobgen = rootobgen + "/"
    
OB_BANK_GEN = "./OBmain"

rootobgen = os.path.abspath(rootobgen)



cat_dirs = os.walk(rootkeyframes).next()[1]

for category in cat_dirs:
    
    #print("*****"+category+"****")
    
    # Make category directory in object bank root folder
    obj_cat_dir = rootobjbank + category
    
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
        print(kf_path)
        
        if os.path.exists(kf_path+"/plot.png"):
            os.remove(kf_path+"/plot.png")
        
        inputdirectory = os.path.abspath(kf_path) + "/"
        outputdirectory = os.path.abspath(obj_kf_dir ) + "/"
        
        
        sp.call([OB_BANK_GEN , inputdirectory , outputdirectory])
       