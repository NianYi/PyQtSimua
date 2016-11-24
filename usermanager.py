#encoding:utf-8
from PyQt5.QtWidgets import QWidget,QGridLayout,QApplication
from userleftwidget import userLeftWidget
from userrightwidget import userRightWidget
class userManager(QWidget):
	instance = None
	def __init__(self):
		super(userManager,self).__init__()
		self.user_list = []
		mainlyt = QGridLayout()
		leflyt = QGridLayout()
		riglyt = QGridLayout()
		mainlyt.addLayout(leflyt,0,0,1,1)
		mainlyt.addLayout(riglyt,0,1,1,1)
		mainlyt.setContentsMargins(0,0,0,0)
		mainlyt.setSpacing(0)
		leftwidget = userLeftWidget.getInstance()
		rigwidget = userRightWidget.getInstance()
		rigwidget.setVisible(False)
		leflyt.addWidget(leftwidget,0,0)
		from userleftbuttomwidget import userLeftButtomWidget
		leflyt.addWidget(userLeftButtomWidget.getInstance(),1,0)
		leflyt.setContentsMargins(0,0,0,0)

		riglyt.addWidget(rigwidget)
		self.setLayout(mainlyt)
		self.setFixedSize(250,280)
		self.setWindowTitle('用户')
		self.start()
	def start(self):
		from sqlitectl import sqliteCtl
		from mainconfigure import MainConfigure
		sqlwords = "select id from user"
		for tup in sqliteCtl.queryDB(MainConfigure.userdbPath,sqlwords):
			self.user_list.append(('QQ.png',tup[0]))
		userLeftWidget.getInstance().start(*self.user_list)
	@classmethod
	def getInstance(cls):
		if cls.instance is None:
			cls.instance = cls()
		return cls.instance
		
if __name__=='__main__':
	import sys
	app = QApplication(sys.argv)
	from usermanager import userManager
	userManager.getInstance().show()
	sys.exit(app.exec_())
