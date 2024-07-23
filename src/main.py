import argparse
from randomovie import RandoMovie
from random import choice

randomovie = RandoMovie()
parser = argparse.ArgumentParser(description="Random movie selector")
parser.add_argument('usernames', type=str, nargs='+', help='Usernames to get the watchlist from')

args = parser.parse_args()
selected_username = choice(args.usernames)

page = randomovie.getting_page(selected_username)
watchlist = randomovie.getting_watchlist(page)
randomovie.formatting_movies_names(watchlist)
try:
    print(str(choice(randomovie.selected_movies)).title())
except:
    print("There was an error! The username might be incorrect.")