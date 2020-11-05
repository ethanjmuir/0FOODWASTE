import requests
import tkinter as tk
import tkinter.font as tkFont
#from tkinter import filedialog, Text, Frame
from tkinter import *
import os

# API Setup
api_key = ('?apiKey=782bba4ef5fd462d81b2102ebb96fe55')

# --------- THE APP ---------

# --- Defining Button Functions START ---

class BaseWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainPage)
    
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class MainPage(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------
        '''
        # --- Profile START ---
        profile_button = tk.Button(self, bg = "#000")
        profile_button.place(relwidth = 0.3, relheight = 0.12, relx = 0.1, rely = 0.12)
        profile_label = tk.Label(self, text = "Your Profile", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.45, rely = 0.15)
        # ---------------------
        '''
        # --- Meal Planner START ---

        meal_label = tk.Label(self, text = "Your Meals for the Day", bg = "#fff", fg = "#000", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
        meal_label.place(relx = 0.05, rely = 0.12)

        previous_button = tk.Button(self, text = "<", bg = "#000")
        previous_button.place(relwidth = 0.075, relheight = 0.15, relx = 0, rely = 0.45)

        next_button = tk.Button(self, text = ">", bg = "#000")
        next_button.place(relwidth = 0.075, relheight = 0.15, relx = 0.925, rely = 0.45)

        frame_3 = tk.Button(self, bg = "#4953f6", command=lambda: master.switch_frame(BreakfastPage))
        frame_3.place(relwidth = 0.8, relheight = 0.15, relx = 0.1, rely = 0.2)
        breakfast_label = tk.Label(self, text = "Breakfast", bg = "#4953f6", fg = "#fff", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
        breakfast_label.place(relx = 0.1, rely = 0.22)

        frame_4 = tk.Button(self, bg = "#6953f4", command=lambda: master.switch_frame(LunchPage))
        frame_4.place(relwidth = 0.8, relheight = 0.15, relx = 0.1, rely = 0.45)
        lunch_label = tk.Label(self, text = "Lunch", bg = "#6953f4", fg = "#fff", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
        lunch_label.place(relx = 0.1, rely = 0.47)

        frame_5 = tk.Button(self, bg = "#8953f3", command=lambda: master.switch_frame(DinnerPage))
        frame_5.place(relwidth = 0.8, relheight = 0.15, relx = 0.1, rely = 0.7)
        dinner_label = tk.Label(self, text = "Dinner", bg = "#8953f3", fg = "#fff", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
        dinner_label.place(relx = 0.1, rely = 0.72)
        '''
        button_1 = tk.Button(self, text = "Suggestions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(SuggestionsPage))
        button_1.place(relwidth = 0.2, relheight = 0.05, relx = 0.1, rely = 0.9,)
        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.35, rely = 0.9)
        '''
        home_button = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(MainPage))
        home_button.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)
        '''
        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.65, rely = 0.9)
        button_3 = tk.Button(self, text = "Instructions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(InstructionsPage))
        button_3.place(relwidth = 0.2, relheight = 0.05, relx = 0.7, rely = 0.9)
        '''
        # ------------------------

class BreakfastPage(tk.Canvas):
    def __init__(self, suggestions):

        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------

        # SUGGESTIONS

        # --- Right-Most Scrollbar ---
        '''
        scrollbar = tk.Scrollbar(self, bg = "#fff").place(relwidth = 0.5, relheight = 1.0, relx = 0.95, rely = 0)
        
        
        canvas.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = canvas.yview)
        '''

        profile_label = tk.Label(self, text = "Breakfast", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.05, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)

        entry_1 = tk.Entry(self, bg = "#f54c49")
        entry_1.place(relwidth = 0.6, relheight = 0.2, relx = 0.2, rely = 0.3)
        '''
        def switch_frame(self, frame_class):
            new_frame = frame_class(self)
            if self._frame is not None:
                self._frame.destroy()
            self._frame = new_frame
            self._frame.pack()
        '''
        def search():
                        
            #Create frame and scroll bar
            my_frame = Frame()
            my_scrollbar = Scrollbar(my_frame, orient = VERTICAL)

            #Listbox
            my_listbox = Listbox(my_frame, height=5, width = 50, yscrollcommand=my_scrollbar.set)

            #configure scrollbar
            my_scrollbar.config(command = my_listbox.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.2, rely = 0.7, relwidth = 0.6, relheight = 0.4)
                
            my_listbox.place(relwidth = 0.6, relheight = 0.1) 

            #search recipe and add it to list box
            food = entry_1.get()
            print(food)
            request_search_recipe = requests.get('https://api.spoonacular.com/recipes/complexSearch'+api_key+'&query='+food)
            request_search_recipe_json=request_search_recipe.json()
            print(food)
            for i in request_search_recipe_json['results']:
                print('hello')
                print(i['title'])
                position = 0
                my_listbox.insert(position, (i['title']))
                #print(i['title'])
                #print(i['id'])
                #print('')
                position +=1


        enter_button = tk.Button(self, text = "Enter", bg = "#ccd1d9", fg = "#000", command=search())
        enter_button.place(relwidth = 0.2, relheight = 0.06, relx = 0.4, rely = 0.6)
           
        '''
        button_1 = tk.Button(self, text = "Suggestions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(SuggestionsPage))
        button_1.place(relwidth = 0.2, relheight = 0.05, relx = 0.1, rely = 0.9,)
        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.35, rely = 0.9)
        '''
        home_button = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(MainPage))
        home_button.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)
        '''
        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.65, rely = 0.9)
        button_3 = tk.Button(self, text = "Instructions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(InstructionsPage))
        button_3.place(relwidth = 0.2, relheight = 0.05, relx = 0.7, rely = 0.9)
        '''
        
class LunchPage(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()

        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)

        profile_label = tk.Label(self, text = "Lunch", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.05, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)

        entry_1 = tk.Entry(self, bg = "#f54c49")
        entry_1.place(relwidth = 0.6, relheight = 0.2, relx = 0.2, rely = 0.3)
        '''
        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.35, rely = 0.9)
        '''
        home_button = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(MainPage))
        home_button.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)
        '''
        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.65, rely = 0.9)
        button_3 = tk.Button(self, text = "Instructions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(InstructionsPage))
        button_3.place(relwidth = 0.2, relheight = 0.05, relx = 0.7, rely = 0.9)
        '''

class DinnerPage(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------

        # SUGGESTIONS

        # --- Right-Most Scrollbar ---
        '''
        scrollbar = tk.Scrollbar(self, bg = "#fff").place(relwidth = 0.5, relheight = 1.0, relx = 0.95, rely = 0)
        
        
        canvas.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = canvas.yview)
        '''

        profile_label = tk.Label(self, text = "Dinner", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.05, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)

        entry_1 = tk.Entry(self, bg = "#f54c49")
        entry_1.place(relwidth = 0.6, relheight = 0.2, relx = 0.2, rely = 0.3)
        '''
        button_1 = tk.Button(self, text = "Suggestions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(SuggestionsPage))
        button_1.place(relwidth = 0.2, relheight = 0.05, relx = 0.1, rely = 0.9,)
        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.35, rely = 0.9)
        '''
        button_2 = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)
        '''
        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.65, rely = 0.9)
        button_3 = tk.Button(self, text = "Instructions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(InstructionsPage))
        button_3.place(relwidth = 0.2, relheight = 0.05, relx = 0.7, rely = 0.9)
        '''
        

# --- Loop All Windows ---
master = BaseWindow()
master.mainloop()
