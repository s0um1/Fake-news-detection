import numpy as nm
import pytesseract
import cv2


def imToString(path=r"D:\Everything CS\Hackathons\Trithon\Fake_News_Detection\\img.jpeg"):

    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    capture = cv2.imread(path)

    # Converted the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    tesstr = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(capture), cv2.COLOR_BGR2GRAY),
        lang='eng')
    print(tesstr)
    return tesstr
