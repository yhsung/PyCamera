#!/usr/bin/python3
import os
import tqdm
from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
camera.rotation = 0
#camera.resolution = (1024, 768)
camera.resolution = (640, 480)
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text_size = 24
directory = 'SingleCapture'
if not os.path.exists(directory):
    os.makedirs(directory)
for awb_mode, v1 in tqdm.tqdm(camera.AWB_MODES.items()):
    camera.awb_mode = awb_mode
    for exp_mode, v2 in tqdm.tqdm(camera.EXPOSURE_MODES.items()):
        camera.exposure_mode = exp_mode
        camera.capture('{}/{}_{}.jpg'.format(directory, awb_mode, exp_mode))
