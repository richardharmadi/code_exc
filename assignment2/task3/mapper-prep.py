#!/usr/bin/python

import sys
postId=0
postType=0
userId=0

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    line = line.replace('<row','').replace('/>','') # remove the XML row identifier
    tokens = line.split(' ')
    for token in tokens:
	if (token.find('PostTypeId')>-1) and (token.find('"')>-1): # find the PostTypeId column
		postType=token.split('"')[1]
	elif (token.find('OwnerUserId')>-1) and (token.find('"')>-1): # find the OwnerUserId column
		userId=token.split('"')[1]
	elif (token.find('ParentId')>-1) and (token.find('"')>-1): # find the parentID
		questionId=token.split('"')[1]
    if(postType=='2'): # if PostTypeId = 2 , or in other words it's an answer
    	print("{0};{1};{2}".format(userId,questionId,1))
