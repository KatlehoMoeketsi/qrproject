import pyqrcode


code = "www.google.co.za"

url = pyqrcode.create(code)

url.svg("myqr.svg", scale=8)



