'''
Convert ocr result for dataloader
'''

import json
import os
from PIL import Image

directory = 'Images'
destination = 'Images'

for filename in os.listdir(directory):
    if filename.endswith(".json"): 
        file_path = directory + '/' + filename
        image_path = file_path[:-4] + 'png'

        image = Image.open(image_path)
        width, height = image.size
        
        print(file_path)

        final_data = {}
        final_data['textbox'] = []
        

        with open(file_path) as json_file:
            data = json.load(json_file)

            for count, ob in enumerate(data):
                bbox = []

                xmin, xmax, ymin, ymax = 0, 0, 0, 0

                if 'boundingPoly' in ob:
                    for box_num, box in enumerate(ob['boundingPoly']):
                        # print(box_num, box)
                        if(box_num == 0):
                            xmin = int(width * float(box[0]))
                            ymin = int(height * float(box[1]))
                            bbox.append(xmin)
                            bbox.append(ymin)
                            
                        if(box_num == 2):
                            xmax = int(width * float(box[0]))
                            ymax = int(height * float(box[1]))
                            bbox.append(xmax)
                            bbox.append(ymax)

                if 'text' in ob:
                    final_data['textbox'].append({
                        'id' : count,
                        'bbox': bbox,
                        'text': ob['text']                    
                    })

            with open(file_path, 'w') as outfile:
                json.dump(final_data, outfile)
            
