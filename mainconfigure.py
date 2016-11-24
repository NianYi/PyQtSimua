#encoding:utf-8
class MainConfigure(object):
	TOPFLOOR,MIDFLOOR,LEFTFLOOR = range(3)
	#-*- Function Flag!!!
	functionNum = 12
	RECEIVE,WRITE,FILE,DELETE,USERMANAGER,SEARCH,\
	MAILMANAGER,\
	MAILBOX,SENDBOX,GARBAGE,FILEBOX,DRAFTSBOX = range(functionNum)
	
	#-*- run flag
	currentManagerItem = 0
	currentDescriptionItem = -1
	
	#-*- top & left widget argument
	firstFloor=[(RECEIVE,'image0.png'),(WRITE,'image1.png'),\
		(FILE,'image2.png'),(DELETE,'image3.png'),(USERMANAGER,'image4.png')]	#,(SEARCH,None)]
	secondFloor=[(MAILMANAGER,'image10.png','分栏'),(MAILBOX,None,'收件箱'),\
		(SENDBOX,None,'已发邮件'),(DRAFTSBOX,None,'草稿箱')]
	thirdFloor=[(MAILBOX,'image20.png','收件箱'),(SENDBOX,'image21.png','已发邮件'),\
		(GARBAGE,'image22.png','垃圾篓'),(FILEBOX,'image23.png','归档'),(DRAFTSBOX,'image24.png','草稿箱')]
	
	#-*- mainWindowTitle
	mainWindowTitle = [None,None,None,None,None,None,'收件箱','已发邮件','垃圾篓','归档','草稿箱']
	
	#mydescription data
	from_list = []
	id_list = []
	subject_list = []
	content_list = []
	date_list = []
	#flag nums
	currentManagerNum = 0
	leftFloorNums = [0 for x in xrange(5)]
	
	#ID for FILEBOX,GARBAGE
	fileBoxIDSetPath = './usr/fileboxdata'
	fileBoxIDSet = [set(),set(),set()]

	#database path
	userdbPath = 'usr/userdb/shadow.db'
	maildbPath = 'usr/userdb/mail.db'
	sendmaildbPath = 'usr/userdb/sendmail.db'
	draftsdbPath = 'usr/userdb/drafts.db'
	#current user
	currentUser = ''
	currentUserPath = './usr/currentUser'

	def __init__(self):
		super(MainConfugure).__init__()
