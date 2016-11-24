#encoding:utf-8
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from userleftlabel import userLeftLabel
class userLeftButtomWidget(QWidget):
	instance = None
	def __init__(self):
		super(userLeftButtomWidget,self).__init__()
		mainlyt = QHBoxLayout()
		mainlyt.addWidget(userLeftLabel('switch','switch.png',None))
		mainlyt.addStretch(10)
		mainlyt.addWidget(userLeftLabel('delete','delete.png',None))
		mainlyt.addWidget(userLeftLabel('add','add.png',None))
		mainlyt.setContentsMargins(0,0,0,0)
		mainlyt.setSpacing(0)
		self.setAutoFillBackground(True)
		self.setBackgroundImageAndColor(QColor(255,255,255))
		self.setFixedSize(250,30)
		self.setLayout(mainlyt)
	@classmethod
	def getInstance(cls):
		if cls.instance is None:
			cls.instance = userLeftButtomWidget()
		return cls.instance
	def setBackgroundImageAndColor(self,qcolor):	
		from imageandcolor import ImageAndColor
		self.setPalette(ImageAndColor.getQPalette(qcolor))


