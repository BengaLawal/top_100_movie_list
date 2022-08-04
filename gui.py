from tkinter import *
from soup import *
from PIL import ImageTk, Image

# UserInterface class -- deals with the window and a function to change a label & image


class UserInterface(Soup):
    def __init__(self):
        super().__init__()
        self.window = Tk()
        self.window.title("Top 100 Movies")
        self.window.config(padx=200, pady=100, bg="#f7f5dd")

        # left canvas that containing img of movie
        with open("movies.txt", mode="r") as movies:
            try:
                first_line = movies.readline().split(")")[1].strip(" ").strip("\n")
            except IndexError:
                first_line = "The Godfather Part II"
        self.canvas = Canvas(height=510, width=910, highlightthickness=0)
        self.movie_img = ImageTk.PhotoImage(Image.open(f"./img/{first_line}.jpg"))
        self.image_on_canvas = self.canvas.create_image(455, 255, image=self.movie_img)
        self.canvas.grid(column=0, row=0, rowspan=3, )

        # have you watched this label
        self.watched_label = Label(text="Have you watched this?", bg="#f7f5dd", font=("arial", 20, "bold"))
        self.watched_label.grid(column=1, row=0, columnspan=2, pady=50)

        # when the code is run the title label will immediately display the first line in the movies txt
        with open("movies.txt", mode="r") as movies:
            first_line = movies.readline()
        self.title_label = Label(text=f"{first_line}", bg="#f7f5dd", font=("arial", 20, "bold"), wraplength=500,
                                 justify="center", width=30)
        self.title_label.grid(column=1, row=1, columnspan=2, pady=50)

        # lambda is used to give a button more than 1 command/function
        self.yes_button = Button(text="Yes", highlightthickness=0,
                                 command=lambda: [self.yes(), self.next_img_and_text()])
        self.yes_button.grid(column=1, row=2, columnspan=2)

        self.window.mainloop()

    def next_img_and_text(self):
        """Clicking the button changes the movie title and img"""
        with open("movies.txt", mode="r") as movies:
            first_line = movies.readline()
            try:
                first_line_img = first_line.split(")")[1].strip(" ").strip("\n")
            # movies no 12 gives IndexError because it has ':' instead of ')'
            except IndexError:
                first_line_img = "The Godfather Part II"
        self.title_label.config(text=first_line)
        self.movie_img = ImageTk.PhotoImage(Image.open(f"./img/{first_line_img}.jpg"))
        self.canvas.itemconfig(self.image_on_canvas, image=self.movie_img)

        if first_line == " ":
            self.title_label.config(text="You have finished the list\nCongratulation")
            self.movie_img = ImageTk.PhotoImage(Image.open(f"./images/img.png"))
            self.canvas.itemconfig(self.image_on_canvas, image=self.movie_img)
            self.yes_button = Button(text="Yes", highlightthickness=0,
                                     command=lambda: [self.yes(), self.next_img_and_text()], state=DISABLED)
            self.make_soup()
