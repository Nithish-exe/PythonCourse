menu_message = "To add a move press 'a', to see your list of movies press 'l', to search for a particular movie click 'ms', to search for an attribute click 'as' to quit the menu click 'q': "
movie_list = []

def add_movie():
   name = input("\n Enter a movie name: ")
   director = input("Enter the director for the movie: ")
   release = input("Enter the release date: ")
   print("\n")

   movie_list.append({"name": name, "director": director, "release": release})

def movie_single(movie):
        print(f"\nTitle: {movie['name']}")
        print(f"Director: {movie['director']}")
        print(f"Release year: {movie['release']}\n")

def movie_multiple():
    for movie in movie_list:
        print(f"\nTitle: {movie['name']}")
        print(f"Director: {movie['director']}")
        print(f"Release year: {movie['release']}\n")

def movie_search():
    search = input("Enter the movie you would like to search for: ")
    for movie in movie_list:
        if search.lower() == movie["name"].lower():
            movie_single(movie)

def attribute_search():
    attribute = input("What characteristic are you looking for: ")
    search = input(f"Which {attribute} are you looking for: ")
    for movie in movie_list:
        if search.lower() == movie[attribute].lower():
            movie_single(movie)
        else:
            print("Invalid Input")

commands = {
"a": add_movie,
"l": movie_multiple,
"ms": movie_search,
"as": attribute_search
}

def app():
    app_state = True
    while app_state == True:
        cmd = input(menu_message)
        if cmd.lower() == "q":
            app_state = False
        elif cmd in commands:
            run = commands[cmd]
            run()
        else:
            print("Invalid Command")

app()