import sys, getopt
sys.path.insert(0,'../../../face_detector')
sys.path.insert(0,'../../face_detector')
sys.path.insert(0,'../face_detector')
from utils.image_validator import ImageValidator

def _execute(image_lists,directory_to_image):
	image_validator = ImageValidator()
	image_validator.load_file_list_from_file(image_lists)
	image_validator.create_histogram_from_file_names_list()
	#image_validator.verify_image_validation(directory_to_image)
	image_validator.verify_directory_image_vality(directory_to_image)


if __name__ == '__main__':
	_execute(sys.argv[1], sys.argv[2])
