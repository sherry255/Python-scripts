#!/usr/bin/env python
# coding:utf-8
'''
The script is aims for format the .srt files.
'''
__author__ = 'sherry'
__date__ = '27 Aug 2016'

from os import listdir
from os.path import isfile, join
import pysrt
import glob
import re

_filespath = "/Users/sherry/Downloads/Lesson1Subtitles/*"


def _generate_new_file(files):
    for f in files:
        write_file = f.replace('.srt', '.txt')
        with open(f, 'r') as file:
            str = ''
            for line in file:
                if line[0] >= 'A':
                    str += line + ' '
            str.replace('\n','')
            str.replace('  ',' ')
            with open(write_file, 'w') as write_file:
                write_file.write(str)


def file_lists():
    files = glob.glob(_filespath)
    return _generate_new_file(files)


if __name__ == '__main__':
    file_lists()
