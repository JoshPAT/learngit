#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.

"""
#when 200 dict[0] = -3 to conteract “and = 3”
letter1to19 = [-3,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,10,8,7]
letterdecimal = [6,6,5,5,5,7,6,6] 
sumletter = 0
dict ={}
#define the number from 1 -19
dict[0] = -3
for i in range(1,20):
	dict[i] = letter1to19[i]
#define the number 20,30,40,50,60,70,80,90
j = 0
for i in range(20,100,10):
	dict[i] = letterdecimal[j]
	j +=1

print dict
print sumletter

i = 20
# define all
while i <1000:
	
	if dict.has_key(i) == False:
		if len(str(i)) == 2:
			dict[i] = dict[int(str(i)[0])*10] + dict[int(str(i)[1])]
		if len(str(i)) == 3:
			dict[i] = dict[int(str(i)[0])] + 7 + 3 + dict[int(str(i)[1:])] 
	i = i + 1

print sum(dict[i] for i in range(1,1000)) + 3 + 8 

print dict

print sumletter + 3 + 8


num = ['','one','two','three','four','five','six','seven','eigth','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
for d in ('twenty','thirty','forty','fifty', 'sixty', 'seventy', 'eighty','ninety'):
    for n in num[:10]:
        num.append(d+n)
for c in num[1:10]:
    num.append(c+'hundred')
    for n in num[1:100]:
        num.append(c+'hundredand'+n)
num.append('onethousand')
print num
print(sum([len(w) for w in num]))
