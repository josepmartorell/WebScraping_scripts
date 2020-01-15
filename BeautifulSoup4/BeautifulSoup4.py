import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent': ua.random}


# To extract a tag with a specific class, you can add the class in a form of dictionary, e.g.:
# tags = soup.find_all('a', {"class":"class-name"})

def beautifulSoup4():
    url = 'https://boston.craigslist.org/search/sof'
    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.content, 'lxml')

    result_titles = soup.find_all(class_='result-title')
    for element in result_titles:
        print('Job: ' + element.string)
        print('Url: ' + element['href'])


if __name__ == '__main__':
    beautifulSoup4()
