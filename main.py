import os.path
from ui import UserInterface
from soup import Soup


# give Soup class a variable
soup = Soup()

# checking if movie.txt has data in it
# if it has data do nothing
# if it doesn't have data make_soup() to get data
# if os.path.isfile("movies.txt") and os.path.isdir("./img"):
#     print("img dir and movies.txt exists")
# else:
#     soup.make_soup()
#     print("made soup")

if os.path.isfile("movies.txt") and os.path.isdir("./img"):
    with open("movies.txt", mode="r") as read_data:
        first_line = read_data.readline()
    if ":" in first_line or ")" in first_line:
        pass
    else:
        soup.make_soup()
else:
    soup.make_soup()

# give UserInterface class a variable
ui = UserInterface()

# IDEAS
# TODO 1: Figure out how to bring the window to a close at the end of the list and/or repopulate the movies.txt
# TODO 2: Add a button to start the list from the beginning
