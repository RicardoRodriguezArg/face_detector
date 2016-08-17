#!/usr/local/bin/python
import sys
import os
from optparse import OptionParser
import subprocess
from detectors.haar_face_detector.detector_haar import FaceDetector

SCRIPT_VERSION = '1.0.0'
#HARDCODED SECTION
PATH_TO_PRE_TRAINNIGN_STEP_SCRIPT = 'pre-trainning-setup/image_downloader/gral_image_downloader.py'
PATH_TO_TRAINNING_SCRIPT = 'trainning/haar_trainning/train_manager.py'
PAT_TO_FACE_DETECTOR_SERVICE = 'service/detector_service.py'
PYTHON_PREFIX = 'python'
#END HARDCODE SECTION
def _execute_cmd_shell(cmd_to_execute):
    p = subprocess.Popen(cmd_to_execute, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()

def __create_parser():
    parser = OptionParser(usage = 'usage: %prog [options] filename',\
                          version = '%prog '+ SCRIPT_VERSION )
    parser.add_option('-t','--train_haar',\
                      action = "store",\
                      type = "string" ,\
                      dest = "train_haar_file_cfg_file",\
                      default = False,\
                     help = "Train Haar Detector using config file especified")

    parser.add_option('-r','--run_detector_haar',\
                      action = "store",\
                      type = "string" ,\
                      dest = "run_haar_detector_service",\
                      default = False,\
                     help = "Run detector Haar")

    parser.add_option('-p','--run_perf_test_haar',\
                      action = "store",\
                      type = "string" ,\
                      dest = "performance_test_cfg_file",\
                      default = False,\
                     help = "Run Performance test on Haar Detector")

    parser.add_option('-s','--run_pre_trainning_setup',\
                      action = "store",\
                      type = "string" ,\
                      dest = "run_pre_trainning_setup_cfg_file",\
                      default = False,\
                     help = "Run Pre setup steps for Detector Haar Trainning")

    return parser


def __process_option_project(options):
    if options.train_haar_file_cfg_file:
        __run_train_haar_classifier(options.train_haar_file_cfg_file)
    elif options.run_haar_detector_service:
        __run_clasiffier_haar_service(options.run_haar_detector_service)
    elif options.performance_test_cfg_file:
        __run_performance_test_on_haar(options.performance_test_cfg_file)
    elif options.run_pre_trainning_setup_cfg_file:
        __run_pre_trainning_steps(options.run_pre_trainning_setup_cfg_file)

def __run_train_haar_classifier(cfg_file):
    _execute_cmd_shell(PYTHON_PREFIX+ ' '+PATH_TO_TRAINNING_SCRIPT+ ' ' + cfg_file)

def __run_clasiffier_haar_service(cfg_file):
    _execute_cmd_shell(PYTHON_PREFIX + ' ' + PAT_TO_FACE_DETECTOR_SERVICE + ' ' + cfg_file)

def __run_performance_test_on_haar(cfg_file):
    pass

def __run_pre_trainning_steps(cfg_file):
    _execute_cmd_shell(PYTHON_PREFIX+ ' '+PATH_TO_PRE_TRAINNIGN_STEP_SCRIPT+ ' ' + cfg_file)


if __name__ == '__main__':
    (options, args ) =  __create_parser().parse_args()
    __process_option_project(options)
    
