from keras.models import Sequential
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense

class KerasDetector(object):
    def __init__(self, width, heigth, depth, classes, path_to_weigth):
        self.__model= Sequential()