import sys
print(sys.executable)

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
#adding mback button
def page_switch (page_function): #Defines Variable that changes to the different Pages. page_function is the page you want to switch
    global current_page #Changes variable outside the def
    if current_page is not None:
        current_page.destroy() #removes current page
    
    current_page = tk.Frame(root) #Creates a new frame 
    current_page.pack(fill="both", expand=True) #New frame fills the Next page
    page_function(current_page) #displays the new page

def home_page(frame):
    image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Login Page Quizzlet.png") #Import the Background for The home page
    image = image.resize((430, 932)) # Resize the image to be correct

    bg_image = ImageTk.PhotoImage(image) # Store the Image
    
    
    bg_label = tk.Label(frame, image=bg_image)

    canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.bg_image = bg_image  
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    #Widget 
    user_entry = tk.Entry(frame, width=30, bd=0, highlightthickness=0, relief = "flat", bg="white", font=("Arial", 16))
    user_entry.insert(0, "Enter your username")  # Placeholder text
    user_entry.place(x=70, y=518)
    def clear_placeholder(event): #Username Prompt
        if user_entry.get() == "Enter your username":
            user_entry.delete(0, tk.END)
            user_entry.config(fg="black")
    user_entry.bind("<FocusIn>", clear_placeholder)


    def restore_placeholder(event):#Defines the function to restore the placeholder text when the entry field loses focus
        if user_entry.get() == "":
            user_entry.insert(0, "Enter your username")
            user_entry.config(fg="grey")
    user_entry.bind("<FocusOut>", restore_placeholder)
    username = user_entry.get()  # Get the username from the entry field
    print("Username:", username)  # Print the username to the console
    #Password
    pass_entry = tk.Entry(frame, width=30, bd=0, highlightthickness=0, relief = "flat", bg="white", font=("Arial", 16), show="*")
    pass_entry.insert(0, "Enter your password")  # Placeholder text
    pass_entry.place(x=73, y=643)
    #Password Prompt
    def clear_placeholder_pass(event): 
        if pass_entry.get() == "Enter your password":
            pass_entry.delete(0, tk.END)
            pass_entry.config(fg="black", show="*")
    pass_entry.bind("<FocusIn>", clear_placeholder_pass)
    #Login Button
    login_button = tk.Button(frame, text="Login", font=("Arial", 16, "bold"), bg="black", fg="black", bd=0, highlightthickness=0, relief="flat", command=lambda: page_switch(main_menu))  # Switch to main menu 
    login_button.place(x=150, y=770)

def main_menu(frame):
    image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Main Menu 1.png") #Import the Background for The home page
    image = image.resize((430, 932)) # Resize the image to be correct

    bg_image = ImageTk.PhotoImage(image) # Store the Image
    bg_label = tk.Label(frame, image=bg_image)
    
    canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.bg_image = bg_image  
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    
    next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#6b63fe", relief="flat", command=lambda: page_switch(main_menu1))  
    next_button.place(x=350, y=475)
    

def main_menu1(frame):
    image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Main Menu 2 Quizzlet.png")
    image = image.resize((430,932)) #Resizes Image

    bg_image = ImageTk.PhotoImage(image)
    image = image.resize((430, 932)) # Resize the image to be correct

    canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.bg_image = bg_image  
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    back_button = tk.Button(frame, text="<", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: page_switch(main_menu))
    back_button.place(x=20, y=475)

    
    



page_switch(home_page)  # Display the home page initially
root.mainloop()



