from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,qApp,QTextEdit\
	,QMessageBox,QFileDialog,QDialog,QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5 import Qt
#from PyQt5.QtCore import QString

class myWindow(QMainWindow):
	def __init__(self):
		super(myWindow,self).__init__()
		self.textedit = QTextEdit()
		self.setCentralWidget(self.textedit)
		self.statusBar().showMessage('Ready')
		self.setGeometry(300,300,250,150)
		
		exitact = QAction('&open',self)
		#exitact.setShortcut('Ctrl+Q')
		exitact.setStatusTip('exit application')
		exitact.triggered.connect(self.open)
		
		menubar = self.menuBar()
		menubar.setNativeMenuBar(False)
		filemenu = menubar.addMenu('&File')
		filemenu.addAction(exitact)
		
		toolbar = self.addToolBar('&exit')
		toolbar.addAction(exitact)
		self.setWindowTitle('hello')
	def open(self):
		colordialog = QColorDialog.getColor()
		if colordialog.isValid():
			self.textedit.setStyleSheet('QWidget {background-color:%s}'%colordialog.name())
		'''
		#QMessageBox.information(None,'open','open a file')
		filedialog = QFileDialog(self)
		filedialog.setWindowTitle('open image')
		filedialog.setDirectory('.')
		filedialog.setFilter()
		#filedialog.exec_()
		if filedialog.exec_() == QDialog.Accepted:
			path = fileDialog.selectedFiles()[0]
			QMessageBox.information(None,'path','you selected'+path)
		else:
			QMessageBox.information(None,'path','yuo not selected any file')
		'''
if __name__=='__main__':
	import sys
	app=QApplication(sys.argv)
	win = myWindow()
	win.show()
	sys.exit(app.exec_())
