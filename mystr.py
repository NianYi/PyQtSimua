#!/usr/bin/env python
import re
class mystr(object):
	def __init__(self):
		pass
	@classmethod
	def mailname2tablename(cls,tablename):
		return 'a'+(''.join(re.split(r'[^0-9a-zA-Z_]',tablename)))
