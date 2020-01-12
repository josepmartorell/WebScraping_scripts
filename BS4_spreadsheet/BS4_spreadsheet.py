from xlsxwriter import Workbook  # neccessary import
from bs4 import BeautifulSoup
import requests
from BS4_utils import  send_attachment


index = 0
fileName = 'first-file.xlsx'
url = "http://www.htmlandcssbook.com/code-samples/chapter-04/example.html"


# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')

# Extracting all the <a> tags into a list.
tags = soup.find_all('a')

# Extracting URLs from the attribute href in the <a> tags.
list = []
for tag in tags:
    list.append(tag.get('href'))

# make workbook
workbook = Workbook(fileName)

# add work sheet
worksheet = workbook.add_worksheet()

# write function - parameters - ( row,column, value )
for row in range(len(list)):
    element = list[index]
    worksheet.write(row, 0, element)
    #worksheet.write(row, column, 'otherElement')
    index += 1

# send attachment

send_attachment(fileName)

# close workbook
workbook.close()