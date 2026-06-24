#Intialise Windows
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.title("Quizzlet")
root.geometry("430x932")
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
    image = Image.open(file="/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Quizzlet Login 1.png")
    image = image.resize((430, 932))

    bg_image = ImageTk.PhotoImage(image)



    bg_label = tk.Label(frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = tk.Label(frame, text="Home Page", font=("Arial", 24, "bold"))
    title.place(x=150, y=50)

page_switch(home_page)  # Display the home page initially
root.mainloop()



