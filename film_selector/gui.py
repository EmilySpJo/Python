from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from get_suggestions_functions import suggestor

############################FUNCTIONS##############################
#plat_selected functions 

def netflixSelected():
    global platform
    platform = "Netflix"

def amazonSelected():
    global platform
    platform = "Amazon Prime"

#media_filter function
def media_filter(event):
     global media
     if(medtyp.get() == "TV Show"):
       media = "TV Show"
     else:
       media = "Movie"
     choose_genre() #triggers the genre function, will ensure it displays the correct options for the chosen platform.

#outputs possible genres to choose from based on selected platforms
def choose_genre():
    global gensel
    gensel['state'] = 'readonly'
    if platform == "Netflix" and media == "TV Show": 
       gensel['values'] = ('TV Dramas', 'Crime TV Shows', 'Reality TV', 'TV Comedies','TV Action & Adventure', 'Kids TV', 'Docuseries', 'Anime Series',
       'Generic TV Shows', 'Romantic TV Shows', 'TV Horror','TV Mysteries', 'British TV Shows', 'TV Sci-Fi & Fantasy','International TV Shows')
    elif platform == "Netflix" and media == "Movie": 
       gensel['values'] = ('Documentaries', 'Family Movies', 'Dramas', 'Comedies','Thrillers', 'Horror Movies', 'Action & Adventure',
       'Stand-Up Comedy', 'Music & Musicals', 'Generic Movies','Romantic Movies', 'Anime Features', 'Sci-Fi & Fantasy','Sports Movies')
    elif platform == "Amazon Prime" and media == "TV Show": 
       gensel['values'] = ('Kids', 'Comedy', 'Anime', 'Generic', 'Action', 'Drama', 'Sports','Western', 'Documentary', 'Unscripted', 'Horror', 'Arts',
       'Special Interest', 'Science Fiction', 'Young Adult Audience','Animation', 'Talk Show', 'Adventure', 'Romance','Music Videos and Concerts')
    else: #platform = amazon and media = movies
       gensel['values'] = ('Comedy', 'Drama', 'Action', 'Documentary', 'Kids', 'Horror', 'Science Fiction', 'Music Videos and Concerts', 'Sports',
       'Faith and Spirituality', 'Special Interest', 'Western', 'Arts', 'Anime', 'Generic', 'Adventure', 'Young Adult Audience', 'Romance',
       'Animation', 'Historical', 'Fantasy', 'Unscripted', 'Suspense')
    gensel.place(relx=0.7, rely=0.75, anchor=E)
    gensel.current(1) #default option
    gensel.bind('<<ComboboxSelected>>', genre_selected)

#genre_selected function
def genre_selected(event):
    global genre
    global gensel
    genre = gensel.get()


#get_suggestions function - calls the data handling functions in the get_suggestions_functions script
def get_suggestions():
    global suggestions
    global media
    global genre
    global platform

    if(platform == "Null" or media == "Null" or genre == "Null"):
      messagebox.showinfo( "Error :(", "You must select a platform, media type and genre for suggestions to be generated!")
    else:
      suggestions = suggestor(platform,media,genre)
      #Display suggestions
      messagebox.showinfo("Suggestion 1", suggestions[0]+"\nDescription: "+ suggestions[1])
      messagebox.showinfo("Suggestion 2", suggestions[2]+"\nDescription: "+ suggestions[3])
      messagebox.showinfo("Suggestion 3", suggestions[4]+"\nDescription: "+ suggestions[5])
      messagebox.showinfo("Suggested titles","THE SUGGESTED TITLES WERE:\n\n"+suggestions[0]+"\n"+ suggestions[2]+"\n"+ suggestions[4])

      # re-set variables
      platform = "Null"
      media = "Null"
      genre = "Null"
      suggestions = []

#############################GUI CODE####################################
#creating the window
window = Tk()
window.title("Content suggestor")
window.geometry('1000x1000')

#Global variables, used to store key information for later use
platform = "Null"
media = "Null"
genre = "Null"
suggestions = []


# background
bg = PhotoImage(file='./images/backgroundResized.png')
canvas1 = Canvas( window, width = 400,height = 400)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")

#Title
canvas1.create_text( 500,75,fill="SteelBlue3",font=("Arial Bold", 50),text="TV show / film suggestor",anchor=CENTER)

#Description of what the system does:
canvas1.create_text( 500,145,fill="white",font=("Arial", 15),text="Select a platform, TV show or Movie and a genre to recieve tailored content suggestions",anchor=CENTER)

#platform prompt:
canvas1.create_text( 500,200,fill="white",font=("Arial", 15), text="Select Amazon Prime or Netflix",anchor=CENTER)

#platform selection

amlogo = PhotoImage(file='./images/amazonLogoResized.png')
Button(canvas1, image=amlogo, command=amazonSelected).place(relx=0.32, rely=0.5, anchor=CENTER)

netlogo = PhotoImage(file='./images/netflixLogoResized.png')
Button(canvas1, image=netlogo, command=netflixSelected).place(relx=0.65, rely=0.5, anchor=CENTER)


#media type prompt
canvas1.create_text(375,500,fill="white",font=("Arial", 15), text="Select Movie or TV Show",anchor=CENTER)

#select media type
medtyp = ttk.Combobox(window)
medtyp['state'] = 'readonly' #stops user altering contents of the drop down box
medtyp['values'] = ("TV Show", "Movie")
medtyp.place(relx=0.3, rely=0.75, anchor=W)
medtyp.current(1) #default option
medtyp.bind('<<ComboboxSelected>>', media_filter)

#genre prompt
canvas1.create_text(625,500,fill="white",font=("Arial", 15), text="Select a genre",anchor=CENTER)

#blank gensel box
gensel = ttk.Combobox(window)
gensel['state'] = 'readonly'
gensel['values'] = ('select_platform/media_type_first')
gensel.current(0) #default option
gensel.place(relx=0.7, rely=0.75, anchor=E)

#button prompt
canvas1.create_text(500,568,fill="white",font=("Arial", 15), text="Press the button to generate your suggestions",anchor=CENTER)

#Button to get suggestions
sugestButton = ttk.Button(window,text="Get suggestions!",command=get_suggestions
)
sugestButton.place(relx=0.5, rely=0.85, anchor=CENTER)

#exit button
exit_button = ttk.Button(window,text='Exit',command=lambda: window.quit())
exit_button.place(relx=0.97, rely=0.05, anchor=E)

canvas1.pack(fill = "both", expand = True)
window.mainloop()