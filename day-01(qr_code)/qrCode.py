import qrcode as qr
from PIL import Image

# some of the methods of qrcode are: make, save(create's a png)
img = qr.make('https://google.com')
img.save('google.png')

# now here we will change the style of the qr png for that we will use QRCode
newQR = qr.QRCode(version = 1,
                  error_correction = qr.constants.ERROR_CORRECT_H,
                  box_size = 10, border = 4,)

newQR.add_data('https://google.com')
newQR.make(fit = True)
img = newQR.make_image(fill_color = 'blue', back_color = 'white')
img.save('new_google_QR.png')