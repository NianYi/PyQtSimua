from PyQt5.QtWidgets import QWidget,QGridLayout
from imagebutton import imageButton
from mainconfigure import MainConfigure
class midFloorLabel(QWidget):
	def __init__(self,internalID,externalID,icon=None,title=None):
		super(midFloorLabel,self).__init__()
		self.internalID = internalID
		self.externalID = externalID
		mainlyt = QGridLayout()
		mainlyt.setContentsMargins(0,0,0,0)
		self.setLayout(mainlyt)
		#self.setFixedHeight(30)
		mainlyt.addWidget(imageButton(MainConfigure.MIDFLOOR,icon,title))
	def mousePressEvent(self,event):
		if MainConfigure.currentManagerItem is not self.externalID-MainConfigure.MAILBOX:
			from maincontroller import MainController
			MainController.imageButtonPressed(self.externalID)
		
