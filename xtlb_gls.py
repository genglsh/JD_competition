# -*- coding:utf-8 -*-
"""
@version: Python 3.5.2
@author: 耿立帅
@license: 广州探迹科技有限公司版权所有
@contact: genglishuai@tungee.com
@software: PyCharm
@file: xtlb_gls.py
@time: 2017/4/26 16:41
"""
import csv


def xtlb(file_name):
    csvfile = open(file_name, 'r')
    line = csvfile.readline()
    while line:
        line_list = line.strip('\n').split(',')
        if line_list[5] == '8':
            action_file.write(line)
        line = csvfile.readline()


if __name__ == '__main__':
    action_file = open('action_file.csv', 'w')
    name_list = ['aaa.csv', 'bbb.csv', 'ccc.csv']
    for i in name_list:
        xtlb(i)

