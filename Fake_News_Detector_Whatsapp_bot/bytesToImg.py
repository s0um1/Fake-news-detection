from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import urllib.request
import io
import binascii


def bytesToImage(bytesInput):
    r_data = binascii.unhexlify(bytesInput)
    #r_data = "".unhexlify(chr(int(b_data[i:i+2],16)) for i in range(0, len(b_data),2))

    stream = io.BytesIO(r_data)

    img = Image.open(stream)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 14)
    draw.text((0, 220), "This is a test11", (255, 255, 0), font=font)
    draw = ImageDraw.Draw(img)
    img.save("img.png")
