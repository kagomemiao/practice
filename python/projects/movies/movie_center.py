import media
import fresh_tomatoes

laji = media.Movie("laji",
                   "this is the story line",
                   "image url",
                   "trailer url")
#print(laji.storyline)
#laji.show_trailer()

movies = [laji]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__module__)
