from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPalette,QImage,QBrush,QImage
class imageWidget(QImage):
	def __init__(self,localPath):
		super(imageWidget,self).__init__(localPath)
		#self.setAutoFillBackground(True)
	def resizeEvent(self,event):
		QImage.resizeEvent(self,event)
		pal = QPalette()
		pal.setBrush(QPalette.Window,QBrush(self.scaled(event.size(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)))
		self.setPalette(pal)
if __name__=='__main__':
	import sys
        app = QApplication(sys.argv)
        win = imageWidget('myMainWidgetBG.png')
        #print type(win)
	#win.show()
        sys.exit(app.exec_())
