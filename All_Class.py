'''
作者:耿立帅
'''
from conf.constant import *


class action(object):
	def __init__(self, s):
		str_list = s.split(',')
		for k, f in enumerate(Feature_action):
			self.f = str_list[k]


class customer(object):
	def __init__(self, s):
		str_list = s.split(',')
		for k, f in enumerate(Feature_customer):
			self.f = str_list[k]


class comment(object):
	def __init__(self, s):
		str_list = s.split(',')
		for k, f in enumerate(Feature_comment):
			self.f = str_list[k]


class product(object):
	def __init__(self, s):
		str_list = s.split(',')
		for k, f in enumerate(Feature_product):
			self.f = str_list[k]