import qrcode as qr
img = qr.make("https://www.youtube.com/channel/UCMUaDgA3GpSKXLT5Mj_ipbQ")   # <--- give link of what ever you want to make it .make("use to create qr") 
img.save("qr.png") #<-- then save it use .save("")