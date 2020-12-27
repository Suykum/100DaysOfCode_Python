from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text
soup = BeautifulSoup(movies_page, "html.parser")
title_list = soup.find_all(name="h3", class_="title")
movie_list = [movie.getText() for movie in title_list]
movie_list_final = movie_list[::-1]

with open("must_watch_movies.txt", "a", encoding="utf8") as file:
    for movie in movie_list_final:
        file.write(f"{movie}\n")
