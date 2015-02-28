#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
#Mathmatic Solutions
days = [31,28,31,30,31,30,31,31,30,31,30,31]

tally=0
day=2 # Jan 1st 1901 was a Tuesday
for yr in range(1,101):
	for month in range(0,12):
		day += days[month]
		if month==1 and yr%4==0:
			day += 1
		if day%7==0:
			tally+=1
			print day,month,yr + 1900
print tally
#Module solutions 
import datetime
matrix  = []
for y in range(1901, 2001):
    for m in range(1, 13):
        #define datetime.time class
        d = datetime.date(y, m, 1)
        #mon~sun -> 0~6
        if d.weekday() == 6:
        	matrix.append([y,m,1])   
print len(matrix)
print matrix