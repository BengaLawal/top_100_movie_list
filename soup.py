import requests
from bs4 import BeautifulSoup
import os

# Soup class -- has function to make soup depending on the file/dir that exist
#               and function/command for yes button that works in ui


class Soup:
    @staticmethod
    def make_soup():
        """create movie.txt, downloads and append the reversed_list if there is no data"""
        try:
            response = requests.get(
                url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features"
                    "/best-movies-2/")
            response.encoding = "utf-8"
            web_page = response.text
        except requests.exceptions.ConnectionError:
            print("run it again")

        # soup for movie name, number and image link
        soup = BeautifulSoup(web_page, "html.parser")
        all_movies = soup.find_all(name="h3", class_="title")
        all_pictures = soup.find_all(name="img", class_="landscape")

        # list of movie title from soup above
        movie_titles = [_.getText() for _ in all_movies]
        # list of img sources
        pictures_src = [i["src"].split("_/")[1] for i in all_pictures]

        # Save scraped images to file
        img_datas = [requests.get(src).content for src in pictures_src]

        # check if dir exist and/or make dir then add images
        if os.path.isdir("./img"):  # check if dir path is present - returns boolean
            print("img dir exists")
            pass
        else:
            os.mkdir("./img")  # os.mkdir - used to make directory
            for i in range(len(img_datas)):
                try:
                    filename = f"{movie_titles[i].split(')')[1].strip(' ')}.jpg"
                except IndexError:
                    filename = f"The Godfather Part II.jpg"
                with open(f"./img/{filename}", "wb") as handler:
                    handler.write(img_datas[i])
            print("made and added images to img directory")

        # populate txt file with title
        if os.path.isfile("movies.txt"):
            with open("movies.txt", mode="r") as read_data:
                first_line = read_data.readline()
            if ":" in first_line or ")" in first_line:
                pass
            else:
                # wb indicates that the file is opened for writing in binary mode
                with open("movies.txt", mode="wb") as write_data:
                    for movie in movie_titles:
                        write_data.write(f"{movie}\n".encode("utf-8"))
                print("added movie titles to empty movies.txt")
        else:
            with open("movies.txt", mode="wb") as write_data:
                for movie in movie_titles:
                    write_data.write(f"{movie}\n".encode("utf-8"))
            print("made movies.txt and added movie titles")

    @staticmethod
    def yes():
        """removes item from list,
        clears txt file,
        populate txt file with new list"""
        # open movies.txt and save content in content variable
        with open("movies.txt", mode="r") as read_file:
            content = read_file.readlines()
        content.pop(0)
        # w+ -- Open a text file for update (reading and writing), first truncating the file to zero length if it exists
        # or creating the file if it does not exist
        with open("movies.txt", mode="w+") as clean_and_write:
            # clear file using .truncate()
            clean_and_write.truncate()
            # write the new content without the first movie when user clicks yes
            for movie_item in content:
                movie_item.strip("\n")
                clean_and_write.write(f"{movie_item}")
            # print(content)
