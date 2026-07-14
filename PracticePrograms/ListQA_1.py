#WAP to ask the user to enter names of their 3 favorite movies & store them in a list?

#Creating an empty list to store movies
movies = []

movie1 = str(input("Enter 1st fav movie name:"))
movies.append(movie1)

movie2 = str(input("Enter 2nd fav movie name:"))
movies.append(movie2)

movie3 = str(input("Enter 3rd fav movie name:"))
movies.append(movie3)

print("Users 3 favorite movies are: ", movies)

