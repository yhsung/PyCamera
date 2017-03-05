#!/usr/bin/python3
import os
from picamera import PiCamera, Color
from time import sleep
camera = PiCamera()
camera.rotation = 180
camera.resolution = (1024, 768)
camera.annotate_background = Color('blue')                                      
camera.annotate_foreground = Color('yellow')
camera.annotate_text_size = 24
directory = 'TimeLapse'
if not os.path.exists(directory):
    os.makedirs(directory)
for awb_mode in camera.AWB_MODES:
    camera.awb_mode = awb_mode
    for exp_mode in camera.EXPOSURE_MODES:
        camera.exposure_mode = exp_mode
        camera.capture('{}/{}_{}.jpg'.format(directory, awb_mode, exp_mode))
