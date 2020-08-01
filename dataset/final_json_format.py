import json
import os

directory = 'Images'
destination = 'Images'

fields = ['SELLER_STATE', 'SELLER_ID', 'SELLER_NAME', 'SELLER_ADDRESS', 'SELLER_GSTIN_NUMBER',
          'COUNTRY_OF_ORIGIN', 'CURRENCY', 'DESCRIPTION', 'INVOICE_NUMBER', 'INVOICE_DATE', 'DUE_DATE',
          'TOTAL_INVOICE_AMOUNT_ENTERED_BY_WH_OPERATOR', 'TOTAL_INVOICE_QUANTITY_ENTERED_BY_WH_OPERATOR',
          'TOTAL_TCS_COLLECTED', 'ROUND_OFF_CHARGES', 'PO_NUMBER', 'INVOICE_ITEMS_TOTAL_AMOUNT',
          'INVOICE_ITEMS_TOTAL_QUANTITY', 'BUYER_GSTIN_NUMBER', 'SHIP_TO_ADDRESS']

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
