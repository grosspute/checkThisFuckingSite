def parseThisFuckingList(sFileList):
	aAlreadyChecked = []
	try:
		with open("%s.checked" % sFileList) as oFileChecked:
			aCheckedLine = oFileChecked.readlines()
			for sCheckedLine in aCheckedLine:
				aAlreadyChecked.append(sCheckedLine.replace("\r","").replace("\n","").split(":"))
	except:
		aAlreadyChecked = []
	aList = []
	try:
		with open(sFileList) as oFileList:
			aElement = oFileList.readlines()
			for sElement in aElement:
				if sElement.replace("\r","").replace("\n","").split(":") not in aAlreadyChecked:
					aList.append(sElement.replace("\r","").replace("\n","").split(":"))
	except:
		return False
	return aList
def writeThisFuckingSuccess(toWrite,sList):
	oFileObj = open("%s.success" % sList, 'a')
	oFileObj.write("\n".join(toWrite))
	oFileObj.close()
	os.unlink("%s.success" % sList)

def writeThisFuckingChecked(toWrite,sList):
	oFileObj = open("%s.checked" % sList, 'a')
	oFileObj.write("\n".join(toWrite))
	oFileObj.close()
	os.unlink("%s.checked" % sList)

def sendThisFuckingRequest(method,url,data={},cookie={},header={}):
	oRequest = requests.session()

	if method == "POST":
		oData = oRequest.post(url,data=data,headers=header,cookies=cookie)
	else:
		oData = oRequest.get(url,data=data,headers=header,cookies=cookie)
	return oData.text.encode('utf8'),oData.cookies

def getThisFuckingCapture(begin,end,index):
	start = begin
	end = end
	capt = re.findall(re.escape(start)+"(.*)"+re.escape(end),s)[index]
	return capt

def parseThisFuckingResponse(tocheck,patern,flag='d'):
	#Viendra lorsque j'aurai fait un parser avec beautiful soup

def checkTheseFuckingsArguments():
	if len(sys.argv) < 2:
		print "Wrong format : checker.py list x (x = thread count)"
		exit(0)
	return 1

def runThisFuckingChecker():
	global aList
	global bit
	global threadc

	threadc = 0
	i = 0
	while i < len(aList):
		if threadc < bit :
			aData = aList[i]
			threading.Thread(target=checkThisFuckingAccount, args=(aData[0],aData[1])).start()
			i += 1
			print "[%s/%s]\n" % (threadc,bit)

	return 1