import sqlite3

class sqliteCtl(object):
	@staticmethod
	def updateDB(dbname,*args):
		conn = sqlite3.connect(dbname)
		cur = conn.cursor()
		for sqlwords in args:
			cur.execute(sqlwords)
		conn.commit()
		cur.close()
		conn.close()
	@staticmethod
	def queryDB(dbname,argu):
		conn = sqlite3.connect(dbname)
		cur = conn.cursor()
		cur.execute(argu)
		relt = cur.fetchall()
		cur.close()
		conn.close()
		return relt
	
