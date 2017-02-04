'''Display List of Movies on Website and Show their trailers'''
import media
import fresh_tomatoes

# Movie Objects that you want to show on your website
# Add your own favourite movies object

batman_begins = media.Movie("Batman Begins",
                            "After training with his mentor,Batman begins "
                            "his fight to free crime-ridden Gotham City "
                            "from the corruption that Scarecrow and the "
                            "League of Shadows have cast upon it.",
                            "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=neY2xVmOfUM")


interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through "
                           "a wormhole in space in an attempt to ensure"
                           "humanity's survival.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=3WzHXI5HizQ")


kungfu_panda = media.Movie("Kung Fu Panda",
                           "The Dragon Warrior has to clash against the"
                           "savage Tai Lung as China's fate hangs in balance."
                           "However, the Dragon Warrior mantle is supposedly"
                           "mistaken to be bestowed upon an obese panda"
                           "who is a tyro in martial arts.",
                           "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=NRc-ze7Wrxw")


gravity = media.Movie("Gravity",
                      "Two astronauts work together to survive after an "
                      "accident which leaves them alone in space.",
                      "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=OiTiKOy59o4")


rangde_basanti = media.Movie("Rang De Basanti",
                             "This story is about six friends who help an "
                             "English filmmaker create a documentary about "
                             "Indian freedom struggle. During filming, this "
                             "group of friends learn about those before them "
                             "and importance of fighting for their rights.",
                             "https://upload.wikimedia.org/wikipedia/en/5/5f/RDB_poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=l-BTOTtcGmk")


inside_out = media.Movie("Inside Out",
                         "After young Riley is uprooted from her Midwest life "
                         "and movedto San Francisco, her emotions - Joy, "
                         "Fear, Anger, Disgust and Sadness - conflict on how "
                         "best to navigate a new city, house, and school.",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY")


movies = [
    batman_begins,
    interstellar,
    kungfu_panda,
    gravity,
    rangde_basanti,
    inside_out]

fresh_tomatoes.open_movies_page(movies)