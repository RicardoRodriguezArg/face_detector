import sys
import numpy as np
import cv2


class FaceDetector(object):
    __IMAGE_SCALE_FACTOR = 1.3
    __IMAGE_MIN_NEIGHBORS = 5

    def __init__(self, xml_file_trainning_detector):
        self.__face_classifier = cv2.CascadeClassifier(xml_file_trainning_detector)
        self.__faces = None
    def __create_action_handler(self):
        self.__ACTION_HANDLER = { 'face_count',self.get_face_count}
    
    def get_face_count(self):
        return len(self.__faces)

    def face_detection_data(self, raw_image):
        self.__faces = None
        grey_image = self.__preprocess_image(raw_image)
        self.__faces =  self.__face_classifier.detectMultiScale(grey_image, self.__IMAGE_SCALE_FACTOR , self.__IMAGE_MIN_NEIGHBORS, minSize=(50, 50))

    def __preprocess_image(self, raw_image):
        gray_scale_image = cv2.cvtColor(raw_image , cv2.COLOR_BGR2GRAY)
        return gray_scale_image

    def __verify_image_size(self):
        pass

    def execute_action(self, action_to_execute):
        return self.__ACTION_HANDLER[action_to_execute]()

if __name__ == '__main__':
    face_detector = FaceDetector(sys.argv[1])
    face_detector.face_detection_data(cv2.imread(sys.argv[2]))
    print "cantidad de caras: {0}".format(face_detector.get_face_count())