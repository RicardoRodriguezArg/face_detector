
'''
opencv_createsamples -info info.lst -num 2000 -w 30 -h 30 -vec positives.vec
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 15 -w 30 -h 30 &
'''
import sys
import subprocess

class HaarTrainning(object):
    __OPENCV_CMD_TO_TRAIN = 'opencv_createsamples'
    __OPENCV_TO_TRAIN_HAAR = 'opencv_traincascade'
    __PRE_TRAINNING_SCRIPT = 'python trainning_setup.py'

    def __create_cmd_line_option_dict(self):
        self.__CMD_OPTIONS = { '-info' : '',\
                      '-num' : '',\
                      '-w' : '',\
                      '-h' : '',\
                      '-vec' : '',\
                      '-data':'',\
                      '-bg':'',\
                      '-numPos':'',\
                      '-numNeg':'',\
                      '-numStages':'',\
                      'path_to_positive_image_directory' : '',\
                      'path_to_negative_image_directory' : ''
                    }


    def __init__(self, cfg_file):
        self.__CMD_TO_EXECUTE = ""
        self.__create_cmd_line_option_dict()
        self.__data_list = []
        self.__load_data_from_cfg_file(cfg_file)

    def __execute_cmd_shell(self, cmd_to_execute):
        p = subprocess.Popen(cmd_to_execute, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line,
        retval = p.wait()

    def train_haar_detector(self):
        self.__create_pretrainning_script_step()
        print "Cmd to execute: {0}".format(self.__CMD_TO_EXECUTE)
        self.__execute_cmd_shell('pwd; clear')
        self.__execute_cmd_shell(self.__CMD_TO_EXECUTE)
        self.__create_vect_cmd_from_options()
        print "Cmd to execute: {0}".format(self.__CMD_TO_EXECUTE)
        self.__execute_cmd_shell(self.__CMD_TO_EXECUTE)
        self.__create_trainning_cmd_from_options()
        print "Cmd to execute: {0}".format(self.__CMD_TO_EXECUTE)
        #self.__execute_cmd_shell(self.__CMD_TO_EXECUTE)
        
    def __process_line(self, string_to_compare, line):
        processed = False
        if string_to_compare == line.split('=')[0].strip():
            self.__CMD_OPTIONS[line.split('=')[0].strip()] = line.split('=')[1].strip()
            processed = True
        return processed

    def __load_data_from_cfg_file(self, cfg_file):
        with open(cfg_file, 'r') as cfg_file:
            data= cfg_file.read()
        self.__data_list = data.split('\n')
        for line in self.__data_list:
            for key, values in self.__CMD_OPTIONS.iteritems():
                if self.__process_line(key, line):
                    break
    def __create_vect_cmd_from_options(self):
        self.__CMD_TO_EXECUTE = self.__OPENCV_CMD_TO_TRAIN +' -info '+self.__CMD_OPTIONS['-info'] \
                                + ' -num ' + self.__CMD_OPTIONS['-num']\
                                + ' -w ' + self.__CMD_OPTIONS['-w']\
                                + ' -h ' + self.__CMD_OPTIONS['-h']\
                                + ' -vec ' + self.__CMD_OPTIONS['-vec']

    def __create_trainning_cmd_from_options(self):
        self.__CMD_TO_EXECUTE = self.__OPENCV_TO_TRAIN_HAAR + ' -data ' + self.__CMD_OPTIONS['-data']\
                                + ' -vec '+ self.__CMD_OPTIONS['-vec']\
                                + ' -bg '+ self.__CMD_OPTIONS['-bg']\
                                + ' -numPos '+ self.__CMD_OPTIONS['-numPos']\
                                + ' -numNeg '+ self.__CMD_OPTIONS['-numNeg']\
                                + ' -numStages '+ self.__CMD_OPTIONS['-numStages']\
                                + ' -w '+ self.__CMD_OPTIONS['-w']\
                                + ' -h '+ self.__CMD_OPTIONS['-h'] + ' &'


    def __create_pretrainning_script_step(self):
        self.__CMD_TO_EXECUTE = self.__PRE_TRAINNING_SCRIPT + ' '+ self.__CMD_OPTIONS['path_to_negative_image_directory'] \
                                + ' ' + self.__CMD_OPTIONS['path_to_positive_image_directory']

if __name__ == '__main__':
    haar_trainning = HaarTrainning(sys.argv[1])
    haar_trainning.train_haar_detector()

