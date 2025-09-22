import qrcode

data = "https://www.facebook.com/minhtuan120702"
img = qrcode.make(data)
img.save("qrcode.png")
img.show()
