FaceDetector command line options:

* Running Pre-setup trainning steps

-This steps download and validate image urls specified in config files setting in directories <Directory_url_image> and have specific
config file for managed this image. It contains the followings item:

- path_to_image_downloader_script = /home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/pre-trainning-setup/image_downloader/image_downloader.py
- path_to_image_url_directory = /home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/pre-trainning-setup/image_downloader/config
- path_to_not_valid_image = /home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/pre-trainning-setup/validation_image_script_test/image_not_valid_list.txt
- path_to_positive_image_directory = /home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/tests/positive_image
- path_to_negative_image_directory = /home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/trainning/negative_images
- path_to_image_validator_script = /home/ricardo/Desktop/CODIGO/ComputerVision/face_detector/pre-trainning-setup/validation_image_script_test/image_validator_script.py

-Image urls:
All image used for trainnign propourses are specified in this directory:
 * /face_detector/pre-trainning-setup/image_downloader/config
Each .cfg file contains optios to downlaod specific files .txt from the directory 
python face_detector_manager.py -s ./config/haar_detector/haar_trainning.cfg

