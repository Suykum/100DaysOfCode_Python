from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text
soup = BeautifulSoup(movies_page, "html.parser")
title_list = soup.find_all(name="h3", class_="title")
movie_list = [movie.getText().split(")") for movie in title_list]
for movie in movie_list:
    if len(movie) < 2:
        movie_list.remove(movie)
movie_list_final = [movie[1] for movie in movie_list]
with open("must_watch_movies.txt", "a", encoding="utf8") as file:
    for n in range(0, len(movie_list_final) - 1):
        file.write(f"{n + 1}{movie_list_final[n]}\n")
