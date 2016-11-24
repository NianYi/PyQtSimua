from PyQt5.QtGui import QColor,QPainter,QFont,QPixmap,QPalette
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QGridLayout,QLayout,QScrollArea,QSizePolicy
from PyQt5.QtCore import Qt
class userLeftWidget(QWidget):
	inStance = None
	def __init__(self):
		super(userLeftWidget,self).__init__()
		self.currentID = -1
		scrollArea = QScrollArea(self)
		scrollArea.setWidgetResizable(True)
		self.mainlyt=QGridLayout()
		self.mainlyt.setContentsMargins(0,0,0,0)
		self.mainlyt.setSpacing(2)
		self.mainlyt.setAlignment(Qt.AlignTop)	
		widget = QWidget(self)
		scrollArea.setWidget(widget)
		widget.setLayout(self.mainlyt)
		rootlyt = QGridLayout()
		rootlyt.setContentsMargins(0,0,0,0)
		rootlyt.addWidget(scrollArea,0,0,1,1)
		self.setFixedWidth(250)
		self.setLayout(rootlyt)

		self.itemSet=[]
	@classmethod
	def getInstance(cls):
		if cls.inStance is None:
			cls.inStance = userLeftWidget()
		return cls.inStance
	def update(self,clickedID):
		if self.currentID != -1:
			self.itemSet[self.currentID].setBackgroundImageAndColor(QColor(255,255,255))
			
		self.itemSet[clickedID].setBackgroundImageAndColor(QColor(219,219,219))
		self.currentID = clickedID
		
	def start(self,*args):
		from userleftlabel import userLeftLabel
		for image,userid in args:
			label_ = userLeftLabel(self.itemSet.__len__(),image,userid)
			self.itemSet.append(label_)
			self.mainlyt.addWidget(label_)
		
	def setBackgroundImageAndColor(self,qcolor):	
		from imageandcolor import ImageAndColor
		self.setPalette(ImageAndColor.getQPalette(qcolor))


