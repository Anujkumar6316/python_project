import requests
from bs4 import BeautifulSoup

output = []

def sort_stories_by_votes(HNlist):
    output = sorted(HNlist, key = lambda k:k['points'], reverse=True)

def create_custom_hackerNews(links, votes):
    # ans = []
    for idx, link in enumerate(links):
        url = link.a.get('href')
        title = link.getText()
        vote = votes[idx].select('.score')
        if len(vote):
            points = int(vote[0].text.replace(' points',''))
            if points>100:
                output.append({'title': title, 'link': url, 'points': points})

    return sort_stories_by_votes(output)

url = 'https://news.ycombinator.com/'

# input for number pages for scraping HackerNews
pages = int(input('Enter the number of pages to scrap: '))

res = requests.get(url)

for i in range(pages):
    if i == 0:
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titleline')
        votes = soup.select('.subtext')
        create_custom_hackerNews(links, votes)
        # output.append(create_custom_hackerNews(links, votes))
    else:
        new_url = url + '?p=' + str(i)
        new_res = requests.get(new_url)
        soup = BeautifulSoup(new_res.text, 'html.parser')
        links = soup.select('.titleline')
        votes = soup.select('.subtext')
        create_custom_hackerNews(links, votes)
        # output.extend(create_custom_hackerNews(links, votes))

# print(len(output))
# for i in output:
#     print(i)
with open('hacknews_output.txt', 'w') as f:
    for i,j in enumerate(output):
        f.write(str(i+1) + '\n' + 'Title: '+j['title']+ '\n')
        f.write('Link: ' + j['link'] + '\n')
        f.write('Number of votes: '+str(j['points'])+'\n')

