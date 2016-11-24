#encoding:utf-8
from PyQt5.QtGui import QColor,QPainter,QFont,QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QGridLayout,QLayout
from mainconfigure import MainConfigure
from maincontroller import MainController
class leftFloorLabel(QWidget):
	def __init__(self,internalID,externalID,icon_,title_):
		super(leftFloorLabel,self).__init__()
		self.setAutoFillBackground(True)
		self.externalID = externalID
		self.internalID = internalID
		if self.internalID is MainConfigure.currentManagerItem:
			self.setBackgroundImageAndColor(QColor(209,209,209))
		else:
			self.setBackgroundImageAndColor(QColor(255,255,255))
		self.initUI(internalID,externalID,icon_,title_)
		self.setFixedHeight(35)
	def initUI(self,internalID,externalID,icon_,title_):
		from imagebutton import imageButton
		self.mainlyt=QGridLayout()
		self.mainlyt.setSpacing(2)
		self.mainlyt.setContentsMargins(0,0,0,0)
		self.setLayout(self.mainlyt)
		self.setFixedHeight(70)
		self.mainlyt.addWidget(imageButton(MainConfigure.LEFTFLOOR,icon_,title_),0,0,1,4)
		self.tipLabel = QLabel()
		self.mainlyt.addWidget(self.tipLabel,0,4,1,1)
	def mousePressEvent(self,event):
		if MainConfigure.currentManagerItem is not self.externalID:
			MainController.leftFloorLabelPressed(self.internalID)
			MainController.start()


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

