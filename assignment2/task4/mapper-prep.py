#!/usr/bin/python

import sys
postId=0
postType=0
userId=0
answerId=0

for line in sys.stdin:                  # input from standard input
    line = line.strip('\n')                 # remove whitespaces
    line = line.replace('<row','').replace('/>','') # remove the XML row identifier
    tokens = line.split(' ')
    for token in tokens:
	if (token.find('PostTypeId')>-1) and (token.find('"')>-1): # find the PostTypeId column
		postType=token.split('"')[1]
	elif (token.find('OwnerUserId')>-1) and (token.find('"')>-1): # find the OwnerUserId column
		userId=token.split('"')[1]
	elif (token.find('AcceptedAnswerId')>-1) and (token.find('"')>-1): # find the parentID
		answerId=token.split('"')[1]
	elif (token.find('Id',0,2)>-1) and (token.find('"')>-1): # find the row ID column
		postId=token.split('"')[1]	
    if(postType=='1'): # if PostTypeId = 1 , or in other words it's a question
    	print("{0};{1}".format(answerId,postType)) # output its accepted answer id and its post type id just to make sure
    elif(postType=='2'): # if PostTypeId = 2, or if it's an answer
	print("{0};{1};{2}".format(postId,postType,userId)) # output its row id (answer id) and its post type (to make sure, plus its user id 
    postId=0
    postType=0
    userId=0
    answerId=0
