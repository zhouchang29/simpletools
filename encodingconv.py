def encodingconv(ustr):
	result = ustr.encode('raw_unicode_escape')
	return ustr.encode("latin1").decode("gbk") 

text = '\xb7\xd1\xd3\xc3\xd7\xdc\xc0\xc0\xa3\xba'

print(encodingconv(text))