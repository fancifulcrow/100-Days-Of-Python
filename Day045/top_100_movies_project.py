import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movie_rankings = [movie_title.get_text() for movie_title in soup.find_all(name="h3", class_="title")][::-1]

with open("./top_100_movies.txt", encoding="UTF-8", mode="w") as file:
    for movie_title in movie_rankings:
        file.write(f"{movie_title}\n")
