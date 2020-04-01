import pickle
import numpy as nm
import pytesseract
import cv2

#doc_new = ['obama is running for president in 2016']
while(True):
    
    ch=int(input("\nPress 1 to for text verfication\nPress 2 for text verification from image\n"))
    if (ch == 1):
        var = input("Please enter the news text you want to verify:\n")
        print("\nYou entered: " + str(var))
    else:
        path=r"C:\Users\HP\Desktop\FakeNewsDetection\image.png"
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\AppData\Local\Tesseract-OCR\tesseract'
        capture = cv2.imread(path)
        var = pytesseract.image_to_string(cv2.cvtColor(nm.array(capture), cv2.COLOR_BGR2GRAY),lang='eng')
        print(var)
        
    #function to run for prediction
    def detecting_fake_news(var):    
    #retrieving the best model for prediction call
        load_model = pickle.load(open('final_model.sav', 'rb'))
        prediction = load_model.predict([var])
        prob = load_model.predict_proba([var])

        return (print("The given statement is ",prediction[0]),
            print("The truth probability score is ",prob[0][1]))


    if __name__ == '__main__':
        detecting_fake_news(var)
