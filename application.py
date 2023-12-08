from tkinter import *
from tkinter import ttk
import movie_management
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
    return manager.find_movie("ID", movie_id_entry.get().strip())

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
            if rating_entry.get().strip().upper() == rating:
                break
        else:
            raise Exception
        
        for widget in main_entry_widgets: # Checks that entry widgets are not empty.
            if widget.get() == "":
                raise Exception
        
        manager.add(movie_id_entry.get().strip(), # If passed, entry values are passed to movie_management
                                movie_name_entry.get().strip(),
                                country_name_entry.get().strip(),
                                duration_entry.get().strip(),
                                genre_entry.get().strip(),
                                rating_entry.get().strip().upper())
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
        elif int(duration_entry.get().strip()) < 1: # Movie duration must not be 0 or lower.
            raise Exception

        ratings = ["G", "PG", "14A", "18A", "R"] # Checks that rating is valid.
        for rating in ratings:
            if rating_entry.get().strip().upper() == rating:
                break
        else:
            raise Exception

        for widget in main_entry_widgets: # Checks that entry widgets are not empty.
            if widget.get() == "":
                raise Exception

        manager.update(movie_id_entry.get().strip(), # If passed, entry values are passed to movie_management
                            movie_name_entry.get().strip(),
                            country_name_entry.get().strip(),
                            duration_entry.get().strip(),
                            genre_entry.get().strip(),
                            rating_entry.get().strip().upper())
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

        manager.delete(movie_id_entry.get().strip())
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
    display_box.delete("1.0", "end") # Empties display_box
    for movie in manager.get_movies():
        string = f"{movie.get_movie_id()} - {movie.get_movie_name()} \n" # Prints all movies with ID - Movie_Name
        display_box.insert(INSERT, string)

def find_movie():
    # Attempts to find a movie given the combo_box criteria and the entry.
    # If a valid ID or name is found, Movie is returned.
    # If a valid country, duration, genre, or rating is found, Movies will be printed to display_box.
    # Else: user is told movie with ID or name is not found, or nothing is printed to display_box.
    movie = manager.find_movie(drop_down_list.get(), find_movie_entry.get().strip()) 
    if movie == False:
        find_movie_entry.delete(0, END)
        find_movie_entry.insert(0,"Movie Not Found.")
    elif isinstance(movie, movie_management.movie.Movie):
        empty()
        movie_id_entry.insert(0, movie.get_movie_id())
        movie_name_entry.insert(0, movie.get_movie_name())
        country_name_entry.insert(0, movie.get_country_name())
        duration_entry.insert(0, movie.get_duration())
        genre_entry.insert(0, movie.get_genre())
        rating_entry.insert(0, movie.get_rating().upper())
    elif isinstance(movie, list):
        display_box.delete("1.0", "end")
        if len(movie) == 0:
            display_box.insert(INSERT, "No Movies Found.")
        else:
            movie = sorted(movie, key=lambda m: m.get_movie_id())
            for m in movie:
                string = f"{m.get_movie_id()} - {m.get_movie_name()} \n"
                display_box.insert(INSERT, string)

    

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
rating_guideA_label = Label()
rating_guideB_label = Label()
rating_guideC_label = Label()
rating_guideD_label = Label()
rating_guideE_label = Label()
rating_guideF_label = Label()
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

rating_guideA_label = Label(root, text="Rating Guide")
font(rating_guideA_label)
rating_guideA_label.place(x=0, y=500)

rating_guideB_label = Label(root, text="- G")
font(rating_guideB_label)
rating_guideB_label.place(x=0, y=525)

rating_guideC_label = Label(root, text="- PG")
font(rating_guideC_label)
rating_guideC_label.place(x=0, y=550)

rating_guideD_label = Label(root, text="- 14A")
font(rating_guideD_label)
rating_guideD_label.place(x=0, y=575)

rating_guideE_label = Label(root, text="- 18A")
font(rating_guideE_label)
rating_guideE_label.place(x=0, y=600)

rating_guideF_label = Label(root, text="- R")
font(rating_guideF_label)
rating_guideF_label.place(x=0, y=625)


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
find_movie_button.place(x=610, y=590)

#Drop_Down_List
drop_down_list = ttk.Combobox(root, values=["ID", "Name", "Country Name", "Duration", "Genre", "Rating"])
drop_down_list.place(x=400, y=600)
font(drop_down_list)

main_entry_widgets = [movie_id_entry, movie_name_entry, country_name_entry, 
                            duration_entry, genre_entry, rating_entry]
root.mainloop()
