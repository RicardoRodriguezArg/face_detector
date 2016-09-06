import numpy as np
import cv2
import caffe
import sys

class GenderDetector(object):
    __NET_FILE_NAME = 'net_filename'
    __TRAINNED_WEIGTH_FILE_NAME = 'trainned_weigth_file_name'
    __TRANSFORMER_MEAN_FILE_NAME = 'transformer_mean_file_name'
    __TRANSFORMER_INPUT_BLOB_NAME = 'transformer_input_blob_name'
    __TRANSFORMER_INPUT_MEAN_IMAGE_FILE_NAME = 'transformer_input_image_mean_filename'
    __TRANSFORMER_TRANSPOSE_TUPLE = 'transformer_transpose_tuple'
    __TRANSFORMER_CHANNEL_SWAP_TUPLE = 'transformer_channel_swap_tuple'
    __TRANSFORMER_RAW_SCALE = 'transformer_raw_scale'
    __IMAGE_RESIZE_WIDTH = 'image_resize_width'
    __IMAGE_RESIZE_HEIGTH = 'image_resize_heigth'
    __IMAGE_BACTH_SIZE = 'image_batch_size'

    def __init__(self, config_diccionary_options):
        caffe.set_mode_cpu()
        if config_diccionary_options:
            self.__net =caffe.Load(config_diccionary_options[self.__NET_FILE_NAME]\
                                , config_diccionary_options[self.__TRAINNED_WEIGTH_FILE_NAME], caffe.TEST)
            self.__load_transformer_settings(config_diccionary_options)


    def __load_transformer_settings(self, config_dictionary_options):
        input_blob_name = config_dictionary_options[self.__TRANSFORMER_INPUT_BLOB_NAME]
        input_mean_image_file_name = config_dictionary_options[self.__TRANSFORMER_INPUT_MEAN_IMAGE_FILE_NAME]
        transpose_tuple = config_dictionary_options[self.__TRANSFORMER_TRANSPOSE_TUPLE]
        channel_swap_tuple = config_dictionary_options[self.__TRANSFORMER_TRANSPOSE_TUPLE]
        raw_scale = config_dictionary_options[self.__TRANSFORMER_RAW_SCALE]
        self.__transformer = caffe.io.Transformer({input_blob_name: net.blobs[input_blob_name].data.shape})
        self.__transformer.set_mean(input_blob_name, np.load(input_mean_image_file_name).mean(1).mean(1))
        self.__transformer.set_transpose(input_blob_name, transpose_tuple)
        self.__transformer.set_channel_swap(input_blob_name, channel_swap_tuple)
        self.__transformer.set_raw_scale(input_blob_name, raw_scale)

    def __reshape_input_blob(self, config_dictionary_options):
        image_width = int(config_dictionary_options[self.__IMAGE_RESIZE_WIDTH])
        image_heigth = int(config_dictionary_options[self.__IMAGE_RESIZE_HEIGTH])
        image_batch_size = int(config_dictionary_options[self.__IMAGE_BACTH_SIZE])

        input_blob_name = config_dictionary_options[self.__TRANSFORMER_INPUT_BLOB_NAME]
        self.__net.blobs[input_blob_name].reshape(image_batch_size,3,image_width,image_heigth)


    def classify_image(self, image_file_name):
        im = caffe.io.load_image(image_file_name)
        image = cv2.imread(image_file_name)
        net.blobs['data'].data[...] = image
        out = net.forward()
        return out['prob'].argmax()



if __name__ == '__main__':

	gender_detector = GenderDetector(None)

