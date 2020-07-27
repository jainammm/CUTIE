import json
import os

directory = 'Images'
destination = 'Images'

i=0

for filename in os.listdir(directory):
    if filename.endswith(".json") and i==0:
        i+=1 
        file_path = directory + '/' + filename
        image_path = filename[:-4] + 'png'

        with open(file_path) as json_file:
            data = json.load(json_file)

            data['fields'] = []

            data['global_attributes'] = {
                "file_id": image_path
            }

        with open('jainam.json', 'w') as outfile:
            json.dump(data, outfile)