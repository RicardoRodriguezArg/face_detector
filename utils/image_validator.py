import numpy as np
import cv2
import time
import sys
import os

class ImageValidator(object):
	__VALID_THRESHOLD_VALUE = 500
	def __init__(self, histogram_list = []):
		self.__histogram_list =  histogram_list
		self.__histogram_result = {}


	def load_file_list_from_file(self, image_list_file_name):
		self.__file_name_list = []
		with open(image_list_file_name, 'r') as raw_file_list:
			data = raw_file_list.read()
		self.__file_name_list = data.split('\n')
		self.__depure_input_image_list()

	def __depure_input_image_list(self):
		for item in self.__file_name_list:
			if len(item)==0:
				self.__file_name_list.remove(item)


	def create_histogram_from_file_names_list(self):
		for file_name in self.__file_name_list:
			histogram = None
			histogram = self.__get_image_histogram(file_name)
			if histogram is not None:
				self.__histogram_list.append(histogram)


	def verify_directory_image_vality(self, image_directory):
		#TODO: agregar opcion de acciones que se pueden realizar
		not_valid_image_count=0
		total_amount_of_files_in_directory = len(os.listdir(image_directory))
		for image_file_name in os.listdir(image_directory):
			if not self.verify_image_validation(image_directory+'/'+image_file_name):
				print "{0}\t--->imagen No valida".format(image_file_name)
				print "eliminando archivo: {0}".format(image_file_name)
				os.remove(image_directory+'/'+image_file_name)
				not_valid_image_count += 1
		print "cantidad de imagenes no Validas: {0}".format(not_valid_image_count)
		print "cantidad total de imagenes en el directorio {0}".format(total_amount_of_files_in_directory)

	def verify_image_validation(self, image_to_validate):
		image_histogram = self.__get_image_histogram(image_to_validate)
		return self.__is_valida_image(image_histogram)

	def __is_valida_image(self, image_histogram):
		result = True
		for histogram in self.__histogram_list:
			d = cv2.compareHist(image_histogram, histogram, 1)
			print "Thresold value: {0}".format(d)
			if d < self.__VALID_THRESHOLD_VALUE:
				result = False
				break
		return result

	def __get_image_histogram(self, image_file_name):
		img = self.__load_image_from_filename(image_file_name)
		histogram = cv2.calcHist([img],[0],None,[256],[0,256])
		cv2.normalize(histogram,histogram,0,255,cv2.NORM_MINMAX)
		return histogram


	def __load_image_from_filename(self, file_name):
		return cv2.imread(file_name)

