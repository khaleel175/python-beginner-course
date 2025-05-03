movies = {'harry potter':'10am',
          'avengers':'12pm',
          'spiderman':'2pm',
          'batman':'4pm',
          'superman':'6pm'
          }

print("WELCOME!!!!,we are casting the following movies:")
for key in movies:
    print(key)

movie = input("enter the show you wanna watch:\n").lower()

showtime = movies.get(movie)

if showtime == None:
    print("apologies,we aint playin that shit!")

else:
    print(f"{movie} is playing at {showtime}")