#!/usr/bin/env python
# 1500921, 3 December, 2015
# The following code was made following the tutorial in:
# https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html
# The official documentation of the functions used was checked from:
# http://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html
#
# Here is the procedure followed to answer the first part of the assignment.

import numpy as np
import cv2
import glob

chessboard = [7, 8]

# prefill matrix with 0,0,0s for the object points.
# Object points are the real points in the real world.
objp = np.zeros((chessboard[1]*chessboard[0], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboard[0],0:chessboard[1]].T.reshape(-1,2)

# Array for the object and image points of every image.
objpoints = [] # Points in the real world in 3D space.
imgpoints = [] # Points in the images in 2D space.

images = glob.glob('*.png')

for fname in images:
    img = cv2.imread(fname)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(img, (chessboard[0], chessboard[1]), flags=cv2.cv.CV_CALIB_CB_ADAPTIVE_THRESH)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)

# Calibrate camera with previous data
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[1::-1], None, None)

# Calculate the focal point by averaging fx and fy (which are different due to factors in the lens of the camera.
focal_point = (mtx[0][0] + mtx[1][1]) / 2
print mtx
print "The focal point is {0}.".format(focal_point)
