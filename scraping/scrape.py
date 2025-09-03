import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')


# print(res)

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# print(soup.body)

# print(soup.body.contents)

# print(soup.find_all('div'))

# print(soup.find(id="score_41391822"))

# print(soup.select('#score_41396501'))

# print(soup.select('.titleline')[2:3])

# heads up! .storylink changed to .titleline
links = soup.select('.titleline')
subtext = soup.select('.subtext')
# heads up! .storylink changed to .titleline
links2 = soup2.select('.titleline ')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sortedOut(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):

    hn = []

    for idx, item in enumerate(links):

        title = item.getText()
        href = links[idx].find('a').get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))

            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sortedOut(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
