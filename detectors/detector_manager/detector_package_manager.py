from hog_detector import HOGDetector
from haar_face_detector import HaarDetector
from caffe_gender_detector import GenderDetector
class DetectorConfig(object):
    __COMMENT_TOKEN = "#"
    __DETECTOR_LIST_TOKEN = "[detector_list]"
    __DETECTOR_CONF_TOKEN = "[conf]"

    def __init__(self, config_file):
        self.__detector_list = []
        self.__parse_file(config_file)
        self.__detector_list_name =[]
        self.__detector_config_file_list = {}

    def __parse_file(self, config_file):
        with open(config_file, 'r') as input_file:
            data = input_file.readLines()
        data = data.split('\n')
        data = self.__remove_comment_lines(data)
        self.__get_detector_list(data)
        self.__get_config_files_for_detectors(data)
        self.__create_detector_from_config()



    def __remove_comment_lines(self, data):
        for line in data:
            if line.strip()[0] == self.__COMMENT_TOKEN:
                data.remove(line)
        return data

    def __get_detector_list(self, data):
        is_detector_list = False
        for item in data:
            if item.strip() == self.__DETECTOR_LIST_TOKEN:
                is_detector_list = True
            elif is_detector_list:
                self.__detector_list_name.append(item)
            elif is_detector_list == self.__DETECTOR_CONF_TOKEN:
                is_detector_list = False

    def __get_config_files_for_detectors(self, data):
        is_detector_config_token = False
        for item in data:
            if item.strip() == self.__DETECTOR_LIST_TOKEN:
                is_detector_config_token = True
            elif is_detector_list:
                self.__detector_config_file_list[item.strip().split("=")[0].strip()] = item.strip().split("=")[1].strip()
            elif is_detector_list == self.__DETECTOR_CONF_TOKEN:
                is_detector_config_token = False

    def __pre_check(self):
        if len(self.self.__detector_list_name) == 0:
            raise Exception("No Detector Process were found in config files!")
        if len(self.self.__detector_config_file_list) == 0:
            raise Exception("No Configuration file for Detector Process were found in config files!")
        if len(self.self.__detector_list_name) == len(self.self.__detector_config_file_list):
            raise Exception("Detector Process and config files have to come in pairs!")


    def __create_detector_from_config(self):
        self.__pre_check()
        for items in self.__detector_list_name:
            config_file = self.__detector_config_file_list[items.strip().split("=")[0]]
            if items.strip().split("=")[1] == "HOG":
                self.__detector_list(HOGDetector(config_file))
            if items.strip().split("=")[1] == "CAFFE_GENDER":
                self.__detector_list(HOGDetector(config_file))
            if items.strip().split("=")[1] == "HAAR":
                self.__detector_list(HaarDetector(config_file))




