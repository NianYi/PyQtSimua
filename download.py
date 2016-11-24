#coding:utf-8
#!/usr/bin/env python
import Tkinter
from imaplib import*
from  email import *
from email.utils import parseaddr
from email.header import decode_header
from email.parser import Parser
from RSA import rsa
from mystr import mystr
from django.utils.encoding import smart_str
from mainconfigure import MainConfigure
import sqlite3
import ConfigParser
import socket
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#-*-config file
config = ConfigParser.ConfigParser()
config.readfp(open('etc/pathcfg.ini','r'))
userdbPath = config.get("global","userdbpath")
datadbPath = config.get("global","datadbpath")

class load(object):
	to_list = []
	from_list = []
	date_list = []
	subject_list = []
	content_list = []
	id_list = []
	content = ''
	@classmethod
	def clearmail(cls):
		cls.to_list = []
		cls.from_list = []
		cls.date_list = []
		cls.subject_list = []
		cls.content_list = []
		cls.id_list = []
	@classmethod
	def loadlocalmail(cls):
		cls.to_list = []
		cls.from_list = []
		cls.date_list = []
		cls.subject_list = []
		cls.content_list = []
		cls.id_list = []
		username,password = cls.accesspass()
		if username is None or password is None:
			return False
		dataconn = sqlite3.connect(datadbPath+'mail.db')
		dataconn.text_factory=str
		datacursor = dataconn.cursor()
		tablename = mystr.mailname2tablename(username)
		datacursor.execute("create table if not exists %s (id integer primary key,subject varchar(80),from_ varchar(40),content varchar(4096),date varchar(20),is_garbage bit(1))"%tablename)
		
		datacursor.execute("select * from %s where is_garbage = 0 order by id desc"%(tablename))
		relt = datacursor.fetchall()
		#print type(relt)
		for item in relt:
			cls.id_list.append(item[0])	
			cls.subject_list.append(item[1])
			cls.from_list.append(item[2])
			cls.content_list.append(item[3])
			cls.date_list.append(item[4])

	@classmethod
	def loadnetmail(cls):
		username,password = cls.accesspass()
		if username is None or password is None:
			return
		print username,password
		dataconn = sqlite3.connect(datadbPath+'mail.db')
		dataconn.text_factory=str
		datacursor = dataconn.cursor()
		host = 'imap.qq.com'
		try:
			server =  IMAP4_SSL(host)
			server.login(username,password)
			rsp,msgs = server.select('INBOX',True)
			tablename = mystr.mailname2tablename(username)
			datacursor.execute("create table if not exists %s (id integer primary key,subject varchar(80),from_ varchar(40),content varchar(4096),date varchar(20),is_garbage bit(1))"%tablename)

			print "select max(id) from %s"%(tablename)

			datacursor.execute("select max(id) from %s"%(tablename))
		
			relt = datacursor.fetchone()
			if relt[0]==None:
				print 'None'
				lef=int(msgs[0])-1
				if lef < 1:
					lef = 1
			else:
				print 'HAS'
				lef=int(relt[0])+1
			print lef
			monthConversion = {
				'Jan':'01',
				'Feb':'02',
				'Mar':'03',
				'Apr':'04',
				'May':'05',
				'Jun':'06',
				'Jul':'07',
				'Aug':'08',
				'Sep':'09',
				'Oct':'10',
				'Nov':'11',
				'Dec':'12',
			}
			for index in range(lef,int(msgs[0])+1):
				rsp,data = server.fetch(index,'(RFC822)')
				mail = '\n'.join(data[0][1].splitlines())
				try:
					date = re.findall(r'Date:\s+(.{3,5}?\s+.{1,3}?\s+.{3,4}?\s+.{4}\s+.{6,10}?)\s+[\+|\-]',mail)
					print date
					li = re.split(r'\s+',date[0].strip())
					date = '{0}/{1}/{2}'.format(li[3],monthConversion[li[2]],li[1])
				except Exception,e:
					date = 'Unknow..'
				cls.date_list.insert(0,date)
				mail = Parser().parsestr(mail)
				load.content = ''
				cls.print_info(mail)
				cls.content_list.insert(0,cls.content)
				datacursor.execute("insert into %s (id,subject,from_,content,date,is_garbage) values (?,?,?,?,?,?)"%tablename,(index,cls.subject_list[0],cls.from_list[0],cls.content_list[0],date,0))
			print '----net mail  !!',int(msgs[0])-lef+1
		except socket.gaierror,e:
			print '无网络连接！',e
		except socket.error,e:
			print 'Socket 错误',e
		except Exception,e:
			print '其他错误',e
		finally:
			datacursor.close()
			dataconn.commit()
			dataconn.close()
			'''
			if server is not None:
				server.close()
				server.logout()
			'''
	#-*-尝试从current_user表中获取账户密码
	@classmethod
	def accesspass(cls):
		if MainConfigure.currentUser.__len__() == 0:
			return None,None
		userconn = sqlite3.connect(userdbPath+"shadow.db")
		cursor = userconn.cursor()
		cursor.execute('select * from user where id = "{}"'.format(MainConfigure.currentUser))
		relt = cursor.fetchone()
		#print relt
		if relt == None:
			return None,None
		return	relt[0],rsa.decrypt(relt[3],relt[1])

	@classmethod
	def print_info(cls,msg,indent=0):
		for header in['From','To','Subject']:
			value  =msg.get(header,'')
	
			if value:
				if header == 'Subject':
					value = cls.decode_str(value)
				else:
					hdr,addr = parseaddr(value)
					name = cls.decode_str(hdr)
					value = '%s <%s>' % (smart_str(name), smart_str(addr))
				if header == 'From':
					cls.from_list.insert(0,value)
				elif header == 'To':
					cls.to_list.insert(0,value)
				else:
					cls.subject_list.insert(0,value)
		if (msg.is_multipart()):
			for part in msg.walk():
				if part.get_content_type()=='text/html':
					load.content = part.get_payload(decode=True)
					break
			if load.content is None:
				for part in msg.walk():
					load.content = part.get_payload(decode=True)
					if load.content is not None:
						break
			
		else:
			print msg.get_content_type()
			content_type = msg.get_content_type()
			if content_type=='text/plain' or content_type=='text/html':
				content = msg.get_payload(decode=True)
				load.content = load.content + content
			else:
				load.content = load.content + '%sAttachment: %s\n' % ('  ' * indent, content_type)
	@classmethod
	def decode_str(cls,s):
		value, charset = decode_header(s)[0]
		if charset:
			#print charset
			try:
				value = value.decode(charset)
			except:
				#print 'decode_str_eooor'
				value=smart_str(value)
				#print len(value)

		return value
	@classmethod
	def guess_charset(cls,msg):
		charset = msg.get_charset()
		if charset is None:
			content_type = msg.get('Content-Type', '').lower()
			pos = content_type.find('charset=')
			if pos >= 0:
				charset = content_type[pos + 8:].split(';')[0]
		return charset.strip()
	@classmethod
	def authentication(cls,username,password):
		host = 'imap.qq.com'
		server =  IMAP4_SSL(host)
		try:
			server.login(username,password)
			return True
		except Exception,e:
			print e	
		return False
if __name__=='__main__':
	with open('296','r') as fp:
		s1 = fp.read()
	s1 = Parser().parsestr(s1)
	load.print_info(s1)
	
