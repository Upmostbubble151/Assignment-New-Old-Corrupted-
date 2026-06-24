#Intialise Windows
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.title("Quizzlet")
root.geometry("420x832")
root.resizable(False, False)

#Main Page Widgets



#Switching Pages
current_page = None #Acts as a changable variable which is us

def page_switch (page_function): #Defines Variable that changes to the different Pages. page_function is the page you want to switch
    global current_page #Changes variable outside the def
    if current_page is not None:
        current_page.destroy() #removes current page
    
    current_page = tk.Frame(root) #Creates a new frame 
    current_page.pack(fill="both", expand=True) #New frame fills the Next page
    page_function(current_page) #displays the new page

def home_page(frame):
    image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Quizzlet Login 1.png") #Import the Background for The home page
    image = image.resize((430, 932)) # Resize the image to be correct

    bg_image = ImageTk.PhotoImage(image) # Store the Image
    
    
    bg_label = tk.Label(frame, image=bg_image)

    canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.bg_image = bg_image  
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    #Widget 
    user_entry = tk.Entry(frame, width=30, font=("Arial", 14))
    user_entry.place(x=110, y=500)

    title = tk.Label(frame, text="Home Page", font=("Arial", 24, "bold"))
    title.place(x=150, y=50)

page_switch(home_page)  # Display the home page initially
root.mainloop()



