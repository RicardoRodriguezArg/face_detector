import os, sys

class HaarSetupTools(object):
	NEGATIVE_FILE_NAME_STRING = 'bg.txt'
	POSITIVE_FILE_NAME_STRING = 'info.lst'
	EMPTY_STRING =""
	POSITIVE_HAAR_SETUP_STRING = ' 1 0 0 50 50'
	def __init__(self, negative_directory, positive_directory):
		self.__negative_directory=negative_directory
		self.__positive_directory=positive_directory

	def create_setup_for_haar_samples(self ,work_directory, haar_setup_filename ,string_to_attach):
		string_to_store = ""
		file_count = 0
		with open(haar_setup_filename,'a') as file_to_store:
			for file_name in os.listdir(work_directory):
				string_to_store = work_directory + '/' + file_name + string_to_attach +'\n'
				file_to_store.write(string_to_store)
				file_count += 1
		print"Total Files: {0} in filename : {1} ".format(str(file_count), haar_setup_filename)

def _execute(negative_directory, positive_directory):
	setup_tools = HaarSetupTools(negative_directory, positive_directory)
	setup_tools.create_setup_for_haar_samples(negative_directory,HaarSetupTools.NEGATIVE_FILE_NAME_STRING,HaarSetupTools.EMPTY_STRING)
	setup_tools.create_setup_for_haar_samples(positive_directory,HaarSetupTools.POSITIVE_FILE_NAME_STRING,HaarSetupTools.POSITIVE_HAAR_SETUP_STRING)

if __name__ == '__main__':
	_execute(sys.argv[1], sys.argv[2])