# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:03:26 2020

@author: Parshva Timbadia
"""


from __future__ import unicode_literals
import youtube_dl


SAVE_PATH='C:/Users/HP/Desktop/TEST'
ydl_opts = {
    
    'writesubtitles': True,
    'writeautomaticsub':True,
    'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
    'skip_download': True,
    'subtitlesformat':'srt'
    }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=nIwU-9ZTTJc'])
    


    
    
