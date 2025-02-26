# -*- coding: utf-8 -*-
"""Untitled84.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RXTEao7m-LCRCZbivOZwF_cATCmasrer
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_cat = cv2.cvtColor(cv2.imread('https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fimages%2Fanimals%2Fcat&psig=AOvVaw2EWO8xZiIvw538ggiE5rGk&ust=1695728667975000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOioqNHXxYEDFQAAAAAdAAAAABAE'), cv2.COLOR_BGR2RGB)
img_dog = cv2.cvtColor(cv2.imread('https://www.freepnglogos.com/uploads/dog-png/bow-wow-gourmet-dog-treats-are-healthy-natural-low-4.png'), cv2.COLOR_BGR2RGB)

import cv2
import numpy as np
import requests
from io import BytesIO

# URL of the image
cat_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fimages%2Fanimals%2Fcat&psig=AOvVaw2EWO8xZiIvw538ggiE5rGk&ust=1695728667975000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOioqNHXxYEDFQAAAAAdAAAAABAE'

# Fetch the image data from the URL
response = requests.get(cat_url)
img_bytes = BytesIO(response.content)

# Read the image using OpenCV
img_cat = cv2.imdecode(np.frombuffer(img_bytes.read(), np.uint8), cv2.IMREAD_COLOR)
img_cat = cv2.cvtColor(img_cat, cv2.COLOR_BGR2RGB)

# Now you can work with img_cat

import cv2
import numpy as np
import requests
from io import BytesIO

# URL of the image
cat_url = '/content/sajad-nori-s1puI2BWQzQ-unsplash.jpg'

# Fetch the image data from the URL
response = requests.get(cat_url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    img_bytes = BytesIO(response.content)

    # Read the image using OpenCV
    img_cat = cv2.imdecode(np.frombuffer(img_bytes.read(), np.uint8), cv2.IMREAD_COLOR)

    if img_cat is not None:
        img_cat = cv2.cvtColor(img_cat, cv2.COLOR_BGR2RGB)
        # Now you can work with img_cat
    else:
        print("Failed to decode the image.")
else:
    print("Failed to fetch the image. Status code:", response.status_code)

import cv2

# Provide the path to the local image file
image_path = '/content/sajad-nori-s1puI2BWQzQ-unsplash.jpg'

# Read the image using OpenCV
img_cat = cv2.imread(image_path)

# Check if the image was read successfully
if img_cat is not None:
    img_cat = cv2.cvtColor(img_cat, cv2.COLOR_BGR2RGB)
    # Now you can work with img_cat
else:
    print("Failed to read the image.")
img_cat