#encoding:utf-8
from PyQt5.QtCore import QObject
from mainconfigure import MainConfigure
from mymanagerwidget import myManagerWidget
class MainController(QObject):
	def __init__(self):
		super(myMainController,self).__init__()
	@staticmethod
	def dataClear(newUser):
		from download import load
		load.clearmail()
		import cPickle as pickle
		with open(MainConfigure.fileBoxIDSetPath+MainConfigure.currentUser,'wb') as fp:
			pickle.dump(MainConfigure.fileBoxIDSet,fp)

		MainConfigure.fileBoxIDSet=[set(),set(),set()]
		MainConfigure.currentDescriptionItem = -1
		if MainConfigure.currentManagerItem is not 0:
			from mymanagerwidget import myManagerWidget
			myManagerWidget.getInstance().clickEvent(MainConfigure.currentManagerItem,0)
		MainConfigure.currentUser = newUser
		MainConfigure.currentManagerItem = 0
		from fileboxctl import fileBoxCtl
		from garbagectl import garbageCtl
		fileBoxCtl.init()
		garbageCtl.init()
		print '切换账户--start'
		MainController.start()
		#MainController.jobCtl()
	@staticmethod
	def jobCtl():
		from threading import Thread
		from download import load
		thread1 = Thread(target=load.loadnetmail,args=())
		thread1.start()
	@staticmethod
	def start():
		from mydescriptionwidget import myDescriptionWidget as mDW
		from mymanagerwidget import myManagerWidget as mMW
		from mywebview import myWebView
		if MainConfigure.currentManagerItem is 0:
			from download import load
			if len(load.from_list) == 0:
				load.loadlocalmail()
				
			MainConfigure.from_list = load.from_list
			MainConfigure.id_list = load.id_list
			MainConfigure.subject_list = load.subject_list
			MainConfigure.content_list = load.content_list
			MainConfigure.date_list = load.date_list
		elif MainConfigure.currentManagerItem is 1:
			MainConfigure.from_list=[]
			MainConfigure.id_list=[]
			MainConfigure.subject_list=[]
			MainConfigure.content_list=[]
			MainConfigure.date_list = []
		elif MainConfigure.currentManagerItem is 2:
			from garbagectl import garbageCtl
			MainConfigure.from_list=garbageCtl.from_list
			MainConfigure.id_list=garbageCtl.id_list
			MainConfigure.subject_list=garbageCtl.subject_list
			MainConfigure.content_list=garbageCtl.content_list
			MainConfigure.date_list = garbageCtl.date_list
		elif MainConfigure.currentManagerItem is 3:
			from fileboxctl import fileBoxCtl
			MainConfigure.from_list=fileBoxCtl.from_list
			MainConfigure.id_list=fileBoxCtl.id_list
			MainConfigure.subject_list=fileBoxCtl.subject_list
			MainConfigure.content_list=fileBoxCtl.content_list
			MainConfigure.date_list = fileBoxCtl.date_list
		elif MainConfigure.currentManagerItem is 4:
			MainConfigure.from_list=[]
			MainConfigure.id_list=[]
			MainConfigure.subject_list=[]
			MainConfigure.content_list=[]
			MainConfigure.date_list = []

		MainConfigure.currentManagerNum = MainConfigure.from_list.__len__()
		try:
			mMW.getInstance().update()
			mDW.getInstance().update()
			myWebView.getInstance().update()
		except Exception,e:
			print e
	@staticmethod
	def textLabelPressed(id):
		from mydescriptionwidget import myDescriptionWidget
		myDescriptionWidget.getInstance().clickEvent(MainConfigure.currentDescriptionItem,id)
		MainConfigure.currentDescriptionItem = id
		from mywebview import myWebView
		print 'start----'
		myWebView.getInstance().update()
		
	@staticmethod
	def imageButtonPressed(id):
		cls = MainConfigure
		if id is cls.RECEIVE:
			print 'receive1 pressed!'
		elif id is cls.WRITE:
			print 'write1 pressed!'
		elif id is cls.FILE:
			id = cls.id_list[cls.currentDescriptionItem]
			print id
			flag = False
			print id,cls.currentManagerItem
			if cls.currentManagerItem is 0 and id not in cls.fileBoxIDSet[0]:
				cls.fileBoxIDSet[0].add(id)
				flag = True
			elif cls.currentManagerItem is 1:
				cls.fileBoxIDSet[1].add(id)	
				flag = True
			elif cls.currentManagerItem is 4:
				cls.fileBoxIDSet[2].add(id)
				flag = True
			if flag:
				id = cls.currentDescriptionItem
				from fileboxctl import fileBoxCtl
				li=[cls.from_list[id],cls.id_list[id],cls.subject_list[id],cls.content_list[id],cls.date_list[id],]
				fileBoxCtl.appendItem(*li)
		elif id is cls.DELETE:
			from sqlitectl import sqliteCtl
			from download import load
			from mystr import mystr
			from garbagectl import garbageCtl
			import ConfigParser
			#-*-config file
			config = ConfigParser.ConfigParser()
			config.readfp(open('etc/pathcfg.ini','r'))
			datadbPath = config.get("global","datadbpath")
			id = cls.id_list[cls.currentManagerItem]
			tablename = mystr.mailname2tablename(load.accesspass()[0])
			if cls.currentManagerItem is 0:
				datadbPath = datadbPath+'/mail.db'
				sqllist = ['update {0} set is_garbage = 1 where id = {1}'.format(tablename,id)]
				
				sqliteCtl.updateDB(datadbPath,*sqllist)
				ind = cls.currentDescriptionItem
				li=[load.from_list.pop(ind),load.id_list.pop(ind),load.subject_list.pop(ind),load.content_list.pop(ind),load.date_list.pop(ind)]
				garbageCtl.appendItem(*li)
				cls.currentDescriptionItem=0
				from fileboxctl import fileBoxCtl
				if id in fileBoxCtl.id_list:
					index_ = fileBoxCtl.id_list.index(id)
					fileBoxCtl.popItem(index_)
					MainConfigure.fileBoxIDSet[0].remove(id)
				MainController.start()	
			elif cls.currentManagerItem is 1:
				pass
				#datadbPath = datadbPath+'/mail.db'
			elif cls.currentManagerItem is 2:
				print 'garbege'
				#datadbPath = datadbPath+'/mail.db'
			elif cls.currentManagerItem is 4:
				pass
				#datadbPath = datadbPath+'/mail.db'
		elif id is cls.USERMANAGER:
			from usermanager import userManager
			userManager.getInstance().show()
		elif id is cls.SEARCH:
			print 'search1 pressed!'
		elif id is cls.MAILMANAGER:
			mMW =  myManagerWidget.getInstance()
			mMW.setVisible(not mMW.isVisible())
		elif id is cls.MAILBOX:
			MainController.leftFloorLabelPressed(0)
			MainController.start()
		elif id is cls.SENDBOX:
			MainController.leftFloorLabelPressed(1)
			MainController.start()
		elif id is cls.DRAFTSBOX:
			MainController.leftFloorLabelPressed(4)
			MainController.start()
		elif id is cls.GARBAGE:
			MainController.leftFloorLabelPressed(2)
			MainController.start()
		elif id is cls.FILEBOX:
			MainController.leftFloorLabelPressed(3)
			MainController.start()
		else:
			pass
	@staticmethod
	def leftFloorLabelPressed(internalID):
		myManagerWidget.getInstance().clickEvent(MainConfigure.currentManagerItem,internalID)
		MainConfigure.currentManagerItem = internalID
		MainConfigure.currentDescriptionItem = -1

		#update description widget and webview
