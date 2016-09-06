from detector_package_manager import DetectorConfig

class DetectorManager(object):
    def __init__(self, config_file):
        config = DetectorConfig(config_file)
        self.__detector_list = config.get_detectors_list()
        self.__config_return_data()

    def __config_return_data(self):
        for detector  in self.__detector_list:
            self.__return_data[detector.feature]=""

    def process_data(self, raw_image):
        self.__return_data = {}
        for detector  in self.__detector_list:
            self.__return_data[detector.feature] = str(detector.process_data(raw_image))
            
        return  self.__return_data



