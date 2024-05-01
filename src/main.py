from randomovie import RandoMovie

random = RandoMovie()


page = random.getting_page("pavaogus")
watchlist = random.getting_watchlist(page)
random.formatting_movies_names(watchlist)
print(random.selected_movies)