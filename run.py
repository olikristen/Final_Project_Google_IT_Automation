#!/usr/bin/env python3

import os
import requests
import re

"""{"name": "Test Fruit", "weight": 100, 
"description": "This is the description of my test fruit", 
"image_name": "icon.sheet.png"}"""

desc_path = "supplier-data/descriptions/"
img_path = "supplier-data/images/"

jpeg_images = sorted([image_name for image_name in os.listdir(img_path) if '.jpeg' in image_name])

list_content = []
img_counter = 0

for file in sorted(os.listdir(desc_path)):

    format = ['name', 'weight', 'description']

    with open(desc_path + file, "r") as txtfile:
        data = {}

        contents = txtfile.read().split("\n")[0:3]  # read the first three lines to remove empty space
        contents[1] = int(re.sub('\D', '', contents[1]))  # remove lbs from weight to get digits only

        counter = 0

        """ Feed the dictionary with name, weight, description"""

        for c in contents:
            data[format[counter]] = c
            counter += 1

        # add the image name to the dict

        data['image_name'] = jpeg_images[img_counter]
        list_content.append(data)
        img_counter += 1

for x in list_content:
    resp = requests.post('http://127.0.0.1:80/fruits/', json=x)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))



