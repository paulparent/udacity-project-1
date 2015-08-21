class Movie():

  """This class provides a way to define a movie and store its related
      information.

  Attributes:
    title: A string with the title of the movie.
    date: A string with the year of the movie's original release.
    storyline: A string with a short summary of the movie's plot.
    poster_image_url: A string containing a URL for an image file with
      the movie's poster art.
    trailer_youtube_url: A string containing a URL for the movie's trailer.
    more_url: A string containing a URL for more information about the
      movie at IMDB.

  """

  def __init__(self, movie_title, release_date, movie_storyline, poster_image,
               trailer_youtube, more_link):

    """Inits Movie with all key attributes."""

    self.title = movie_title
    self.date = release_date
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube
    self.more_url = more_link
