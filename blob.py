import cv2
import sys
import numpy as np

def imsplit(name, debug=False):
    im = cv2.imread('1'+name)
    # Setup BlobDetector
    detector = cv2.SimpleBlobDetector_create()
    params = cv2.SimpleBlobDetector_Params()
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 2
    params.maxArea = 4000000
    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1
    # Filter by Convexity
    params.filterByConvexity = False
    #params.minConvexity = 0.87
    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.8

    # Distance Between Blobs
    params.minDistBetweenBlobs = 24
    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
    #retval, im = camera.read()
    overlay = im.copy()

    keypoints = detector.detect(im)
    x_start, y_start = 0, 0
    x_end, y_end = 0, 0
    for k in keypoints:
        if debug:
            cv2.circle(overlay, (int(k.pt[0]), int(k.pt[1])), int(k.size/2), (0, 0, 255), -1)
       
       #print(int(k.pt[0]))
        #print(int(k.pt[1]))
        if int(k.pt[0]) > x_start:
            x_start = int(k.pt[0])
            y_start = int(k.pt[1])
        #cv2.line(overlay, (int(k.pt[0])-20, int(k.pt[1])), (int(k.pt[0])+20, int(k.pt[1])), (0,0,0), 3)
        #cv2.line(overlay, (int(k.pt[0]), int(k.pt[1])-20), (int(k.pt[0]), int(k.pt[1])+20), (0,0,0), 3)

    w,h = 30 ,26
    x_start, y_start = x_start - w/2, y_start - h/2
    x_end, y_end = x_start + w, y_start + h

    opacity = 0.5
    cv2.addWeighted(overlay, opacity, im, 1 - opacity, 0, im)

    # Uncomment to resize to fit output window if needed
    #im = cv2.resize(im, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    refPoint = [(x_start, y_start), (x_end, y_end)]
    roi = im[int(refPoint[0][1]):int(refPoint[1][1]), int(refPoint[0][0]):int(refPoint[1][0])]
    cv2.imwrite('2'+name,roi)

    if debug:
        cv2.imshow("Output", overlay)
        cv2.imwrite('2.png',overlay)
        cv2.waitKey()
        cv2.destroyAllWindows()
    
    print('imcrop done')
    return;
