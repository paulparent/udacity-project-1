import media
import fresh_tomatoes

# Create new instances of the Movie class for several of my favorite movies
# Arguments: (movie_title, release_date, movie_storyline, poster_image, trailer_youtube, more_link)

big_lebowski = media.Movie("The Big Lebowski", "2008", "\"The Dude\" Lebowski, mistaken for a millionaire Lebowski, seeks restitution for his ruined rug and enlists his bowling buddies to help get it.", "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg", "https://www.youtube.com/watch?v=cd-go0oBF4Y", "http://www.imdb.com/title/tt0118715/")
do_the_right_thing = media.Movie("Do the Right Thing", "1989", "On the hottest day of the year on a street in the Bedford-Stuyvesant section of Brooklyn, everyone's hate and bigotry smolders and builds until it explodes into violence.", "https://upload.wikimedia.org/wikipedia/en/2/22/DO_THE_RIGHT_THING.jpg", "https://youtu.be/KVQHkq3Tk7E", "http://www.imdb.com/title/tt0097216/")
american_hustle = media.Movie("American Hustle", "2013", "A con man, Irving Rosenfeld, along with his seductive partner Sydney Prosser, is forced to work for a wild FBI agent, Richie DiMaso, who pushes them into a world of Jersey powerbrokers and mafia.", "https://upload.wikimedia.org/wikipedia/en/8/85/American_Hustle_2013_poster.jpg", "https://www.youtube.com/watch?v=1KQzDk-u2B0", "http://www.imdb.com/title/tt1800241/")
mad_max_fury_road = media.Movie("Mad Max: Fury Road", "2015", "A woman rebels against a tyrannical ruler in post apocalyptic Austrailia in search for her homeland with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max, who is anything but happy.", "https://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg", "https://www.youtube.com/watch?v=hEJnMQG9ev8", "http://www.imdb.com/title/tt1392190/")
jiro_dreams = media.Movie("Jiro Dreams of Sushi", "2011", "A documentary on 85-year-old sushi master Jiro Ono, his renowned Tokyo restaurant, and his relationship with his son and eventual heir, Yoshikazu.", "https://upload.wikimedia.org/wikipedia/en/4/47/Jiro_sushi_poster.jpg", "https://www.youtube.com/watch?v=M-aGPniFvS0", "http://www.imdb.com/title/tt1772925/")
wall_e = media.Movie("WALL-E", "2008", "In the distant future, a small waste collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.", "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg", "https://www.youtube.com/watch?v=RSarEDlnJI4", "http://www.imdb.com/title/tt0910970/")

# Load all movies into a list, pass the list to the fresh_tomatoes module to created browser-ready output

movies = [big_lebowski, do_the_right_thing, american_hustle, mad_max_fury_road, jiro_dreams, wall_e]
fresh_tomatoes.open_movies_page(movies)
