import urllib2
import imghdr
from urllib2 import Request
from urllib2 import urlopen, HTTPError
import os
import numpy as np
import cv2

class ImageDownloader(object):
	FULL_RANGE_IMAGE_COUNT = -1

	def __init__(self, image_prefix, urls_image, total_image_amount_to_download, negative_image_size = 100, positive_image_size = 50):
		self.__image_prefix = image_prefix
		self.__load_image_urls_from_file(urls_image)
		self.__crop_image_url(total_image_amount_to_download)
		self.__create_image_trainning_config_dic(int(positive_image_size), int(negative_image_size))


	def __create_image_trainning_config_dic(self, positive_image_size, negative_image_size):
		self.__IMAGE_TRAINNING_TYPE= { "positive" : (positive_image_size, self.__resize_positive_image),
										"negative" : (negative_image_size, self.__resize_negative_image),
									}

	def __load_image_urls_from_file(self, file_name):
		if file_name:
			data = self.__load_data_from_file(file_name)
			self.__data_list = data.split('\n')


	def __load_data_from_file(self, file_name):
		data = ""
		with open(file_name, 'r') as image_file:
			 data = image_file.read()
		return data

	def __verify_load_operation(self):
		if len(self.__data_list) == 0:
			raise Exception('Empty Image url File')

	def __crop_image_url(self, image_count):
		if image_count != -1:
			self.__data_list = self.__data_list[0:int(image_count)]

	def __verify_download_directory(self, directory):
		if not os.path.exists(directory):
			os.makedirs(directory)

	def __resize_positive_image(self, raw_image, filename):
		self.__resize_image(filename, raw_image, self.__IMAGE_TRAINNING_TYPE["positive"][0])

	def __resize_negative_image(self, raw_image, filename):
		self.__resize_image(filename, raw_image, self.__IMAGE_TRAINNING_TYPE["negative"][0])

	def __if_image_valid(self, filename):
		return self.__image_type in imghdr.what(filename)

	def __process_downloaded_image(self, filename):
		image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
		resized_image = cv2.resize(image, (image_size, image_size))
		cv2.imwrite(filename,resized_image)

	def __resize_image(self, filename, raw_image, image_size):
		if len(raw_image)>0:
			with open(filename, 'wb') as file:
				file.write(raw_image)
			if self.__if_image_valid(filename):
				self.__process_downloaded_image(filename)



	def download_files(self, directory_to_download, image_format_ext, image_trainning_type):
		self.__image_type = image_format_ext
		self.__verify_download_directory(directory_to_download)
		file_name_idx = 1
		for image_url in self.__data_list:
			try:
				image_uri = directory_to_download+'/'+self.__image_prefix+str(file_name_idx)+image_format_ext
				file_name_idx += 1
				print "downloading file to : {0}".format(image_uri)
				raw_image = urllib2.urlopen(image_url).read()
				self.__IMAGE_TRAINNING_TYPE[image_trainning_type][1](raw_image,image_uri)
			except Exception as e:
				print ("Error Processing image: {0}".format(str(e)))


