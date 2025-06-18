from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)


# Finding the upvotes
# If all articles on the page have upvotes, this will work:
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# However, some submissions may not have any upvotes yet.
# This uses a conditional expression to handle cases where there are no upvotes (span is None)
subtexts = soup.find_all(class_="subtext")
article_upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(f"\nTitle Article : {article_texts[largest_index]}")
print(f"Link Article : {article_links[largest_index]}")
print(f"{largest_number} Points")





























# """" Use lxml when you need high performance, full features (like XPath), and full control over XML/HTML.
# Ideal for large projects, advanced scraping, or data integration systems. """
# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.string)
#
# # Use prettify() to displays HTML (or XML) structure neatly and beautifully formatted
# # print(soup.prettify())
#
# # Method .find_all in BeautifulSoup it is used to search for all HTML tags that match certain criteria, then returns them in list form.
# all_anchor_tag = soup.find_all("a")
# # print(all_anchor_tag)
#
# # for tag in all_anchor_tag:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# class_is_heading = soup.find(class_="heading")
# print(class_is_heading)
#
# h3_heading = soup.find(name="h3", class_="heading")
# print(h3_heading)
#
# # .select_one() function in BeautifulSoup is used to retrieve the first HTML element that matches a CSS selector.
# # This is very useful when you want to target an element specifically, such as by class, id, or more complex HTML structure.
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select_one(".heading")
# print(headings)
