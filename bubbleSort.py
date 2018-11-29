#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author: sober
# time: 2018/11/29
# soberwone@gmail.com

import sys,os

def bubbleSort(arr):
	count = len(arr)
	for j in range(count-1,0,-1):
		for i in range(j):
			if arr[i] > arr[i + 1]:
				arr[i],arr[i + 1] = arr[i + 1],arr[i]

if __name__ == "__main__":
	arr = [1,3,2,55,33,4,3]
	bubbleSort(arr)
	print(arr)