'''
作者:耿立帅
'''
from All_Class import *
from conf.constant import *


def read_data(file_name, flag):
	with open(file_name, 'r') as f:
		if flag == 1:
			Feature_action = f.readline().strip('\n').split(',')
		elif flag == 2:
			Feature_customer = f.readline().strip('\n').split(',')
		elif flag == 3:
			Feature_product = f.readline().strip('\n').split(',')
		else:
			F
		line = f.readline()
		while line:

			line = f.readline().strip('\n')
