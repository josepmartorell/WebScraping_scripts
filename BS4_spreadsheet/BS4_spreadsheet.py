import requests
from bs4 import BeautifulSoup
from xlsxwriter import Workbook
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    # worksheet.write(row, column, 'otherElement')
    index += 1


def send_attachment(file):
    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    sender_email = "jetro4100@gmail.com"
    receiver_email = "martorelljosep@gmail.com"
    password = input("Type your password and press enter:")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = file  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


# send attachment

send_attachment(fileName)

# close workbook
workbook.close()
