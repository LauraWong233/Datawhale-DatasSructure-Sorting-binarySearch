#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:47:14 2019

@author: laura
"""

def binarySearch(list,val):
	length = len(list)
	left = 0
	right = length-1
	while left<=right:
		temp = (left+right)//2
		if list[temp]==val:
			print(temp)
			return temp
		elif list[temp] > val:
			right = temp-1
		else:
			left = temp+1
	return -1



if __name__=='__main__':
	binarySearch([1,2,4,5,6,7,9,10,100],5)
    
