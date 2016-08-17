import sys, getopt
sys.path.insert(0,'../../../face_detector')
sys.path.insert(0,'../../face_detector')
sys.path.insert(0,'../face_detector')
from utils.image_database_downloader import ImageDownloader

def _execute_download(image_prefix, imager_url, total_image_count , directory, image_format, trainning_type, negative_scale, positive_scale):
	downloader = ImageDownloader(image_prefix,imager_url, total_image_count, int(negative_scale), int(positive_scale))
	downloader.download_files(directory, image_format, trainning_type)

def __parse_config_file_and_execute(config_file_path):
	config_data = ""
	with open(config_file_path, 'r') as image_file:
		config_data = image_file.read()
	config_data = config_data.split('\n')
	diccionary_option = []
	for item in config_data:
		item = item.strip()
		if len(item)>1:
			value = item.split('=')
			diccionary_option.append(value[1].strip())
	_execute_download(*diccionary_option)

#if __name__ == '__main__':
#	_execute_download(sys.argv[1],sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])


if __name__ == '__main__':
	__parse_config_file_and_execute(sys.argv[1])
