import sys
import dlib
from skimage import io
import cv2

class DlibDetector(object):
    def __init__(self):
        self.__detector = dlib.get_frontal_face_detector()
        self.__faces = None

    def detect(self, raw_image):
         img = raw_image
         self.__faces = None
         self.__faces = self.__detector(img, 1)

    def face_count(self):
        return len(self.__faces)

    def get_faces_roi_list(self):
        return self.__faces



if __name__ == '__main__':
    detector = DlibDetector()
    image = cv2.imread(sys.argv[1])
    detector.detect(image)
    print "Cantidad de Caras: {0}".format(str(detector.face_count()))
