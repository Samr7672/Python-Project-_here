import qrcode as qr
from PIL import Image

qrcode=qr.QRCode(version=1,
                 error_correction=qr.constants.ERROR_CORRECT_H,
                 box_size=20,border=8)
qrcode.add_data("https://github.com/Samr7672")

qrcode.make(fit=True)
img=qrcode.make_image(fill_color="Blue",back_color="Black")
img.save("my github account -v2.png")