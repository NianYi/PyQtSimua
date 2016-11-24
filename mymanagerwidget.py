#encoding:utf-8
from PyQt5.QtGui import QColor,QPainter,QFont,QPixmap,QPalette
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QGridLayout,QLayout,QScrollArea,QSizePolicy
from PyQt5.QtCore import Qt
from mainconfigure import MainConfigure
class myManagerWidget(QLabel):
	instance = None
	def __init__(self):
		super(myManagerWidget,self).__init__()
		self.scrollArea = QScrollArea(self)
		self.scrollArea.setWidgetResizable(True)
		#self.setStyleSheet("background-color:white")
		mainlyt=QGridLayout()
		mainlyt.setContentsMargins(0,0,0,0)
		mainlyt.setSpacing(2)
		mainlyt.setAlignment(Qt.AlignTop)
		ind = 0
		self.itemSet = []
		from leftfloorlabel import leftFloorLabel
		for item in MainConfigure.thirdFloor:
			label_ = leftFloorLabel(MainConfigure.thirdFloor.index(item),item[0],item[1],item[2])
			mainlyt.addWidget(label_,ind,0)
			self.itemSet.append(label_)
			ind = ind+1
		widget = QWidget(self)
		widget.setLayout(mainlyt)
		self.scrollArea.setWidget(widget)
		rootlyt = QGridLayout()
		rootlyt.setContentsMargins(0,0,0,0)
		rootlyt.addWidget(self.scrollArea)
		self.setFixedWidth(150)
		self.setLayout(rootlyt)

	def update(self):
		from simua import mywindow
		mywindow.getInstance().setWindowTitle('%s(%d)'%(MainConfigure.thirdFloor[MainConfigure.currentManagerItem][-1],MainConfigure.currentManagerNum))
		mywindow.getInstance().show()
		from download import load
		from fileboxctl import fileBoxCtl
		from garbagectl import garbageCtl
		numFlag = [len(load.content_list),0,len(garbageCtl.content_list),len(fileBoxCtl.content_list),0]
		for ind in xrange(self.itemSet.__len__()):
			if numFlag[ind]==0:
				numFlag[ind]=''
			else:
				numFlag[ind]=str(numFlag[ind])
			self.itemSet[ind].tipLabel.setText(numFlag[ind])
		
	def clickEvent(self,preId,curId):
		from maincontroller import MainController
		self.itemSet[preId].setBackgroundImageAndColor(QColor(255,255,255))
		self.itemSet[curId].setBackgroundImageAndColor(QColor(209,209,209))
	@classmethod
	def getInstance(cls):
		#print 'ninini--',cls.instance
		if cls.instance is None:
			cls.instance = myManagerWidget()
		return cls.instance
	
if __name__=='__main__':
	import sys
	app = QApplication(sys.argv)
	win = myManagerWidget()
	win.show()
	sys.exit(app.exec_())
