# The MIT License

# Copyright (c) 2022 Sougato Bagchi

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# read calibration parameters (intrinsic and extrinsic) from the
# calibration file
# camera calibration (takes care of the intrinsic parameters)
# these are given/should be provided with the dataset 

# Import Libraries 
import pandas as pd
import numpy as np 
import cv2


df = pd.read_csv('./sample_data/calib.txt', header=None, delimiter=' ')
arr = df.to_numpy()

# this(KITTI) must be a quad camera setup. So there's 4 intrinsic parameters 
# Intrinsic matrix for the left/reference camera 
# Bit of python dosage -> np.vstack((arr1,arr2)).T || for transpose(not required here)
p1 = np.vstack((arr[0,1:5],arr[0,5:9],arr[0,9:13])) 
p2 = np.vstack((arr[1,1:5],arr[1,5:9],arr[1,9:13])) 

# read the images, and also convert to grayscale
I1_l = cv2.cvtColor(cv2.imread('./sample_data/image_2/000000.png'), cv2.COLOR_BGR2GRAY)
I1_r = cv2.cvtColor(cv2.imread('./sample_data/image_3/000000.png'), cv2.COLOR_BGR2GRAY)
I2_l = cv2.cvtColor(cv2.imread('./sample_data/image_2/000001.png'), cv2.COLOR_BGR2GRAY)
I2_r = cv2.cvtColor(cv2.imread('./sample_data/image_3/000001.png'), cv2.COLOR_BGR2GRAY)

# call the visual odometry 
