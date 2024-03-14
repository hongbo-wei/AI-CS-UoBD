class Movie:
    id_counter = 0 # Class attribute to track the next available ID for new movie instances
    
    def __init__(self, title, rating) -> None:
        self.tilte = title
        self.rating = rating
        Movie.id_counter += 1 # Increment id_counter for each new instance
        self.id = Movie.id_counter # Assign the new value of id_counter as the unique id for the instance

    
    def info(self):
        """
        Method to print out the movie's ID, title, and rating in a readable format.
        """
        print("Basic information of the movie:")
        print(f"\tMovies's ID: {self.id}")
        print(f"\tTitle: {self.tilte}")
        print(f"\tRating: {self.rating}")


movie_inception = Movie("Inception", 8.8)
movie_matrix = Movie("The Matrix", 8.7)

movie_inception.info()
movie_matrix.info()
