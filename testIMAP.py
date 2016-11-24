from imaplib import *
from download import load

if __name__=='__main__':
	user,pass1 = load.accesspass()
	server = IMAP4_SSL('imap.qq.com')
	server.login(user,pass1)
	rsp,msgs = server.select('INBOX',True)
	import email
	rsp,data = server.fetch(msgs[0],'RFC822')
	for item in data:
		for it2 in item:
			print it2,'\n\n\n'

	with open('file/f{0}.html'.format(ind),'w') as fp:
		fp.write(data[0][1])
	server.close()
	server.logout()
