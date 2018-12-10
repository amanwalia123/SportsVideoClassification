# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:32:06 2018

@author: boshra.badran
"""

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


#rootobgen = str(sys.argv[3])
'''
if not rootobgen.endswith('/'):
    rootobgen = rootobgen + "/"
    
'''
OB_BANK_GEN = "./OBmain"

#rootobgen = os.path.abspath(rootobgen)



cat_dirs = os.walk(rootkeyframes).next()[1]

for category in cat_dirs:
    
    #print("*****"+category+"****")
    
    # Make category directory in object bank root folder
    obj_cat_dir = rootobjbank + "/"+category
    
    if not os.path.exists(obj_cat_dir):
            os.makedirs(obj_cat_dir)
    
    
    kfdir_path = rootkeyframes + category
    
    
    inputdirectory = kfdir_path + "/"
    outputdirectory = obj_cat_dir + "/"
        
        
    sp.call([OB_BANK_GEN , inputdirectory , outputdirectory])
