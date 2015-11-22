import media
import fresh_tomatoes

print (media.Movie.__doc__)
#Instantiate of class Movie

inglourious_basterds = media.Movie("Inglourious Basterds","Story of war between France and Germany","http://goo.gl/rz9p8v","https://www.youtube.com/watch?v=Sn35dWgffTk")

in_better_world = media.Movie("In a Better World","The lives of two Danish families cross each other, and an extraordinary but risky friendship comes into bud. But loneliness, frailty and sorrow lie in wait.","http://goo.gl/SHltht","https://www.youtube.com/watch?v=ava0Rn8nrVs")

a_second_chance = media.Movie("A Second Chance","How far would decent human beings be willing to go, when tragedy blurs the line between just and unjust?","http://goo.gl/z01Ydr","https://www.youtube.com/watch?v=yDQ7mX3SA80")

secretary = media.Movie("Secretary","A young woman, recently released from a mental hospital, gets a job as a secretary to a demanding lawyer, where their employer-employee relationship turns into a sexual, sadomasochistic one.","http://goo.gl/TlC6Dr","https://www.youtube.com/watch?v=AFma24S-Uvw")

# Saving list of all movies in "movies"
movies=[inglourious_basterds,in_better_world,a_second_chance,secretary]

# Calling the open_movie_page function from fresh_tomatoes
# class to open up the html containig my favoirte movies
# together with trailer.
fresh_tomatoes.open_movies_page(movies)


