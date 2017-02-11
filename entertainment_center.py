""" This Module create instances for the Movie Class """

import fresh_tomatoes
import media

toy_story = media.Video("Toy Story", "110 min")

kungfu_panda = media.Video("Kungfu Panda", "105 min")

toy_story = media.Movie("Toy Story", "110 min", "A story of a Toy comes\
to Life", "https://goo.gl/d1HmOZ",
"https://www.youtube.com/watch?v=KYz2wyBy3kc")

kungfu_panda = media.Movie("Kung fu Panda", "105 min", "A story\
of a Panda who \defeated his enemies", "https://goo.gl/zLuaDP",
"https://www.youtube.com/watch?v=PXi3Mv6KMzY")

the_dark_knight = media.Movie("The Dark Knight", "124min",
"A movie about Batman","https://goo.gl/m6Rg0K",
"https://www.youtube.com/watch?v=rGQUKzSDhrg")

pride_and_prejudice = media.Movie("Pride and Prejudice-2005", "130 min",
"A romantic comedy in victorian England ","https://goo.gl/92RHSD",
"https://www.youtube.com/watch?v=fJA27Jujzq4")


jane_eyre = media.Movie("Jane Eyre", "130 min", "A mousy governess\
who softens the heart of her employer soon discovers that he's \
hiding a terrible secret.", "https://goo.gl/K8lhSN",
 "https://www.youtube.com/watch?v=e8PLpXvhtlc")

titanic = media.Movie("Titanic", "194 min", "A \
seventeen-year-old aristocrat falls in love \
with a kind but poor artist aboard the luxurious,\
ill-fated R.M.S. Titanic.","https://goo.gl/ZZfkKe", 
"https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

hamlet = media.Movie(
"Hamlet", "184 min", "Shakespeare's most iconic\
work,\ 'Hamlet' explodes with big ideas and is the ultimate story\
of loyalty, love, betrayal, murder and madness.", "https://goo.gl/JAek0x",
"https://www.youtube.com/watch?v=evc_jJNKxPg")

atonement = media.Movie("Atonement", "123 min", 
"Fledgling writer Briony Tallis, as a \
thirteen-year-old, irrevocably changes the course \
of several lives when she  accuses her older sister's \
lover of a crime he did not commit.", "https://goo.gl/0u86VA",
"https://www.youtube.com/watch?v=rkVQwwPrr4c")

movies = [toy_story, kungfu_panda, the_dark_knight,
          pride_and_prejudice, jane_eyre, titanic, hamlet, atonement]
fresh_tomatoes.open_movies_page(movies)
