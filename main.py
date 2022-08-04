import os.path
from gui import UserInterface
from soup import Soup

soup = Soup()

if os.path.isfile("movies.txt") and os.path.isdir("./img"):
    with open("movies.txt", mode="r") as read_data:
        first_line = read_data.readline()
    if ":" in first_line or ")" in first_line:
        pass
    else:
        soup.make_soup()
else:
    soup.make_soup()

ui = UserInterface()

# IDEAS
# TODO 1: Figure out how to bring the window to a close at the end of the list and/or repopulate the movies.txt
# TODO 2: Add a button to start the list from the beginning
