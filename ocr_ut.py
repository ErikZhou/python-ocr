import ocr
import tesseract
import pytesseract

from PIL import Image, ImageEnhance, ImageFilter

def im2string(name):

    #file_name='LITE_peg.jpeg'
    file_name='2' + name
    text = tesseract.image_to_string(file_name, True, ' -psm 7 digits')
    #im = Image.open(file_name)

    #text = pytesseract.image_to_string(im,config='outputbase digits')
    print(text)
    return text;


