#coding:utf-8
from PyQt5.QtWidgets import QWidget,QLineEdit,QGridLayout,QLabel,QComboBox,QPushButton,QMessageBox
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class userRightWidget(QLabel):
	instance = None
	def __init__(self):
		super(userRightWidget,self).__init__()
		self.initUI()
		self.setFixedWidth(250)
	def initUI(self):
		self.userLabel = QLabel("User:")
		self.userEdit = QLineEdit()
		self.passLabel = QLabel("Pass:")
		self.passEdit = QLineEdit()
		self.passEdit.setEchoMode(QLineEdit.Password)
		self.typeLabel = QLabel("Type:")
		self.comboBox = QComboBox()
		self.comboBox.addItems(['QQ Mail','163 Mail','126 Mail'])
		self.button = QPushButton("添加账户")
		self.button.clicked.connect(self.go)
		mainlyt = QGridLayout()
		self.setLayout(mainlyt)
		mainlyt.addWidget(self.userLabel,0,0,1,1)
		mainlyt.addWidget(self.userEdit,0,1,1,3)
		mainlyt.addWidget(self.passLabel,1,0,1,1)
		mainlyt.addWidget(self.passEdit,1,1,1,3)
		mainlyt.addWidget(self.typeLabel,2,0,1,1)
		mainlyt.addWidget(self.comboBox,2,1,1,3)
		mainlyt.addWidget(self.button,3,3,1,1)
	def go(self):
		username = self.userEdit.text()
		password = self.passEdit.text()
		if username.__len__()==0 or password.__len__() == 0:
			QMessageBox.warning(self,self.tr('Warning'),'用户或密码为空！')
			return
		from download import load
		if not load.authentication(username,password):
			QMessageBox.warning(self,self.tr('Error'),'用户或密码错误！')
			self.userEdit.clear()
			self.passEdit.clear()
			return
		
		from sqlitectl import sqliteCtl
		from mainconfigure import MainConfigure
		sqlwords = "select id from user"
		for item in sqliteCtl.queryDB(MainConfigure.userdbPath,sqlwords):
			if username == item[0]:
				QMessageBox.warning(self,self.tr('Tip'),'用户已存在！')
				self.userEdit.clear()
				self.passEdit.clear()
				return
	
		from RSA import rsa
		pubKey,privKey = rsa.generate()
		rsa.encrypt(pubKey,password)
		sqlwords = "insert into user values('{}','{}','{}','{}')".format(username,rsa.encrypt(pubKey,password),pubKey,privKey)
		sqliteCtl.updateDB(MainConfigure.userdbPath,sqlwords)
		from userleftwidget import userLeftWidget
		userLeftWidget.getInstance().start(*[('QQ.png',username)])
		self.userEdit.clear()
		self.passEdit.clear()
	@classmethod
	def getInstance(cls):
		if cls.instance is None:
			cls.instance = userRightWidget()
		return cls.instance
	
