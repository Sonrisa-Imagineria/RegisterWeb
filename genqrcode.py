import png
import pyqrcode
import io
import os
import base64
loginUrl = 'https://msftewcyep19.azurewebsites.net/login'

def gen(alias):
	memberLoginUrl = loginUrl + alias
	print(memberLoginUrl)
	qrcode = pyqrcode.create(memberLoginUrl)
	#qrcode.png("myQrcode.png", scale=6)
	return qrcode

def genHtml(alias):
	s = io.BytesIO()
	qrBin = gen(alias)
	qrBin.png(s, scale=6)
	encoded = base64.b64encode(s.getvalue()).decode("ascii")
	htmlImg = '''<html><head></head><body><img src="data:image/png;base64,''' + encoded + '''"></body></html>'''
	return htmlImg

# genHtmlImg('all')
