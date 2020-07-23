## Getting start
The ```opencv_python-4.3.0.36-cp36-cp36m-linux_x86_64(gstreamer_enabled).whl``` wheel is a pre-build of python package ```opencv-python``` with gstreamer 1.14 enabled. Please refer to [manual builds](https://github.com/skvark/opencv-python#manual-builds) for details build instructions.

Install the package by running ```pip install opencv_python-4.3.0.36-cp36-cp36m-linux_x86_64(gstreamer_enabled).whl```.

## Manual builds
1. Clone this repository ```git clone --recursive https://github.com/skvark/opencv-python.git```
- ```git checkout 36```
2. Add custom Cmake flags if needed,
```
export CMAKE_ARGS="-D BUILD_TIFF=ON -D WITH_CUDA=OFF -D WITH_OPENGL=ON -D WITH_OPENCL=ON -D WITH_GTK=ON -D WITH_GTK_2_X=ON -D WITH_IPP=OFF -D WITH_TBB=ON -D BUILD_TBB=ON -D WITH_GST=ON -D WITH_EIGEN=OFF -D WITH_V4L=ON -D WITH_LIBV4L=ON -D WITH_FFMPEG=ON"
```
3. Select the version which you wish to build with ```ENABLE_CONTRIB``` and ```ENABLE_HEADLESS```: i.e. ```export ENABLE_CONTRIB=1``` if you wish to build ```opencv-contrib-python```
4. Run ```pip wheel . --verbose```. NOTE: make sure you have the latest pip, the pip wheel command replaces the old python setup.py bdist_wheel command which does not support pyproject.toml. 
- cmake qt build error ```sudo apt-get install qt4-default```
