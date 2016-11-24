#!-*-encoding:utf-8
from PyQt5.QtGui import QColor,QPainter,QFont,QPixmap,QPalette,QIcon,QImage,QBrush
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout,QGridLayout,QLayout,QScrollArea,QSizePolicy,QLineEdit
from PyQt5.QtCore import Qt
from imagebutton import imageButton
from mainconfigure import MainConfigure
class myMainWidget(QLabel):
	def __init__(self):
		super(myMainWidget,self).__init__()
		#self.setStyleSheet("background-color:black")
		self.imagewidget = QImage("myMainWidgetBG.png")
		mainlyt=QGridLayout()
		self.setAutoFillBackground(True)
		self.setLayout(mainlyt)
		uplyt = QHBoxLayout()
		downlyt = QHBoxLayout()
		mainlyt.setContentsMargins(0,0,0,0)
		mainlyt.setSpacing(0)
		mainlyt.addLayout(uplyt,0,0,1,1)
		mainlyt.addLayout(downlyt,1,0,1,1)
		
		uplyt.setContentsMargins(0,0,0,0)
		uplyt.setSpacing(0)
		for item in MainConfigure.firstFloor:
			if item[0] is MainConfigure.FILE:
				uplyt.addStretch(1)
			uplyt.addWidget(imageButton(item[0],item[1]))
		uplyt.addStretch(4)

		imagePath = ['image%s.png'%('10'),None,None,None]
		for item in MainConfigure.secondFloor:
			downlyt.addWidget(imageButton(item[0],item[1],item[2]))
		downlyt.addStretch(10)
		downlyt.setContentsMargins(0,0,0,0)
		downlyt.setSpacing(0)
		self.setFixedHeight(65)
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
