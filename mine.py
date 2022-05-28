from urllib import request
url = "https://www.foxnews.com/us"
html = request.urlopen(url).read().decode('utf8')
html[:60]

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
article = soup.find('main')

content = article.div.p.a.text
title = article.div.h2.a.text
place = article.div.header.span.a.text
published= article.div.span.text

mini_articles = soup.find('div',class_='collection collection-spotlight collection-spotlight-cards')

#print(article.prettify())

print(f"FROM = {place}")

print()

print(f"TITLE = {title}")

print()

print(f"CONTENT = {content}")

print()

#print(mini_articles.prettify())
print(published)


#print(content)