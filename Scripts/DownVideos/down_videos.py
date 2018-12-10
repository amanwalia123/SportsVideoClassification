#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 05:22:21 2018

@author: aman

Usage :

python read_csv.sh <CSV file containing links and time> <Folder to download(NO SLASH AT THE END)>
"""
from __future__ import unicode_literals
import csv 
import sys
import subprocess as sp
import youtube_dl
import platform
import os


if platform.system() == 'Linux':
    FFMPEG_BIN = "ffmpeg" # on Linux ans Mac OS

if platform.system() == 'Windows':
    FFMPEG_BIN = "ffmpeg.exe" # on windows


ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
 
CSV_FILE = sys.argv[1]
    
f = open(CSV_FILE, 'r')
dataset_folder = sys.argv[2] + "/" + "Videos"

reader = csv.reader(f)

for row in reader:
    category = str(row[0]).rstrip()
    link = str(row[1]).rstrip()
    time = str(row[2]).rstrip()
    dur = str(row[3]).rstrip()
    
    vid_name = link.split('=')[1].replace('-','_') + ".mp4"
    
    directory = dataset_folder + "/" + category 
    
    if not os.path.exists(directory):
        os.makedirs(directory) 
       
    with ydl:
        result = ydl.extract_info(link,download=False)
        
    if 'entries' in result:
       # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
    # Just a video
        video = result
  
    
    if os.path.exists(directory + "/" + vid_name) == False:
        
        formats = video['formats']
        formats = [x for x in formats if x['vcodec'] != 'none']
        formats = sorted(formats, key=lambda k: k['width'], reverse=True)
        
        for _format in formats:
            if _format['vcodec'] != 'none':
                url = _format['url']
                command = [ FFMPEG_BIN,
                            '-ss',time,
                            '-t',dur,
                            '-i', url, 
                             directory + "/" + vid_name ]
                ffmpeg = sp.Popen(command, stderr=sp.STDOUT,stdout = sp.PIPE)
		out, err = ffmpeg.communicate()
                if os.path.exists(directory + "/" + vid_name):
                    break;
            
    
    
    
f.close()
