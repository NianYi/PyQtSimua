from PyQt5.QtWidgets import QWidget,QGridLayout
from PyQt5.QtGui import QPixmap
from imagebutton import imageButton
from mainconfigure import MainConfigure
class topFloorLabel(QWidget):
	def __init__(self,internalID,externalID,icon=None,title=None):
		super(topFloorLabel,self).__init__()
		self.internalID = internalID
		self.externalID = externalID
		mainlyt = QGridLayout()
		mainlyt.setContentsMargins(0,0,0,0)
		self.setLayout(mainlyt)
		self.label_ = imageButton(MainConfigure.TOPFLOOR,icon,title)
		mainlyt.addWidget(self.label_)
	def mousePressEvent(self,event):
		self.label_.l1.setPixmap(QPixmap('image%sPress.png'%(self.externalID)))
	def mouseReleaseEvent(self,event):
		from maincontroller import MainController
		self.label_.l1.setPixmap(QPixmap('image%s.png'%(self.externalID)))
		MainController.imageButtonPressed(self.externalID)

