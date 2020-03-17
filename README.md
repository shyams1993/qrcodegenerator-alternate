# qrcodegenerator-alternate
Alternate python code to generate qr codes using pyqrcode module

ALGORITHM:

1 - import pyqrcode module
2 - create variable link_to_post and save the target URL in that
3 - create the URL as a qrcode by using pyqrcode.create() function
4 - save the image as png in the same folder (if PNG doesn't work, import pypng module)
5 - print the qr code
6 - use url.terminal() to show qr code as a hex version
