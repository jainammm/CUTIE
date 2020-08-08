'''
Run OCR for Training Images
'''

import requests
import json
import os

directory = 'Images'
destination = 'Images'

for filename in os.listdir(directory):
    if filename.endswith(".png"): 
        file_path = directory + '/' + filename

        print(file_path)

        multipart_form_data = {
            'image': (filename, open(file_path, 'rb')),
        }

        url = 'https://clova.ai/ocr/api/general/ko/recognition?ts=1595701921417&s=3894416e780dee0611a09e1a7e4c3830b60b3897'

        response = requests.post(url,
            files=multipart_form_data)

        dest_path = destination + '/' + filename[:-3] + 'json'

        with open(dest_path, 'w') as outfile:
            json.dump(response.json()['annotations'], outfile)