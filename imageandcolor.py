from PyQt5.QtGui import QPalette,QColor
class ImageAndColor(object):
	def __init__(self):
		super(ImageAndColor,self).__init__()
	@staticmethod
	def getQPalette(background):
		pal = QPalette()
		if isinstance(background,QColor):
			pal.setColor(QPalette.Background,background)
		else:
			pal.setBrush(QPalette.Background,background)
		return pal
