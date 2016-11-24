#!-*-encoding:utf-8
from PyQt5.QtGui import QColor,QPainter,QFont,QPixmap,QPalette,QIcon,QImage,QBrush
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout,QGridLayout,QLayout,QScrollArea,QSizePolicy,QLineEdit
from PyQt5.QtCore import Qt
from imagebutton import imageButton
from mainconfigure import MainConfigure
from midfloorlabel import midFloorLabel
class myMidFloorWidget(QLabel):
	instance = None
	def __init__(self):
		super(myMidFloorWidget,self).__init__()
		self.imagewidget = QImage("myMainWidgetBG2.png")
		mainlyt=QHBoxLayout()
		self.setAutoFillBackground(True)
		self.setLayout(mainlyt)
		mainlyt.setContentsMargins(0,0,0,0)
		mainlyt.setSpacing(5)
		self.itemSet = []
		for item in MainConfigure.secondFloor:
			label_ = midFloorLabel(MainConfigure.secondFloor.index(item),item[0],item[1],item[2])
			mainlyt.addWidget(label_)
			self.itemSet.append(label_)
		mainlyt.addStretch(10)
		self.setFixedHeight(25)
	@classmethod
	def getInstance(cls):
		if cls.instance is None:
			cls.instance = myMidFloorWidget()
		return cls.instance
	def resizeEvent(self,event):
		QLabel.resizeEvent(self,event)
		try:
			pal = QPalette()
			pal.setBrush(QPalette.Window,QBrush(self.imagewidget.scaled(event.size(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)))
			self.setPalette(pal)
		except:
			return
if __name__=='__main__':
	import sys
	app = QApplication(sys.argv)
	win = myMainWidget()
	win.show()
	sys.exit(app.exec_())
