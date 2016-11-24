from PyQt5.QtWidgets import QLabel,QGridLayout,QWidget
from PyQt5.QtGui import QPixmap,QBitmap,QColor,QBrush
from PyQt5.QtCore import Qt
from textlabel import TextLabel
from mainconfigure import MainConfigure
from maincontroller import MainController
class imageButton(QWidget):
	def __init__(self,floor,icon=None,title=None):
		super(imageButton,self).__init__()
		self.floor = floor
		height = 30
		width = 40
		errorValue=5
		import os
		if icon is not None and not os.path.exists(icon):
			print icon,'not exist!'
			icon = None

		if icon and title is None:
			mainlyt = QGridLayout()
			mainlyt.setContentsMargins(0,0,0,0)
			self.setLayout(mainlyt)
			self.l1=QLabel()
			self.l1.setPixmap(QPixmap(icon))
			mainlyt.addWidget(self.l1)
			#self.setAutoFillBackground(True)
		elif icon is None and title:
			mainlyt = QGridLayout()
			self.setLayout(mainlyt)
			mainlyt.setContentsMargins(0,0,0,0)
			mainlyt.setSpacing(0)
			mainlyt.addWidget(QLabel(title))
			width = TextLabel.getTextLength(title,self.font())+errorValue
		else:
			mainlyt = QGridLayout()
			mainlyt.setContentsMargins(0,0,0,0)
			mainlyt.setSpacing(0)
			self.setLayout(mainlyt)
			self.l1=QLabel()
			self.l1.setPixmap(QPixmap(icon))
			mainlyt.addWidget(self.l1,0,0)
			mainlyt.addWidget(QLabel(title),0,1)
			width = width + TextLabel.getTextLength(title,self.font())
		self.setFixedSize(width,height)
		if self.floor is MainConfigure.MIDFLOOR:
			self.setBackgroundImageAndColor(QColor(209,209,209))
			
	#*----------
	def setBackgroundImageAndColor(self,background):
		from imageandcolor import ImageAndColor
		self.setPalette(ImageAndColor.getQPalette(background))
	def enterEvent(self,event):
		if self.floor is MainConfigure.MIDFLOOR:
			self.setAutoFillBackground(True)
	def leaveEvent(self,event):
		if self.floor is MainConfigure.MIDFLOOR:
			self.setAutoFillBackground(False)
	#----------*
