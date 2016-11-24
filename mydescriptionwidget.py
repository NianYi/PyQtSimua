from PyQt5.QtGui import QColor,QPainter,QFont,QPixmap,QPalette
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QGridLayout,QLayout,QScrollArea,QSizePolicy
from PyQt5.QtCore import Qt
from mysuperlabel import mySuperLabel
from mainconfigure import MainConfigure
class myDescriptionWidget(QWidget):
	inStance = None
	def __init__(self):
		super(myDescriptionWidget,self).__init__()
		scrollArea = QScrollArea(self)
		scrollArea.setWidgetResizable(True)
		self.mainlyt=QGridLayout()
		self.mainlyt.setContentsMargins(0,0,0,0)
		self.mainlyt.setSpacing(1)
		self.mainlyt.setAlignment(Qt.AlignTop)	
		widget = QWidget(self)
		scrollArea.setWidget(widget)
		widget.setLayout(self.mainlyt)
		scrollArea.setWidget(widget)
		rootlyt = QGridLayout()
		rootlyt.setContentsMargins(0,0,0,0)
		rootlyt.addWidget(scrollArea)
		self.setFixedWidth(275)
		self.setLayout(rootlyt)
		self.itemSet=[]
	@classmethod
	def getInstance(cls):
		if cls.inStance is None:
			cls.inStance = myDescriptionWidget()
		return cls.inStance
	def update(self):
		for item in self.itemSet:
			self.mainlyt.removeWidget(item)
			item.hide()
			item.destroy()
		self.itemSet=[]
		self.mainlyt.update()
		for ind in range(0,len(MainConfigure.content_list)):
			label_ = mySuperLabel(ind,MainConfigure.from_list[ind],MainConfigure.date_list[ind],MainConfigure.subject_list[ind],MainConfigure.content_list[ind][:50])
			self.itemSet.append(label_)
			self.mainlyt.addWidget(label_,ind,0)
		#MainConfigure.currentDescriptionItem=0
	def clickEvent(self,preId,curId):
		self.itemSet[preId].setBackgroundImageAndColor(QColor(255,255,255))
		self.itemSet[curId].setBackgroundImageAndColor(QColor(209,209,209))

if __name__=='__main__':
	import sys
	app = QApplication(sys.argv)
	win = myDescriptionWidget()
	win.show()
	sys.exit(app.exec_())
