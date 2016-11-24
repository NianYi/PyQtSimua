#!/usr/bin/env python
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import sqlite3
import ConfigParser
#-*-config file
config = ConfigParser.ConfigParser()
config.readfp(open('etc/pathcfg.ini','r'))
userdbPath = config.get("global","userdbpath")

class rsa(object):
	def __init__(self):
		pass

	@classmethod
	def generate(cls):
		random_generator = Random.new().read
		secret = RSA.generate(1024,random_generator)
		private_pem = secret.exportKey()
		public_pem = secret.publickey().exportKey()
		return public_pem,private_pem
	@classmethod
	def encrypt(cls,key,oriString):
		'''
		conn = sqlite3.connect(userdbPath+'shadow.db')
		cursor = conn.cursor()
		cursor.execute(select_current_publicpem)
		key = cursor.fetchone()[0]
		cursor.close()
		conn.close()
		'''
		rsakey  =RSA.importKey(key)
		cipher = Cipher_pkcs1_v1_5.new(rsakey)
		cipher_text = base64.b64encode(cipher.encrypt(oriString.decode('utf8').encode('utf8')))
		return cipher_text
	@classmethod
	def decrypt(cls,key,secString):
		'''
		conn = sqlite3.connect(userdbPath+'shadow.db')
		cursor = conn.cursor()
		cursor.execute(select_current_privatepem)
		key = cursor.fetchone()[0]
		cursor.close()
		conn.close()
		'''
		rsakey  =RSA.importKey(key)
		cipher = Cipher_pkcs1_v1_5.new(rsakey)
		ori_text = cipher.decrypt(base64.b64decode(secString),Random.new().read)
		return ori_text

