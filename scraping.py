'''
import PyPDF2

with open('D:\college\starting\SRIP24\data.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    pdf_text = ''
    
    for page_num in range(len(pdf_reader.pages)):
        pdf_text += pdf_reader.pages[page_num].extract_text()

output_file_path = 'D:\college\starting\SRIP24\extracted_text.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(pdf_text)

print("Text extracted from the PDF has been written to:", output_file_path)
'''

import requests
from bs4 import BeautifulSoup

#update link acc to website to scrape
url = "https://indiankanoon.org/doc/18291089/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    webpage_text = soup.get_text()
    #set output file beforehand to print text to
    output_file_path = 'D:\college\starting\SRIP24\supremecourt12-2023to4-2024.txt'
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(webpage_text)

    print("Text has been written to:", output_file_path)

else:
    print("Failed to retrieve:", url)
