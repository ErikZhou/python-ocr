from PIL import Image
import pytesseract
import cv2

def imcrop(name):
    img=cv2.imread(name)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    newx = 100
    newy = 100
    newimage = cv2.resize(img,(newx,newy))
    height, width, channels = img.shape
    x_start, y_start = width* 0.01, height * 0.4
    x_end, y_end = width * 0.75, height * 0.85
    refPoint = [(x_start, y_start), (x_end, y_end)]
    roi = img_gray[int(refPoint[0][1]):int(refPoint[1][1]), int(refPoint[0][0]):int(refPoint[1][0])]
    ret,img_thresh=cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite('1'+name,roi)
    #cv2.imshow('cropped',roi)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    return;
