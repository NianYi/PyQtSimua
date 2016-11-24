#encoding:utf-8
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication,QLabel
from PyQt5.QtCore import QUrl,QFile,QFileInfo
import sys,sqlite3
mailpath='/Users/zhuimengbuzhi/Documents/myGithub/Simua/usr/datadb/mail.db'
conn = sqlite3.connect(mailpath)
conn.text_factory = str
cur = conn.cursor()
cur.execute("select * from a907422056")
relt = cur.fetchone()
cur.close()
conn.close()
if __name__=='__main__':

	app = QApplication(sys.argv)
	webview = QWebEngineView()
	#path = 'file://'+QFileInfo('test.html').absolutePath()+'/test.html'
	#webview.load(QUrl('www.baidu.com'))
	with open('test.html','r') as fp:
		webview.setHtml(fp.read())
		webview.show()
	'''	
	try:
		#webview.setHtml(relt[3])
		webview.show()
	except:
		print 'sss'
	'''
	sys.exit(app.exec_())
