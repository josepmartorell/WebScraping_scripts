import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'http://www.consumerreports.org/cro/a-to-z-index/products/index.htm'  # input your url here
file_name = 'consumer_reports.txt'  # output file name

user_agent = UserAgent()

page = requests.get(url, headers={'user-agent': user_agent.chrome})
with open(file_name, 'w') as file:
    file.write(page.content.decode('utf-8')) if type(page.content) == bytes else file.write(page.content)

def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data


if __name__ == '__main__':
    read_file()

    soup = BeautifulSoup(read_file(), 'lxml')
    print(soup.prettify())
    products = {}  # product name - key product link - value
    product_names = [div.div.a.span.string for div in soup.find_all('div', class_='entry-letter')]
    product_links = [div.div.a['href'] for div in soup.find_all('div', class_='entry-letter')]
    products = {div.div.a.span.string: div.div.a['href'] for div in soup.find_all('div', class_='entry-letter')}

    for key, value in products.items():
        print(key, '   -->', value)