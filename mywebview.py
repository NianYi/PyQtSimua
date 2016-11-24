from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget,QGridLayout
from mainconfigure import MainConfigure
class myWebView(QWidget):
	instance=None
	def __init__(self):
		super(myWebView,self).__init__()
		self.webview = QWebEngineView()
		mainlyt = QGridLayout()
		mainlyt.addWidget(self.webview)
		mainlyt.setContentsMargins(0,0,0,0)
		self.setLayout(mainlyt)
	@classmethod
	def getInstance(cls):
		if cls.instance is None:
			cls.instance = myWebView()
		return cls.instance
	def update(self):
		if  MainConfigure.currentDescriptionItem != -1:
			try:
				self.webview.setHtml(MainConfigure.content_list[MainConfigure.currentDescriptionItem])
			except:
				self.webview.setHtml('')
		else:
			self.webview.setHtml('')

