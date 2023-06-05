import openai
import requests
from io import BytesIO
from dotenv import dotenv_values

secrets = dotenv_values(".env")


# setting up openai api key.
openai.api_key = secrets['API_KEY']


# Define prompt
prompt = "donkey on Mars growing wheat"

# call the API to generate the image
response = openai.Image.create(
    prompt = prompt,
    n=1,
    size="256x256")

# Parse the response to get the image data
image_url = response['data'][0]['url']
  # requests.get() make a http get request. It return a Response object with the response for the request.
image_response = requests.get(image_url)
  # creating a 'in-memory byte buffer that behaves like a file object'. It allows you to read from or write to a stream of bytes using the same interface as a file object, but without the need for a physical file.
image_data = BytesIO(image_response.content)

# downloading the image file
with open('image.jpg','wb') as f:
    f.write(image_data.getbuffer())
