'''
Converts pdf to images
'''

from pdf2image import convert_from_path
import os

directory = 'GRiD_Sample Invoices II'
destination = 'Images'

for filename in os.listdir(directory):
    if filename.endswith(".pdf"): 
        pages = convert_from_path(directory + '/' + filename)
        print(filename)

        for count, page in enumerate(pages):
            page.save(destination + '/' + filename[:-4] + '_' + str(count)+'.png', 'PNG')