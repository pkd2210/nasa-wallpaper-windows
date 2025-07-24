### Imports ###
from datetime import datetime
from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw
import os  # Used for interacting safely with the operating system to access my secret (environmental) variable
import ctypes  # ctypes is used specifically to change the wallpaper
import requests  # Used to get earth images for the background
from datetime import datetime

### Constants ###
imagePath = 'PATHHHH'  # Replace with the DIRECT file path to your wallpaper
SPI_SETDESKWALLPAPER = 20  # Tells Windows API to perform action 20: set desktop wallpaper
url = 'https://cdn.star.nesdis.noaa.gov/GOES19/ABI/FD/GEOCOLOR/10848x10848.jpg'

def setWallpaper(imagePath):
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, os.path.abspath(imagePath).encode(), 0)

def fetchEarthPicture(imagePath):
    response = requests.get(url)
    if response.status_code == 200:
        with open(imagePath, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
fetchEarthPicture(imagePath)
img = Image.open(imagePath)
font = ImageFont.truetype("font.ttf", 1000)
currentDate = datetime.now().strftime("%d/%m - %H:%M")
text = "EARTH AT: " + currentDate
draw = ImageDraw.Draw(img)
textArea = draw.textbbox((0, 0), text, font=font)
textWidth = textArea[2] - textArea[0]
draw.text(((img.width - textWidth) / 2, img.height/2), text, font=font, fill="white", stroke_fill="black", stroke_width=50)
img.save(imagePath) 

setWallpaper(imagePath)