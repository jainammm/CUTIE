import json
import os

directory = 'Images'
destination = 'Images'

fields = ['Seller State', 'Seller ID', 'Seller Name', 'Seller Address', 'Seller GSTIN Number',
          'Country of Origin', 'Currency', 'Description', 'Invoice Number', 'Invoice Date', 'Due Date',
          'Total Invoice amount entered by WH operator', 'Total Invoice Quantity entered by WH operator',
          'Total TCS Collected', 'Round Off Charges', 'PO Number', 'Invoice Items Total Amount',
          'Invoice Items total quantity', 'Buyer GSTIN Number', 'Ship to Address']

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        file_path = directory + '/' + filename
        image_path = filename[:-4] + 'png'

        with open(file_path) as json_file:
            data = json.load(json_file)

            data['fields'] = []

            for f in fields:
                data['fields'].append(
                    {
                        "field_name": f.upper().replace(' ', '_'),
                        "value_id": [],
                        "value_text": [],
                        "key_id": [],
                        "key_text": []
                    }
                )

            data['global_attributes'] = {
                "file_id": image_path
            }

        with open(file_path, 'w') as outfile:
            json.dump(data, outfile)
