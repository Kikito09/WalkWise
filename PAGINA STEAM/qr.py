import qrcode
import qrcode.constants

url= 'https://68jqkt7m-5000.use2.devtunnels.ms/' #CAMBIAR EL LINK POR EL LOCAL HOST

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)  

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("qr_code.png")
print("QR Generado")