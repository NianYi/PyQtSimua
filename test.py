import os
import re
def fun(dir):
	li = os.listdir(dir)
	for item in li:
		item = os.path.join(dir,item)
		print 'item: ',item
		if os.path.isdir(item):
			fun(item)
		elif re.match(r'.*?\.pyc$',item):
			os.system('rm {0}'.format(item))

fun(os.path.abspath('.'))
