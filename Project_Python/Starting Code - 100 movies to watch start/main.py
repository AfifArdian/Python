import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movie_titles = [name.getText() for name in reversed(soup.find_all(name="h3", class_="title"))]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movies in movie_titles:
        file.write(f"{movies}\n")