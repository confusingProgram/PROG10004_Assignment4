from tkinter import *
from movie_management import MovieManagement

def font(widget):
    widget.config(font=('Papyrus', 12))

# Empties main entry widgets.
def empty():
        movie_id_entry.delete(0, END)
        movie_name_entry.delete(0, END)
        country_name_entry.delete(0, END)
        duration_entry.delete(0, END)
        genre_entry.delete(0, END)
        rating_entry.delete(0, END)

# Searches movie_management for movie with ID in movie_id_entry. Returns Movie if exists, False if does not exist.
def search_management():
    return manager.find_movie(0, movie_id_entry.get())

def add_movie():
    try:
        movie = search_management() # Returns either Movie or False
        if movie != False: # Checks if not False, i.e., Movie with ID already exists, reject.
            raise Exception
        elif int(movie_id_entry.get()) < 1: # Movie IDs must not be 0 or lower.
            raise Exception
        elif int(duration_entry.get()) < 1: # Movie duration must not be 0 or lower.
            raise Exception

        ratings = ["G", "PG", "14A", "18A", "R"] # Checks that rating is valid.
        for rating in ratings:
            if rating_entry.get().upper() == rating:
                break
        else:
            raise Exception
        
        for widget in main_entry_widgets: # Checks that entry widgets are not empty.
            if widget.get() == "":
                raise Exception
        
        manager.add(movie_id_entry.get(), # If passed, entry values are passed to movie_management
                                movie_name_entry.get(),
                                country_name_entry.get(),
                                duration_entry.get(),
                                genre_entry.get(),
                                rating_entry.get().upper())
        empty()
        movie_id_entry.insert(0,"Entry Created.")

    except Exception as e:
        empty()
        movie_id_entry.insert(0,"Invalid Entry.")  

def update_movie():
    try:
        movie = search_management() # Returns either Movie, or False. Will throw error if non-int or <1.
        if movie == False: # Checks that ID is 0, i.e., does not exist.
            raise Exception
        elif int(duration_entry.get()) < 1: # Movie duration must not be 0 or lower.
            raise Exception

        ratings = ["G", "PG", "14A", "18A", "R"] # Checks that rating is valid.
        for rating in ratings:
            if rating_entry.get().upper() == rating:
                break
        else:
            raise Exception

        for widget in main_entry_widgets: # Checks that entry widgets are not empty.
            if widget.get() == "":
                raise Exception

        manager.update(movie_id_entry.get(), # If passed, entry values are passed to movie_management
                            movie_name_entry.get(),
                            country_name_entry.get(),
                            duration_entry.get(),
                            genre_entry.get(),
                            rating_entry.get().upper())
        empty()
        movie_id_entry.insert(0,"Entry Updated.")    

    except Exception as e:
        empty()
        movie_id_entry.insert(0,"Invalid Entry.")

def delete_movie():
    try:
        movie = search_management()
        if movie == False: # Checks that movie is False, i.e., does not exist.
            raise Exception

        manager.delete(movie_id_entry.get())
        empty()
        movie_id_entry.insert(0,"Entry Deleted.")

    except Exception as e:
        empty()
        movie_id_entry.insert(0,"Invalid answer.")

def save():
    manager.sort()
    manager.save()
    empty()
    movie_id_entry.insert(0,"Saved.")

def display_all():
    manager.sort()
    display_box.delete("1.0", "end")
    for movie in manager.get_movies():
        string = f"{movie.get_movie_id()} - {movie.get_movie_name()} \n"
        display_box.insert(INSERT, string)

def find_movie():
    movie = manager.find_movie(option.get(), find_movie_entry.get())
    if movie == False:
        find_movie_entry.delete(0, END)
        find_movie_entry.insert(0,"Invalid Entry.")

    empty()
    movie_id_entry.insert(0, movie.get_movie_id())
    movie_name_entry.insert(0, movie.get_movie_name())
    country_name_entry.insert(0, movie.get_country_name())
    duration_entry.insert(0, movie.get_duration())
    genre_entry.insert(0, movie.get_genre())
    rating_entry.insert(0, movie.get_rating())

"""
manager = MovieManagement()
root = Tk()
application_label = Label()
movie_id_label = Label()
movie_id_entry = Entry()
movie_name_label = Label()
movie_name_entry = Entry()
country_name_label = Label()
country_name_entry = Entry()
duration_label = Label()
duration_entry = Entry()
genre_label = Label()
genre_entry = Entry()
rating_label = Label()
rating_entry = Entry()
add_movie_button = Button()
update_movie_button = Button()
delete_movie_button = Button()
save_button = Button()
display_box = Text()
display_all_button = Button()
find_movie_entry = Entry()
find_movie_button = Button()
by_id_radiobutton = Radiobutton()
by_name_radiobutton = Radiobutton()
main_entry_widgets = []
"""

manager = MovieManagement()
root = Tk()
root.geometry("750x750")

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
country_name_label = Label(root, text="Country Name")
font(country_name_label)
country_name_label.place(x=0, y=200)

country_name_entry = Entry(root, text="")
font(country_name_entry)
country_name_entry.place(x=150, y=200)

#Duration
duration_label = Label(root, text="Duration (minutes)")
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

#Update_Movie
update_movie_button = Button(root, text="Update Movie", command=update_movie)
font(update_movie_button)
update_movie_button.place(x=177, y=525)

#Delete_Movie
delete_movie_button = Button(root, text="Delete Movie", command=delete_movie)
font(delete_movie_button)
delete_movie_button.place(x=180, y=575)

#Save
save_button = Button(root, text="Save", command=save)
font(save_button)
save_button.place(x=210, y=625)

#Display_Box
display_box = Text(root, width = 37, height=25, wrap =WORD)
display_box.place(x=400, y=50)

#Display_All
display_all_button = Button(root, text="Display All", command=display_all)
font(display_all_button)
display_all_button.place(x=500, y=475)

#Find_Movie
find_movie_entry = Entry(root, text="")
font(find_movie_entry)
find_movie_entry.place(x=450, y=550)
find_movie_button = Button(root, text="Find Movie", command=find_movie)
font(find_movie_button)
find_movie_button.place(x=575, y=620)

# Radiobuttons
option = IntVar()
by_id_radiobutton = Radiobutton(root, text="By ID", variable=option, value=0)
by_id_radiobutton.place(x=450, y=600)
font(by_id_radiobutton)

by_name_radiobutton = Radiobutton(root, text="By Name", variable=option, value=1)
by_name_radiobutton.place(x=450, y=650)
font(by_name_radiobutton)

main_entry_widgets = [movie_id_entry, movie_name_entry, country_name_entry, 
                            duration_entry, genre_entry, rating_entry]
root.mainloop()
