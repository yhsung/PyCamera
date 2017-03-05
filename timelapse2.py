#!/usr/bin/python3
from picamera import PiCamera, Color
from time import sleep
from datetime import datetime
import os
camera = PiCamera()
camera.rotation = 180
camera.resolution = (1024, 768)
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text_size = 24
directory = 'TimeLapse'                                                         
if not os.path.exists(directory):
    os.makedirs(directory)
i=0
for counts in range(4000):
    timestamp = str(datetime.now())
    camera.annotate_text = '(Time: {})'.format(timestamp)
    print('{:0>5}'.format(i))
    camera.capture('{}/timelapse-{:0>5}.jpg'.format(directory, i))
    sleep(300)
    i+=1
