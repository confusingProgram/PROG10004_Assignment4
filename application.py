from tkinter import *
from tkinter import ttk
from tkinter import Tk, font


class Application:
    def run():
        pass
    pass

root = Tk()
root.geometry("750x750")

def font(label):
    label.config(font=('Papyrus', 12))

def add_movie():
    try:
        id = int(movie_id_entry)
        movie_id_entry.delete(0, END)
        movie_name_entry.delete(0, END)
        country_name_entry.delete(0, END)
        duration_entry.delete(0, END)
        genre_entry.delete(0, END)
        rating_entry.delete(0, END)
    except Exception as e:
        movie_id_entry.delete(0, END)
        movie_id_entry.insert(0,"Invalid answer.")
    pass

def display_all():
    display_box.insert(INSERT, "Apple \n")

# Application label
application_label = Label(root, text = "Cinema Collection")
application_label.config(font=('Papyrus', 20))
application_label.place(x=275, y=0)

#Movie_ID
movie_id_label = Label(root, text="Movie ID")
font(movie_id_label)
movie_id_label.place(x=0, y=50)

movie_id_entry = Entry(root, text="")
font(movie_id_entry)
movie_id_entry.place(x=150, y=50)

#Movie_Name
movie_name_label = Label(root, text="Movie Name")
font(movie_name_label)
movie_name_label.place(x=0, y=125)

movie_name_entry = Entry(root, text="")
font(movie_name_entry)
movie_name_entry.place(x=150, y=125)

#Country_Name
country_name_label = Label(root, text="Country_Name")
font(country_name_label)
country_name_label.place(x=0, y=200)

country_name_entry = Entry(root, text="")
font(country_name_entry)
country_name_entry.place(x=150, y=200)

#Duration
duration_label = Label(root, text="Duration")
font(duration_label)
duration_label.place(x=0, y=275)

duration_entry = Entry(root, text="")
font(duration_entry)
duration_entry.place(x=150, y=275)

#Genre
genre_label = Label(root, text="Genre")
font(genre_label)
genre_label.place(x=0, y=350)

genre_entry = Entry(root, text="")
font(genre_entry)
genre_entry.place(x=150, y=350)

#Rating
rating_label = Label(root, text="Rating")
font(rating_label)
rating_label.place(x=0, y=425)

rating_entry = Entry(root, text="")
font(rating_entry)
rating_entry.place(x=150, y=425)

#Add_Movie_Button
add_movie_button = Button(root, text="Add Movie", command=add_movie)
font(add_movie_button)
add_movie_button.place(x=190, y=475)

#Display_All
display_all_button = Button(root, text="Display All", command=display_all)
font(display_all_button)
display_all_button.place(x=500, y=475)

#Display_Box
display_box = Text(root, width = 37, height=25, wrap = WORD)
display_box.place(x=400, y=50)


root.mainloop()