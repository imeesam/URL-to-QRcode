import qrcode as qr
img = qr.make("Enter the link here to convert whatever you wanna convert")  
img.save("qr.png")
