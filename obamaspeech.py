from __future__ import division

import math
import os

from collections import defaultdict

PATH_TO_DATA = "/Users/alexlassalle/Desktop/obama"

def read():
	words={}
	text_file=open("input.txt","r")
	text_file_array=text_file.read().split(', . \n - -- ')

	print text_file_array[0]
	print text_file_array[1]

if __name__=='__main__':
	read()
