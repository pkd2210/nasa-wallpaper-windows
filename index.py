### Imports ###
from datetime import datetime
import PIL  # Python Imaging Library is used to read and modify the images used
import os  # Used for interacting safely with the operating system to access my secret (environmental) variable
import ctypes  # ctypes is used specifically to change the wallpaper
import requests  # Used to get earth images for the background

### Constants ###
imagePath = 'C:\\Users\\pkd22\\OneDrive\\Desktop\\Wallpaper\\wallpaper.png'  # Replace with the DIRECT file path to your wallpaper
SPI_SETDESKWALLPAPER = 20  # Tells Windows API to perform action 20: set desktop wallpaper
APIKey = os.getenv("API-KEY")
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
setWallpaper(imagePath)