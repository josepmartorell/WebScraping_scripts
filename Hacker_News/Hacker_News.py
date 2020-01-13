import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# Background on user-agents
ua = UserAgent()
header = {'user-agent':ua.firefox}

def get_front_page():
    target = "https://news.ycombinator.com"
    front_page = requests.get(target, headers=header, timeout=3)
    print(header)
    if not front_page.ok:
        raise RuntimeError("Can't access hacker news, you should go outside")
    news_soup = BeautifulSoup(front_page.text, "lxml")
    return news_soup


def find_interesting_links(soup):
    items = soup.findAll('td', {'align': 'right', 'class': 'title'})
    links = []
    for i in items:
        try:
            siblings = list(i.next_siblings)
            post_id = siblings[1].find('a')['id']
            link = siblings[2].find('a')['href']
            title = siblings[2].text
            links.append({'link': link, 'title': title, 'post_id': post_id})
        except Exception as e:
            pass

    return links


if __name__ == '__main__':
    soup = get_front_page()
    results = find_interesting_links(soup)
    for r in results:
        if r is not None:
            print(r['link'] + " " + (r['title']))