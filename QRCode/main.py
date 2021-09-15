import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2
)

qr.add_data("https://pro.codesdope.com")

img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img.save("qr02.png")
