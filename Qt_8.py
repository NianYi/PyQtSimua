from PyQt5.QtWidgets import QDialog,QCheckBox,QLabel,QPushButton,QLineEdit,QVBoxLayout,QHBoxLayout,QApplication,QScrollArea
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QImage,QPixmap,QPalette
from mydescriptionwidget import myDescriptionWidget
class myDialog(QDialog):
	for_find = pyqtSignal(object,object)
	back_find = pyqtSignal(object,object)
	def __init__(self):
		super(myDialog,self).__init__()
		mainlyt = QHBoxLayout()
		leflyt = QVBoxLayout()
		riglyt = QVBoxLayout()
		uplyt = QHBoxLayout()
		downlyt = QVBoxLayout()
		
		self.find_l = QLabel('Find &what:')
		self.input_ = QLineEdit()
		#self.input_.setEabled(False)
		self.find_l.setBuddy(self.input_)
		self.input_.textChanged.connect(self.valueChange)
		self.find_b = QPushButton('&find')
		self.find_b.setDefault(True)
		self.find_b.setEnabled(False)
		self.close_b = QPushButton('close')
		self.close_b.clicked.connect(self.close)
		self.find_b.clicked.connect(self.find_act)
		self.chk_match = QCheckBox('Case match')
		self.chk_dir = QCheckBox('forword search')
		
		mainlyt.addLayout(leflyt)
		mainlyt.addLayout(riglyt)
		leflyt.addLayout(uplyt)
		leflyt.addLayout(downlyt)
		uplyt.addWidget(self.find_l)
		uplyt.addWidget(self.input_)
		downlyt.addWidget(self.chk_match)
		downlyt.addWidget(self.chk_dir)
		riglyt.addWidget(self.find_b)
		riglyt.addWidget(self.close_b)
		self.setLayout(mainlyt)
	def find_act(self):
		text = self.input_.text()
		print text
		if self.chk_dir.isChecked():
			self.for_find.emit(text,self.chk_match.isChecked())
		else:
			self.back_find.emit(text,self.chk_match.isChecked())
	def valueChange(self,event):
		#print event
		if event:
			self.find_b.setEnabled(True)
if __name__=='__main__':
	import sys
	app = QApplication(sys.argv)
	#win = myDialog()
	#win.show()
	l1 = myDescriptionWidget()
	l1.setMinimumSize(l1.size())
	#image1 = QImage('flagOn.png')
	#l1.setPixmap(QPixmap.fromImage(image1))
	scroll = QScrollArea()
	scroll.setBackgroundRole(QPalette.Dark)
	scroll.setWidget(l1)
	l1.show()
	sys.exit(app.exec_())
