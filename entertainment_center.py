""" This Module create instances for the Movie Class """

import fresh_tomatoes
import media
toy_story = media.Video("Toy Story", "110 min")
kungfu_panda = media.Video("Kungfu Panda", "105 min")

toy_story = media.Movie("Toy Story", "110 min", "A story of a Toy comes to\
Life", "https://en.wikipedia.org/wiki/File:Toy_Story.jpg", \
"https://www.youtube.com/watch?v=KYz2wyBy3kc") 

kungfu_panda = media.Movie("Kung fu Panda", "105 min", "A story of a Panda\
defeated his enemies", "https://en.wikipedia.org/wiki/File:Kungfupanda.jpg",\
"https://www.youtube.com/watch?v=PXi3Mv6KMzY")

the_dark_knight = media.Movie("The Dark Knight", "124min","A movie about Batman",\
"https://en.wikipedia.org/wiki/File:Dark_Knight.jpg",\
"https://www.youtube.com/watch?v=rGQUKzSDhrg")

movies = [toy_story, kungfu_panda, the_dark_knight]
fresh_tomatoes.open_movies_page(movies)
