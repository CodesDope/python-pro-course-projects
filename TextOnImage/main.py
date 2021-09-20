from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open("sample_img.png")
draw = ImageDraw.Draw(img)

text = input("Enter some text: ")

image_width, image_height = img.size
text_width, text_height = draw.textsize(text)
font = ImageFont.truetype("Roboto-Black.ttf", 100)

draw.text(
    ((image_width - text_width) / 2, (image_height - text_height) / 2),
    text,
    (255, 255, 255),
    font=font,
    anchor="mm",  # https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html
)

img.save("sample_out_img.png")
