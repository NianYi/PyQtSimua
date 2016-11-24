from PyQt5.QtGui import QColor,QPainter,QFont,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QGridLayout,QLayout
from textlabel import TextLabel
from maincontroller import MainController
from mainconfigure import MainConfigure
class mySuperLabel(QWidget):
	def __init__(self,id_,from_,date_,subject_,content_):
		super(mySuperLabel,self).__init__()
		self.setAutoFillBackground(True)
		self.id = id_
		if self.id is MainConfigure.currentDescriptionItem:
			self.setBackgroundImageAndColor(QColor(209,209,209))
		else:
			self.setBackgroundImageAndColor(QColor(255,255,255))

		#self.setStyleSheet("background-color:rgb(0,0,0)")
		self.initUI(from_,date_,subject_,content_)
		self.setFixedWidth(270)
	def initUI(self,from_,date_,subject_,content_):
		singleLine=1
		doubleLine=2
		l1=TextLabel(160,from_,singleLine)
		d1=TextLabel(80,date_,singleLine)
		l2=TextLabel(240,subject_,singleLine)
		l3=TextLabel(240,content_,doubleLine)
		self.f1=QLabel()
		self.f1.setPixmap(QPixmap('flagOn.png'))
		self.f1.setFixedWidth(20)
		#l1.setFixedWidth(150)
		#d1.setFixedWidth(90)
		#l2.setFixedWidth(250)
		#l3.setFixedWidth(250)

		self.flag=True
		self.mainlyt=QGridLayout()
		self.leflyt=QGridLayout()
		self.riglyt=QGridLayout()
		self.mainlyt.addLayout(self.leflyt,0,0,1,1)
		self.mainlyt.addLayout(self.riglyt,0,1,1,19)
		self.mainlyt.setSpacing(0)
		self.mainlyt.setContentsMargins(0,0,0,0)
		self.setLayout(self.mainlyt)
		self.setFixedHeight(70)
		self.leflyt.addWidget(self.f1)
		self.leflyt.setContentsMargins(0,0,0,0)
		
		self.uplyt=QGridLayout()
		self.downlyt=QGridLayout()
		self.riglyt.addLayout(self.uplyt,0,0,1,1)
		self.riglyt.addLayout(self.downlyt,1,0,3,1)
		self.riglyt.setContentsMargins(0,0,0,0)
		self.riglyt.setSpacing(0)
		self.uplyt.addWidget(l1,0,0,1,3)
		self.uplyt.addWidget(d1,0,3,1,1)
		self.uplyt.setContentsMargins(0,0,0,0)
		self.uplyt.setSpacing(0)

		self.downlyt.addWidget(l2,0,0,1,1)
		self.downlyt.addWidget(l3,1,0,2,1)
		self.downlyt.setSpacing(0)
		self.downlyt.setContentsMargins(0,0,0,0)	
	def mousePressEvent(self,event):
		if self.flag is True:
			self.flag = False
			self.f1.setPixmap(QPixmap('flagOff.png'))
		print MainConfigure.currentDescriptionItem, self.id
		if MainConfigure.currentDescriptionItem != self.id:
			MainController.textLabelPressed(self.id)

	def setBackgroundImageAndColor(self,qcolor):	
		from imageandcolor import ImageAndColor
		self.setPalette(ImageAndColor.getQPalette(qcolor))

if __name__=='__main__':

	import sys
	app = QApplication(sys.argv)
	win = mySuperLabel()
	print win.size()
	win.show()
	sys.exit(app.exec_())

