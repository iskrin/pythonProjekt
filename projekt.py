from PIL import ImageTk
import PIL.Image
import urllib.request
import io
import requests
from tkinter import *


# Define function to fetch images from url and exception handling
def display_image_from_url(url):
    raw_data = urllib.request.urlopen(url).read()
    image = PIL.Image.open(io.BytesIO(raw_data))
    resized_image= image.resize((200,200))
    photo = ImageTk.PhotoImage(resized_image)
    return photo

def fetch_data_from_api(url):
    
    # Send a GET request to the API
    response = requests.get(url)
        
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON format
        json_data = response.json()
        return json_data
    else:
        # If the request was unsuccessful, print an error message
        print("Error:", response.status_code)
        return None
    
    
def savePokemon(url, name, userDirectory):
    try:
      with urllib.request.urlopen(url) as u:
         raw_data = u.read()
    except Exception as e:
      print(f"Error fetching image: {e}")
      return

    
    image = PIL.Image.open(io.BytesIO(raw_data)).resize((400,400)).convert('RGB')
    image.save(userDirectory + "\\" + name)
    







