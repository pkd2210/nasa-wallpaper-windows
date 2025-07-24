### Imports ###
from datetime import datetime
import PIL  # Python Imaging Library is used to read and modify the images used
import os  # Used for interacting safely with the operating system to access my secret (environmental) variable
import ctypes  # ctypes is used specifically to change the wallpaper
import requests  # Used to get cat images for the background
import urllib.request  # Used to download an image from a URL

### Constants ###
imagePath = 'C:\\Users\\pkd22\\OneDrive\\Desktop\\Wallpaper\\wallpaper.png'  # Replace with the DIRECT file path to your wallpaper
SPI_SETDESKWALLPAPER = 20  # Tells Windows API to perform action 20: set desktop wallpaper
APIKey = os.getenv("CatAPI")
url = 'https://api.thecatapi.com/v1/images/search'

def setWallpaper(imagePath):
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, os.path.abspath(imagePath).encode(), 0)

def getCurrentHour():
    current_datetime = datetime.now()
    return str(current_datetime.time())[0:2]

# Generate a message to add to the wallpaper based on the current time
hour = int(getCurrentHour())
if hour > 0 and hour < 5:
    message = "Go to sleep!!"
elif hour < 12:
    message = "have a good morning!"
elif hour < 18:
    message = "have a good afternoon!"
else:
    message = "have a good evening!"

def fetchARandomCat(APIKey, imagePath):
    headers = {
        'x-api-key': APIKey
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        catPic = response.json()
        URL = catPic[0].get('url')
        urllib.request.urlretrieve(URL, imagePath)
    else:
        print(response.status_code)

fetchARandomCat(APIKey, imagePath)
setWallpaper(imagePath)