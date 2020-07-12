## Getting start

Launch some random stuff
```
gst-launch-1.0 videotestsrc pattern=ball ! video/x-raw, width=1920, height=1080, framerate=60/1 ! videoconvert ! ximagesink
```

Mirror the screen and display it
```
gst-launch-1.0 ximagesrc xname=gst-launch-1.0 use-damage=0 ! video/x-raw,framerate=60/1 ! videoconvert ! ximagesink
```

Openning two screen at a time
```
gst-launch-1.0 videotestsrc ! videoconvert ! tee name=t ! queue ! ximagesink t. ! queue ! ximagesink
```

or similarily penning camera on 3 viewer at a time
```
gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! tee name=t ! queue ! ximagesink t. ! queue ! ximagesink t. ! queue ! ximagesink
``` 

Spin two pipeline, one for recording one for display
```
gst-launch-1.0 v4l2src device=/dev/video0 ! timeoverlay ypad=5 xpad=5 auto-resize=false ! video/x-raw, width=1920, height=1080, framerate=60/1 ! videoconvert ! tee name=t ! queue ! x264enc ! mp4mux ! filesink location="video.mp4" t. ! queue leaky=1 ! xvimagesink
```