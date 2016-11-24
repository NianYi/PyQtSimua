#encoding:utf-8
from PyQt5.QtWidgets import (QGraphicsView,QGraphicsScene,QApplication,\
	QLabel,QPushButton,QWidget,QSpinBox,QSlider,QHBoxLayout,QGridLayout,\
	QLayout,QMessageBox,QSizePolicy)
from PyQt5.QtCore import Qt
from mywebview import myWebView

from mainconfigure import MainConfigure
class mywindow(QWidget):
	instance = None
	def __init__(self):
		#from mainconfigure import MainConfigure
		from mytopfloorwidget import myTopFloorWidget
		from mymidfloorwidget import myMidFloorWidget
		#from mywebview import myWebView
		from mydescriptionwidget import myDescriptionWidget

		super(mywindow,self).__init__()
		self.setWindowTitle('收件箱')
		mainlyt = QGridLayout()
		uplyt = QGridLayout()
		downlyt = QGridLayout()
		leflyt = QGridLayout()
		midlyt = QGridLayout()
		riglyt = QGridLayout()
		mainlyt.addLayout(uplyt,0,0,1,1)
		mainlyt.addLayout(downlyt,1,0,9,1)
		mainlyt.setContentsMargins(0,0,0,0)
		mainlyt.setSpacing(0)
		downlyt.addLayout(leflyt,0,0,1,1)
		downlyt.addLayout(midlyt,0,1,1,1)
		downlyt.addLayout(riglyt,0,2,1,2)
		webview = myWebView.getInstance()	
		uplyt.addWidget(myTopFloorWidget.getInstance(),0,0,1,1)
		uplyt.addWidget(myMidFloorWidget.getInstance(),1,0,1,1)
		uplyt.setContentsMargins(0,0,0,0)
		uplyt.setSpacing(0)
		from mymanagerwidget import myManagerWidget
		mMW=myManagerWidget.getInstance()
		leflyt.addWidget(mMW)
		midlyt.addWidget(myDescriptionWidget.getInstance())
		riglyt.setContentsMargins(0,1,0,0)
		riglyt.addWidget(webview)
		self.setLayout(mainlyt)
	@classmethod
	def getInstance(cls):
		if cls.instance is None:
			cls.instance = mywindow()
		return cls.instance
	def closeEvent(self,event):
		import cPickle as pickle
		with open(MainConfigure.fileBoxIDSetPath+MainConfigure.currentUser,'wb') as fp:
			pickle.dump(MainConfigure.fileBoxIDSet,fp)
		with open(MainConfigure.currentUserPath,'wb') as fp:
			pickle.dump(MainConfigure.currentUser,fp)
		return
		if QMessageBox.question(self,self.tr('Quit'),'Sure?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No) == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
if __name__=='__main__':
	from maincontroller import MainController
	import sys
	app=QApplication(sys.argv)
	from fileboxctl import  fileBoxCtl 
	from garbagectl import garbageCtl
	import cPickle as pickle
	import os
	filepath =  MainConfigure.currentUserPath
	if os.path.isfile(filepath):
		with open(filepath,'r') as fp:
			MainConfigure.currentUser = pickle.load(fp)
	garbageCtl.init()

	fileBoxCtl.init()

	MainController.start()

	MainController.jobCtl()
	sys.exit(app.exec_())
