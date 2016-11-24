from PyQt5.QtWidgets import QLabel,QApplication
from PyQt5.QtGui import QPainter,QColor,QFont,QFontMetrics
from PyQt5.QtCore import Qt
class TextLabel(QLabel):
	def __init__(self,mxWidth,text,lines):
		super(TextLabel,self).__init__()
		text = self.getElideText(text,mxWidth,lines)
		doubleLine=2
		self.setWordWrap(lines is doubleLine)
		self.setAlignment(Qt.AlignLeft)
		self.setText(text)
		self.setMargin(0)
	def getElideText(self,text,mxWidth,lines):
		std_height = TextLabel.getTextHeight(self.font()) * lines
		errorValue = 0
		if lines > 1:
			errorValue = 50
		self.resize(mxWidth,std_height)
		width = TextLabel.getTextLength(text,self.font())
		mxWidth = mxWidth*lines
		if width > mxWidth:
			text = TextLabel.getElidedText(self.font(),text,Qt.ElideRight,mxWidth-errorValue)
		return text

	@staticmethod
	def getElidedText(font,text,elideAlign,mxWidth):
		return QFontMetrics(font).elidedText(text,elideAlign,mxWidth)
	@staticmethod
	def getTextLength(text,font):
		return QFontMetrics(font).width(text)+5

	@staticmethod
	def getTextHeight(font):
		return QFontMetrics(font).height()

'''
import sys
app=QApplication(sys.argv)
mainwin = TextLabel(20,'helloassasasasasasas',2)
mainwin.show()
sys.exit(app.exec_())
'''
