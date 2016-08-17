import sys,os
import subprocess
import time

def _execute_cmd_shell(cmd_to_execute):
    p = subprocess.Popen(cmd_to_execute, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()

def _execute():
    download_1_string='python image_downloader.py ./config/downloader.cfg'
    download_2_string='python image_downloader.py ./config/downloader-car.cfg'
    download_3_string='python image_downloader.py ./config/downloader-flora.cfg'
    download_4_string='python image_downloader.py ./config/downloader-landscape.cfg'
    path_to_not_valid_image = '/home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/tests/validation_image_script_test/image_not_valid_list.txt'
    path_to_positive_image_directory ='/home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/tests/positive_image/'
    path_to_negative_image_directory = '/home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/trainning/negative_images/'
    path_to_validator_script = '../validation_image_script_test/image_validator_script.py'
    clean_positive_image_cmd ='python '+path_to_validator_script+' '+ path_to_not_valid_image + ' ' +path_to_positive_image_directory
    clean_negative_image_cmd = 'python '+path_to_validator_script+' '+ path_to_not_valid_image + ' ' + path_to_negative_image_directory

    _execute_cmd_shell(download_1_string)
    _execute_cmd_shell(download_2_string)
    _execute_cmd_shell(download_3_string)
    _execute_cmd_shell(download_4_string)
    #image cleaning and validation
    _execute_cmd_shell(clean_positive_image_cmd)
    _execute_cmd_shell(clean_negative_image_cmd)


def __extract_url_cfg_files_from_directory(image_url_directory_path):
    result_list = []
    for cfg_file in os.listdir(image_url_directory_path):
        if cfg_file.split('.')[1] == 'cfg':
            print "loading config file for download : {0}".format(image_url_directory_path+'/'+cfg_file)
            result_list.append(image_url_directory_path+'/'+cfg_file)
    return result_list

    
def _execute_using_cfg_file(cfg_file_):
    print "Loading data from cfg file {0}".format(cfg_file_)
    data = ""
    with open(cfg_file_,'r') as file:
        data =file.read()
    #setup initial variables
    data = data.split('\n')
    image_url_list = []
    path_to_not_valid_image = ''
    path_to_positive_image_directory = ''
    path_to_negative_image_directory = ''
    path_to_image_validator_script = ''
    path_to_image_downloader_script = ''
    python_prefix = 'python'
    print "Parsing Config File....."
    #parsing cfg options
    for line in data:
        if line.split('=')[0].strip() == 'path_to_image_url_directory':
            image_url_list = __extract_url_cfg_files_from_directory(line.split('=')[1].strip())
        elif line.split('=')[0].strip() == 'path_to_not_valid_image':
            path_to_not_valid_image = line.split('=')[1].strip()
        elif line.split('=')[0].strip() == 'path_to_positive_image_directory':
            path_to_positive_image_directory = line.split('=')[1].strip()
        elif line.split('=')[0].strip() == 'path_to_negative_image_directory':
            path_to_negative_image_directory = line.split('=')[1].strip()
        elif line.split('=')[0].strip() == 'path_to_image_validator_script':
            path_to_image_validator_script = line.split('=')[1].strip()
        elif line.split('=')[0].strip() == 'path_to_image_downloader_script':
            path_to_image_downloader_script = line.split('=')[1].strip()
    
    #download scritps executions
    print "Executing Downloading Step"
    image_downloader_script_prefix = python_prefix + ' ' + path_to_image_downloader_script
    for cfg_file in image_url_list:
        _execute_cmd_shell(image_downloader_script_prefix + ' ' +cfg_file)
        

    print "Cleannig and validating image downloaded"
    clean_positive_image_cmd ='python ' + path_to_image_validator_script + ' ' + path_to_not_valid_image + ' ' + path_to_positive_image_directory
    clean_negative_image_cmd = 'python ' + path_to_image_validator_script + ' ' + path_to_not_valid_image + ' ' +path_to_negative_image_directory
    print "cmd to execute: {0}".format(clean_positive_image_cmd)
    print "cmd to execute: {0}".format(clean_negative_image_cmd)
       
    _execute_cmd_shell(clean_positive_image_cmd)
    _execute_cmd_shell(clean_negative_image_cmd)


if __name__ == '__main__':
    #_execute()
    _execute_using_cfg_file(sys.argv[1])
