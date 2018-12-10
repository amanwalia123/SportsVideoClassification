#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 00:20:30 2018

@author: aman
"""

import os
import sys
import genkeyframe


# Directory where Videos are located
vidpath = sys.argv[1]

# Directory where Keyframes are going to be stored
keypath = sys.argv[2]

# smoothing window threshold for moving camera
CAM_MOV_THRESH = 18

for root, dirs, files in os.walk(vidpath):
    for cat in dirs:
        
        kdir =  keypath +"/" + cat
        
        if not os.path.exists(kdir):
            os.makedirs(kdir)
    
        for root,dirs,vids in os.walk(vidpath+"/"+cat): 
            
            for v in vids:
            
                vid_name = str(v).split(".")[0]
                kf_dir = kdir + "/" + vid_name
                
                if not os.path.exists(kf_dir):
                    os.makedirs(kf_dir)
                
                videopath = vidpath+"/"+cat+"/"+v
                                
                genkeyframe.divideFrames(videopath,kf_dir,CAM_MOV_THRESH)