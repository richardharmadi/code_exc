#!/usr/bin/python

import sys
postId=0
postType=0
viewCount=0

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    line = line.replace('<row','').replace('/>','') # remove the XML row identifier
    #line = re.sub('(<row|\/>)','',line) # can also be implemented using regex
    tokens = line.split(' ')
    for token in tokens:
	if (token.find('Id',0,2)>-1) and (token.find('"')>-1):# find the Id column, by searching 'id' in the first index of the word, and have " in the whole word
		postId=token.split('"')[1] # save the value
	elif (token.find('PostTypeId')>-1) and (token.find('"')>-1): # find the PostTypeId column
		postType=token.split('"')[1]
	elif (token.find('ViewCount')>-1) and (token.find('"')>-1) : # find the ViewCount column
		viewCount=token.split('"')[1]
    if(postType=='1'): # if PostTypeId = 1 , or in other words it's a question
    	print("{0};{1}".format(viewCount,postId))
