import pyqrcode
from PIL import Image

link = input("Enter a a link to generate a QR Code: ")
qr_code = pyqrcode.create(link)
qr_code.png('qrcode.png', scale=15)
qr_code.show()
print(f'Returning to main menu.')