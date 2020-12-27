from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_vote = max(article_upvote)
print(max_vote)
index_of = article_upvote.index(max_vote)
print(index_of)
print(article_texts[index_of])
print(article_links[index_of])
# print(article_upvote)



# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# tags = soup.find_all(name="a")
# for tag in tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
#
#
# company_url = soup.select_one(selector="p a")
# print(company_url)