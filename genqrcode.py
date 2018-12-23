import pyqrcode

serverUrl = "https://www.google.com"
loginParam = "?alias="

def gen(alias):
	loginUrl = serverUrl + loginParam + alias
	print(loginUrl)
	qrcode = pyqrcode.create(loginUrl)
	#qrcode.png("myQrcode.png", scale=6)
	#print(qrcode.terminal(quiet_zone=1))
	return qrcode

gen("")
#img.save("image.jpg")
