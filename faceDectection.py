import cv2

class face_detection():
    def __init__(self, img, classifier): 
        self.__img = cv2.imread(im=-)
        self.__face = None
        self.__classifer =  classifier

    def detectFace(self):
        img = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        return img

    def show_img
