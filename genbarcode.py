import qrcode

serverUrl = ""
loginParam = "?alias="
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

def gen(mem):
    loginUrl = serverUrl + loginParam + mem.alias 
    print(loginUrl)
    qr.add_data(loginUrl)
    qr.make(fit=True)
    img = qr.make_image()
    return img

#img.save("image.jpg")