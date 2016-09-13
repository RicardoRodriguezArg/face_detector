import cv2

class ImageManipulation(object):
    def __init__(self):
        pass

    @staticmethod
    def histogram_esqualization(img, img_width, img_height):
        #Histogram Equalization
        img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
        img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
        img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])
        return img

    @staticmethod
    def rezize_image(img_width, img_height):
        #Image Resizing
        return cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_CUBIC)