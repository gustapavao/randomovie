from bs4 import BeautifulSoup as bs
from requests import get

class RandoMovie:
    def __init__(self):
        """
        Initializes a RandoMovie object with default values.
        """
        self.selected_movies = []  

    def getting_page(self, user):
        """
        Retrieves the HTML content of the watchlist page for the given user on Letterboxd.

        Args:
        - user (str): The username of the user on Letterboxd.

        Returns:
        - BeautifulSoup: A BeautifulSoup object containing the parsed HTML content of the page.
        """
        link = f"https://letterboxd.com/{user}/watchlist/"
        page = get(link)
        return bs(page.content, features="html.parser")

    def getting_watchlist(self, page):
        """
        Extracts the movies from the watchlist page.

        Args:
        - page (BeautifulSoup): A BeautifulSoup object containing the parsed HTML content of the page.

        Returns:
        - list: A list of BeautifulSoup Tag objects representing the movies in the watchlist.
        """
        not_watched_movies = page.find_all(attrs={"data-image-width": 125})
        return not_watched_movies

    def formatting_movies_names(self, movies: list):
        """
        Formats the names of the movies and appends them to the selected_movies list.

        Args:
        - movies (list): A list of BeautifulSoup Tag objects representing the movies.

        Returns:
        
        """
        for movie in movies:
            self.selected_movies.append(str(movie["data-film-slug"]).replace("-", " "))
        
#   I've changed some things and need to update
# jsdjoas