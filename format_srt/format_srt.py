#!/usr/bin/env python
# coding:utf-8
'''
The script is aims for formatting the srt files.
'''
__author__ = 'sherry'
__date__ = '27 Aug 2016'

# from os import listdir
# from os.path import isfile, join
# import pysrt
# import re
import glob

# 预定义文件夹地址
_filespath = "/Users/sherry/Downloads/Lesson1Subtitles/*"


def _generate_new_file(files):
    for f in files:
        # 对每一个rst文件,都新建一个与之对应的txt文件
        write_file = f.replace('.srt', '.txt')
        with open(f, 'r') as file:
            # 新建一个数组,用来存取每行的字符串
            str_list = []
            for line in file:
                # 每行只有字幕部分的开头字母 >= 'A'
                if line[0] >= 'A':
                    # remap = {
                    #     ord('\n'):'',
                    #     ord('\t'):' '
                    # }
                    # line = line.translate(remap)
                    # 替换掉换行符
                    line = line.strip().replace('\n', ' ')
                    # 将每行字符串存入数组
                    str_list.append(line)
            # 将数组中的字符串串起来
            str = ' '.join(str_list)
            with open(write_file, 'w') as write_file:
                write_file.write(str)


def file_lists():
    # 读取文件夹中的所有文件, 存入files 列表中
    files = glob.glob(_filespath)
    return _generate_new_file(files)


if __name__ == '__main__':
    file_lists()
    # with open('/Users/sherry/Downloads/Lesson1Subtitles/01 - Welcome.txt', 'r') as write_file:
    #     print write_file
