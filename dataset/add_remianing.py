'''
Util to add remaining fields to the json data
'''

import json
import os

directory = 'Images'
destination = 'Images'

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        fields = ['SELLER_STATE', 'SELLER_ID', 'SELLER_NAME', 'SELLER_ADDRESS', 'SELLER_GSTIN_NUMBER',
                  'COUNTRY_OF_ORIGIN', 'CURRENCY', 'DESCRIPTION', 'INVOICE_NUMBER', 'INVOICE_DATE', 'DUE_DATE',
                  'TOTAL_INVOICE_AMOUNT_ENTERED_BY_WH_OPERATOR', 'PO_NUMBER', 'BUYER_GSTIN_NUMBER', 'SHIP_TO_ADDRESS',
                  'PRODUCT_ID', 'HSN', 'TITLE', 'QUANTITY', 'UNIT_PRICE', 'DISCOUNT_PERCENT', 'SGST_PERCENT',
                  'CGST_PERCENT', 'IGST_PERCENT', 'TOTAL_AMOUNT']

        file_path = directory + '/' + filename
        image_path = filename[:-4] + 'png'

        with open(file_path) as json_file:
            data = json.load(json_file)

            for f in data['fields']:
                fields.remove(f['field_name'])

            for remaining_fields in fields:
                data['fields'].append(
                    {
                        "field_name": remaining_fields,
                        "value_id": [],
                        "value_text": [],
                        "key_id": [],
                        "key_text": []
                    }
                )

        with open(file_path, 'w') as outfile:
            json.dump(data, outfile)