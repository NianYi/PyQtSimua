#coding:utf-8
#!/usr/bin/env python
from mystr import mystr
from django.utils.encoding import smart_str
from mainconfigure import MainConfigure
import sqlite3
import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#-*-config file
config = ConfigParser.ConfigParser()
config.readfp(open('etc/pathcfg.ini','r'))
datadbPath = config.get("global","datadbpath")

class fileBoxCtl(object):
	from_list = []
	id_list = []
	subject_list = []
	content_list = []
	date_list = []
	@classmethod
	def appendItem(cls,*args):
		li = [cls.from_list,cls.id_list,cls.subject_list,cls.content_list,cls.date_list]
		for ind in xrange(len(args)):
			li[ind].insert(0,args[ind])
	@classmethod
	def popItem(cls,index):
		li = [cls.from_list,cls.id_list,cls.subject_list,cls.content_list,cls.date_list]
		for ind in xrange(len(li)):
			li[ind].pop(index)
	


	@classmethod
	def init(cls):
		cls.from_list = []
		cls.id_list = []
		cls.subject_list = []
		cls.content_list = []
		cls.date_list = []
		import cPickle as pickle
		import os
		filepath =  MainConfigure.fileBoxIDSetPath+MainConfigure.currentUser
		if not os.path.isfile(filepath):
			return
		#print 'fileBox',MainConfigure.fileBoxIDSet
		with open(filepath,'r') as fp:
			relt = pickle.load(fp)
			#print relt
			if relt.__len__() >= 3:
				MainConfigure.fileBoxIDSet=relt
		#print MainConfigure.fileBoxIDSet
		datadblist = [datadbPath+'mail.db',datadbPath+'sendmail.db',datadbPath+'drafts.db']
		#print MainConfigure.fileBoxIDSet
		from download import load
		username,password = load.accesspass()
		if username is None or password is None:
			return False
		for ind in xrange(3):
			dataconn = sqlite3.connect(datadblist[ind])
			dataconn.text_factory=str
			datacursor = dataconn.cursor()
			tablename = mystr.mailname2tablename(username)
			datacursor.execute("create table if not exists %s (id integer primary key,subject varchar(80),from_ varchar(40),content varchar(4096),date varchar(20),is_garbage bit(1))"%tablename)
			for item in MainConfigure.fileBoxIDSet[ind]:
				datacursor.execute("select * from %s where id=%s and is_garbage=0"%(tablename,item))
				relt = datacursor.fetchall()
				#print type(relt)
				for item1 in relt:
					cls.date_list.insert(0,item1[4])
					cls.id_list.insert(0,item1[0])
					cls.subject_list.insert(0,item1[1])
					cls.from_list.insert(0,item1[2])
					cls.content_list.insert(0,item1[3])

	
