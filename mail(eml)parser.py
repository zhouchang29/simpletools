#coding: utf-8
import os
import email
import email.header
import re
from ast import literal_eval
from bs4 import BeautifulSoup
import datetime

def encodingconv(ustr):
	uresult = str(eval(repr(literal_eval("b'{}'".format(ustr)))), "gbk")
	return uresult

def extract(mailname):
	emaildict = {}
	with open(mailname, 'r') as mailobj:
		m = email.message_from_file(mailobj)
		for bodycheck in m.walk():
			if not bodycheck.is_multipart():
				data = bodycheck.get_payload(decode=True)
				p = str(data)
				soup = BeautifulSoup(p, 'html5lib')
				for datatable in soup.find_all('table'):
					for item in datatable.find_all('td'):
						content = item.get_text()
						ncontent = encodingconv(content)
						if ncontent != ' ':
							tmpkv = ncontent.split('：')
							emaildict[tmpkv[0]] = tmpkv[1]
					break
	return emaildict

mails = [mail for mail in os.listdir() if mail.endswith('.eml')]

havechangelist = []
errorlist = []

for mail in mails:
	try:
		maildict = extract(mail)
		date = ''
		rst = ''
		# date = datetime.datetime.strptime(日期, ("%m/%d/%Y")).strftime('%Y%m%d')
		# rst = re.findall(r"\d+\.?\d*", 带有金额的字符串)[0] + '元'
		if rst not in havechangelist:
			# print('将' + mail + '更改为' + rst +'.eml')
			console = 'ren \"' + mail + '\"  \"' + rst + '.eml\"'
			# print(console)
			# line = os.popen(console).read()
			# print(line)
			havechangelist.append(rst)
		else:
			errorlist.append(rst)
	except Exception:
		errorlist.append(rst)

print(errorlist)