from sqlitectl import sqliteCtl
from mystr import mystr

relt=sqliteCtl.queryDB('usr/userdb/shadow.db','select * from user')
print relt[0]
