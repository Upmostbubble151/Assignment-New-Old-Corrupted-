

#Intialise Windows
from email.mime import image
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser #Video

class QuizApp:
    def __init__(self, root): #Creating the Window
        self.root = root
        self.root.title("Quizzlet")
        self.root.geometry("420x832")
        self.root.resizable(False, False)
        #Switching Pages
        self.current_page = None #Acts as a changable variable which is us
        self.page_switch(self.home_page)  # Display the home page initially
        self.score = 0 #Intialise the Score to be counted 
    #Page Switch
    def page_switch (self, page_function): #Defines Variable that changes to the different Pages. page_function is the page you want to switch
        if self.current_page is not None:
            self.current_page.destroy() #removes current page
        
        self.current_page = tk.Frame(self.root) #Creates a new frame 
        self.current_page.pack(fill="both", expand=True) #New frame fills the Next page
        page_function(self.current_page) #displays the new page

    def home_page(self,frame):
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
        login_button = tk.Button(frame, text="Login", font=("Arial", 16, "bold"), bg="black", fg="black", bd=0, highlightthickness=0, relief="flat", command=lambda: self.page_switch(self.main_menu))  # Switch to main menu 
        login_button.place(x=180, y=760)
        #Quit Button
        quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
        quit_button.place(x=100, y=800)
                    

    def main_menu(self,frame):
        image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Main Menu 1.png") #Import the Background for The home page
        image = image.resize((430, 932)) # Resize the image to be correct

        bg_image = ImageTk.PhotoImage(image) # Store the Image
        bg_label = tk.Label(frame, image=bg_image)
        
        canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.bg_image = bg_image  
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        Start_button = tk.Button(frame, text="Start", font=("Arial", 16, "bold"), bg="black", fg="black", bd=0, highlightthickness=0, relief="flat", command=lambda: self.page_switch(self.lecture1))  # Switch to Lecture 1 
        Start_button.place(x=200, y=755)
        
        next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#6b63fe", relief="flat", command=lambda: self.page_switch(self.main_menu1))  
        next_button.place(x=350, y=475)
        #Quit Button
        quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
        quit_button.place(x=100, y=800)
                    
        
    

    def lecture1(self,frame):
            image = Image.open("//Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lesson 1 - Video.png") #Import the Background for The home page
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)
        
            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image  
            canvas.create_image(0, 0, image=bg_image, anchor="nw")
            #Widgets
            play_button = tk.Button(frame, text="Play Video", font=("Arial", 16, "bold"), command=lambda: webbrowser.open("https://www.youtube.com/watch?v=lWcIhIyKeog"))
            play_button.place(x=160, y=495)

            back_button = tk.Button(frame, text="<", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.main_menu))
            back_button.place(x=20, y=475)

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q1))
            next_button.place(x=350, y=475)
    def lecture1_Q1(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture 1 - Q1 .png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")
            #Provide An entry box for the user to input their answer
            answer_entry = tk.Entry(frame, font=("Arial", 16), width = 10)
            answer_entry.place(x=150, y=750)
            #Function to check the answer and update the score
            def check_answer():
                 user_entry = answer_entry.get().strip().upper()  # Converts user input to uppercase and remove spaces
                 correct_answer = "A"

                 if user_entry == correct_answer:
                     self.score += 1  # Add Score 1 to variable to keep track
                     print("Correct! Score:", self.score)
                     self.page_switch(self.lecture1_Q1_Correct)
                 else:
                        print("Incorrect. Score:", self.score)
                        self.page_switch(self.lecture1_Q1_Incorrect)
                        
            #Submit Button
            submit_button = tk.Button(frame, text="Submit", font=("Arial", 16, "bold"), command=check_answer)                 
            submit_button.place(x=200, y=800)
            quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
            quit_button.place(x=50, y=800)
                    

    def lecture1_Q1_Correct(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q1_Correct.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q2))
            next_button.place(x=350, y=475)

         
    
    def lecture1_Q1_Incorrect(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q1_Incorrect.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q2))
            next_button.place(x=350, y=475)

    def lecture1_Q2(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q2.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")
            #Provide An entry box for the user to input their answer
            answer_entry = tk.Entry(frame, font=("Arial", 16), width = 10)            
            answer_entry.place(x=150, y=750)
            #Function to check the answer and update the score
            def check_answer():
                    user_entry = answer_entry.get().strip().upper()  # Converts user input to uppercase and remove spaces
                    correct_answer = "A"
    
                    if user_entry == correct_answer:
                        self.score += 1  # Add Score 1 to variable to keep track
                        print("Correct! Score:", self.score)
                        self.page_switch(self.lecture1_Q2_Correct)
                    else:
                            print("Incorrect. Score:", self.score)
                            self.page_switch(self.lecture1_Q2_Incorrect)
            submit_button = tk.Button(frame, text="Submit", font=("Arial", 16, "bold"), command=check_answer)                 
            submit_button.place(x=200, y=800)
            quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
            quit_button.place(x=100, y=800)
                    
    
    def lecture1_Q2_Correct(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q2_Correct.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q3))
            next_button.place(x=350, y=475)
    def lecture1_Q2_Incorrect(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q2_Incorrect.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q3))
            next_button.place(x=350, y=475)

    def lecture1_Q3(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q3.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")
            #Provide An entry box for the user to input their answer
            answer_entry = tk.Entry(frame, font=("Arial", 16), width = 10)            
            answer_entry.place(x=150, y=750)
            #Function to check the answer and update the score
            def check_answer():
                    user_entry = answer_entry.get().strip().upper()  # Converts user input to uppercase and remove spaces
                    correct_answer = "B"
    
                    if user_entry == correct_answer:
                        self.score += 1  # Add Score 1 to variable to keep track
                        print("Correct! Score:", self.score)
                        self.page_switch(self.lecture1_Q3_Correct)
                    else:
                            print("Incorrect. Score:", self.score)
                            self.page_switch(self.lecture1_Q3_Incorrect)
            submit_button = tk.Button(frame, text="Submit", font=("Arial", 16, "bold"), command=check_answer)                 
            submit_button.place(x=200, y=800)
            quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
            quit_button.place(x=100, y=800)
                    

    def lecture1_Q3_Correct(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q3_Correct.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q4))
            next_button.place(x=350, y=475)
    
    def lecture1_Q3_Incorrect(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q3_Incorrect.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q4))
            next_button.place(x=350, y=475)

    def lecture1_Q4(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q4.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")
            #Provide An entry box for the user to input their answer
            answer_entry = tk.Entry(frame, font=("Arial", 16), width = 10)            
            answer_entry.place(x=150, y=750)
            #Function to check the answer and update the score
            def check_answer():
                    user_entry = answer_entry.get().strip().upper()  # Converts user input to uppercase and remove spaces
                    correct_answer = "C"
    
                    if user_entry == correct_answer:
                        self.score += 1  # Add Score 1 to variable to keep track
                        print("Correct! Score:", self.score)
                        self.page_switch(self.lecture1_Q4_Correct)
                    else:
                            print("Incorrect. Score:", self.score)
                            self.page_switch(self.lecture1_Q4_Incorrect)
            submit_button = tk.Button(frame, text="Submit", font=("Arial", 16, "bold"), command=check_answer)                 
            submit_button.place(x=200, y=800)
            quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
            quit_button.place(x=100, y=800)
                    

    def lecture1_Q4_Correct(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q4_Correct.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q5))
            next_button.place(x=350, y=475)
    def lecture1_Q4_Incorrect(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q4_Incorrect.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q5))
            next_button.place(x=350, y=475)
        
    def lecture1_Q5(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q5.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")
            #Provide An entry box for the user to input their answer
            answer_entry = tk.Entry(frame, font=("Arial", 16), width = 10)            
            answer_entry.place(x=150, y=750)
            #Function to check the answer and update the score
            def check_answer():
                    user_entry = answer_entry.get().strip().upper()  # Converts user input to uppercase and remove spaces
                    correct_answer = "B"
    
                    if user_entry == correct_answer:
                        self.score += 1  # Add Score 1 to variable to keep track
                        print("Correct! Score:", self.score)
                        self.page_switch(self.lecture1_Q5_Correct)
                    else:
                            print("Incorrect. Score:", self.score)
                            self.page_switch(self.lecture1_Q5_Incorrect)
            submit_button = tk.Button(frame, text="Submit", font=("Arial", 16, "bold"), command=check_answer)                 
            submit_button.place(x=200, y=800)
            quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
            quit_button.place(x=100, y=800)
                    

    def lecture1_Q5_Correct(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q5_Correct.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q6))
            next_button.place(x=350, y=475)
    def lecture1_Q5_Incorrect(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q5_Incorrect.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")

            next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q6))
            next_button.place(x=350, y=475)

    def lecture1_Q6(self, frame):
            image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/lecture1_Q6.png")
            image = image.resize((430, 932)) # Resize the image to be correct

            bg_image = ImageTk.PhotoImage(image) # Store the Image
            bg_label = tk.Label(frame, image=bg_image)

            #Creates Canvas to display the background image
            canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)
            canvas.bg_image = bg_image
            canvas.create_image(0, 0, image=bg_image, anchor="nw")
            #Provide An entry box for the user to input their answer
            answer_entry = tk.Entry(frame, font=("Arial", 16), width = 10)            
            answer_entry.place(x=150, y=750)
            #Function to check the answer and update the score
            def check_answer():
                    user_entry = answer_entry.get().strip().upper()  # Converts user input to uppercase and remove spaces
                    correct_answer = "C"
    
                    if user_entry == correct_answer:
                        self.score += 1  # Add Score 1 to variable to keep track
                        print("Correct! Score:", self.score)
                        self.page_switch(self.lecture1_Q6_Correct)
                    else:
                            print("Incorrect. Score:", self.score)
                            self.page_switch(self.lecture1_Q6_Incorrect)
            submit_button = tk.Button(frame, text="Submit", font=("Arial", 16, "bold"), command=check_answer)                 
            submit_button.place(x=200, y=800)
            quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
            quit_button.place(x=100, y=800)
                    

    def lecture1_Q6_Correct(self, frame):
        image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/lecture1_Q6_Correct.png")
        image = image.resize((430, 932))

        bg_image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.bg_image = bg_image
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q7)); next_button.place(x=350, y=475)
        next_button.place(x=350, y=475)
        
    def lecture1_Q6_Incorrect(self, frame):
        image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/lecture1_Q6_Incorrect.png")
        image = image.resize((430, 932))

        bg_image = ImageTk.PhotoImage(image)
        bg_label = tk.Label(frame, image=bg_image)

        canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.bg_image = bg_image
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_Q7))
        next_button.place(x=350, y=475)

    def lecture1_Q7(self, frame):
        image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q7.png")
        image = image.resize((430, 932))

        bg_image = ImageTk.PhotoImage(image)
        bg_label = tk.Label(frame, image=bg_image)

        canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.bg_image = bg_image
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        answer_entry = tk.Entry(frame, font=("Arial", 16), width=10)
        answer_entry.place(x=150, y=750)

        def check_answer():
                user_entry = answer_entry.get().strip().upper()
                correct_answer = "C"

                if user_entry == correct_answer:
                    self.score += 1
                    print("Correct! Score:", self.score)
                    self.page_switch(self.lecture1_Q7_Correct)
                else:
                    print("Incorrect. Score:", self.score)
                    self.page_switch(self.lecture1_Q7_Incorrect)

        submit_button = tk.Button(frame, text="Submit", font=("Arial", 16, "bold"), command=check_answer)
        submit_button.place(x=200, y=800)
        quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
        quit_button.place(x=100, y=800)
                    

    def lecture1_Q7_Correct(self, frame):
        image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Lecture1_Q7_Correct.png")
        image = image.resize((430, 932))

        bg_image = ImageTk.PhotoImage(image)
        bg_label = tk.Label(frame, image=bg_image)

        canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.bg_image = bg_image
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_report))
        next_button.place(x=350, y=475) 

    def lecture1_Q7_Incorrect(self, frame):
        image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/lecture1_Q7_Incorrect.png")
        image = image.resize((430, 932))

        bg_image = ImageTk.PhotoImage(image)
        bg_label = tk.Label(frame, image=bg_image)

        canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.bg_image = bg_image
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.lecture1_report))
        next_button.place(x=350, y=475)
    
    def lecture1_report(self, frame):
        image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/lecture1_Report.png")
        image = image.resize((430, 932))

        bg_image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.bg_image = bg_image
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        #Displaying a positive message of result
        
        if self.score == 7:
                message = f"Excellent! {self.score}/7"
        elif self.score >= 5:
                message = f"Great job! {self.score}/7"
        elif self.score >= 3:
                message = f"Good effort! {self.score}/7"
        else:
                message = f"Keep practising! {self.score}/7"

        message_label = tk.Label(frame, text=message, font=("Arial", 20, "bold"), bg="white", fg="black")
        message_label.place(x=110, y=600)

        next_button = tk.Button(frame, text=">", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.main_menu))
        next_button.place(x=350, y=475)
    def main_menu1(self,frame):
        image = Image.open("/Users/HeereshGaneshan/Documents/VIsual Studio Code/Assignment 2/Assignment New (Old Corrupted)/Main Menu 2 Quizzlet.png")
        image = image.resize((430,932)) #Resizes Image

        bg_image = ImageTk.PhotoImage(image)
        image = image.resize((430, 932)) # Resize the image to be correct

        canvas = tk.Canvas(frame, width=430, height=932, bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.bg_image = bg_image  
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        back_button = tk.Button(frame, text="<", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.main_menu))
        back_button.place(x=20, y=475)

        trylater_button = tk.Button(frame, text="Try Again Later", bg="#6b63fe", bd=0, highlightthickness=0, activebackground="#ffffff", relief="flat", command=lambda: self.page_switch(self.main_menu1))
        trylater_button.place(x=170, y=750)

        #Quit Button
        quit_button = tk.Button(frame, text="Quit", font=("Arial", 16, "bold"), command=self.root.quit)
        quit_button.place(x=100, y=800)
                    
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
        





