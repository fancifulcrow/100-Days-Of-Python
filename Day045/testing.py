from bs4 import BeautifulSoup
import requests

# for a different way of parsing websites
# import lxml

with open("./website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser") # lxml for lxml

print(soup.title) # title of the website
# soup.title.name is the HTML tag of the title
# soup.title.string is the string within the tag

print(soup.prettify()) # prints the html formatted

print(soup.a) # gets the first anchor tag in the website


############### Finding and Selecting Particular Elements ###############
all_anchor_tags = soup.findAll(name="a") # Finds all with the anchor tag

print(all_anchor_tags)

for tag in all_anchor_tags:
    print(f"{tag.getText()} and the link is: {tag.get('href')}")

heading = soup.find(name="h1", id="name") # Finds just the first item with the h1 tag
print(heading.getText())

h3_heading = soup.find(name="h3", class_="heading")
print(h3_heading.get("class"))

# Finding an element within another element
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)


############### Scraping a Live Website ###############
response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
yc_webpage = response.text

yc_soup = BeautifulSoup(yc_webpage, "html.parser")
# Getting the Headline for the first post
article_tags = yc_soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article_tag in article_tags:
    article_text = article_tag.getText()
    article_texts.append(article_text)

    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes =[int(score.getText().split()[0]) for score in yc_soup.findAll(name="span", class_="score")] # Recall list Comprehension

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_upvotes = max(article_upvotes)
index_of_largest_upvotes = article_upvotes.index(largest_upvotes)

print(f"Article : \"{article_texts[index_of_largest_upvotes]}\" with the link: {article_links[index_of_largest_upvotes]} has the highest upvotes of {largest_upvotes} points at this moment.")

# Webstites have their own robots.txt to show what is allowed when scraping