import numpy as np
import cv2
from multiprocessing import Process

print(cv2.getBuildInformation())

"""
# udp streaming sending side
gst-launch-1.0 videotestsrc pattern=ball ! video/x-raw, width=1920, height=1080, framerate=60/1 ! videoconvert ! tee name=t ! queue ! x264enc ! rtph264pay ! udpsink host=127.0.0.1 port=5000

# udp streaming receiver side
gst-launch-1.0 udpsrc port=5000 ! application/x-rtp, encoding-name=H264,payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! xvimagesink
"""

# cap = cv2.VideoCapture("v4l2src device=/dev/video0 ! videoconvert ! tee name=t ! queue ! ximagesink t. ! queue ! ximagesink t. ! queue ! appsink", cv2.CAP_GSTREAMER)

# QString GST_PIPELINE_RECORDING = "v4l2src device=%1 ! timeoverlay ypad=5 xpad=5 auto-resize=false ! video/x-raw, width=1920, height=1080, framerate=60/1 ! videoconvert ! tee name=t ! queue ! vaapivp9enc ! webmmux ! filesink location=%2 t. ! videocrop left=168 right=168 ! videoscale ! video/x-raw, width=1760, height=1200 ! queue leaky=1 ! videoconvert ! appsink drop = true";

# cap = cv2.VideoCapture("v4l2src device=/dev/video0 ! video/x-raw, width=1920, height=1080, framerate=60/1 ! tee name=t ! queue ! xvimagesink t. ! videoconvert ! queue leaky=1 ! videoconvert ! appsink drop = true", cv2.CAP_GSTREAMER)

cap = cv2.VideoCapture("videotestsrc pattern=ball ! video/x-raw, width=1920, height=1080, framerate=60/1 ! tee name=t ! queue ! xvimagesink t. ! videoconvert ! queue leaky=1 ! videoconvert ! appsink drop = true", cv2.CAP_GSTREAMER)

import time
t_0 = time.time()

while True:
    ret,frame = cap.read()
    if not ret:
        print('empty frame')
        continue    
    cv2.imshow('receive', frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
cap.release()