import pyqrcode									            #import pyqrcode module
link_to_post = "https://www.google.com"			#create variable link_to_post and save the target URL in that
url = pyqrcode.create(link_to_post)				  #create the URL as a qrcode by using pyqrcode.create() function
url.png('url.png', scale=8)						      #save the image as png in the same folder (if PNG doesn't work, import pypng module)
print("Printing QR code")						        #print the qr code
print(url.terminal())							          #use url.terminal() to show qr code as a hex version
