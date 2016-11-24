#encoding:utf-8
from PyQt5.QtGui import QColor,QPainter,QFont,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QGridLayout,QLayout
from PyQt5.QtCore import Qt
class userLeftLabel(QWidget):
	def __init__(self,id_,icon_,title_):
		super(userLeftLabel,self).__init__()
		self.id = id_
		self.title = title_
		self.setAutoFillBackground(True)
		self.setBackgroundImageAndColor(QColor(255,255,255))
		self.initUI(icon_,title_)
	def initUI(self,icon_,title_):
		from imagebutton import imageButton
		self.mainlyt=QGridLayout()
		self.mainlyt.setSpacing(0)
		self.mainlyt.setContentsMargins(0,0,0,0)
		self.setLayout(self.mainlyt)
		self.mainlyt.addWidget(imageButton(-1,icon_,title_),0,0,Qt.AlignLeft)
		
	def mousePressEvent(self,event):
		if isinstance(self.id,int):
			from userleftwidget import userLeftWidget
			userLeftWidget.getInstance().update(self.id)
		elif self.id is 'switch':
			from userleftwidget import userLeftWidget
			uLW = userLeftWidget.getInstance()
			if uLW.currentID == -1:
				return
			from maincontroller import MainController
			MainController.dataClear(uLW.itemSet[uLW.currentID].title)
			from usermanager import userManager
			userManager.getInstance().close()
			#MainController.start()
			#MainController.jobCtl()

		elif self.id is 'delete':
			from userleftwidget import userLeftWidget
			uLW = userLeftWidget.getInstance()
			if uLW.currentID == -1:
				return
			uLW.itemSet[uLW.currentID].setVisible(False)
			from sqlitectl import sqliteCtl
			from mainconfigure import MainConfigure
			sqlwords = ["delete from user where id = '{0}'".format(uLW.itemSet[uLW.currentID].title)]
			print sqlwords
			sqliteCtl.updateDB(MainConfigure.userdbPath,*sqlwords)
			
		elif self.id is 'add':
			from userrightwidget import userRightWidget
			uRW = userRightWidget.getInstance()
			uRW.setVisible(not uRW.isVisible())
			from usermanager import userManager
			uM = userManager.getInstance()
			if uM.width() == 250:
				uM.setWindowTitle('添加用户')
				uM.setFixedWidth(500)
			else:
				uM.setFixedWidth(250)
				uM.setWindowTitle('用户')
		

	def setBackgroundImageAndColor(self,qcolor):	
		from imageandcolor import ImageAndColor
		self.setPalette(ImageAndColor.getQPalette(qcolor))


