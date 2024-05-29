'''
import PyPDF2

# Open the PDF file in binary mode
with open('D:\college\starting\SRIP24\data.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Initialize an empty string to store the extracted text
    pdf_text = ''
    
    # Loop through each page of the PDF and extract text
    for page_num in range(len(pdf_reader.pages)):
        pdf_text += pdf_reader.pages[page_num].extract_text()

# Write the extracted text to a new text file
output_file_path = 'D:\college\starting\SRIP24\extracted_text.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(pdf_text)

print("Text extracted from the PDF has been written to:", output_file_path)
'''

import requests
from bs4 import BeautifulSoup

#update link acc to website to scrape
url = "https://indiankanoon.org/doc/28682724/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    webpage_text = soup.get_text()
    #set output file beforehand to print text to
    output_file_path = "D:\college\starting\SRIP24\MadanBhargavAndSons\doc.txt"
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(webpage_text)

    print("Text has been written to:", output_file_path)

else:
    print("Failed to retrieve:", url)
