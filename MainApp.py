import requests
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import os

# API Setup

#api_key = ('?apiKey=782bba4ef5fd462d81b2102ebb96fe55')
#api_key = ('?apiKey=76865ec43abf4ed8b775b956dd6dfaf5')
#api_key = ('?apiKey=b2851b4e879e4d24800357e02da17645')
#api_key = ('?apiKey=9172aaf2bf104daa84d9e09f6f54a3ed')
api_key = ('?apiKey=83e419f9ed354ccc86b57c36f95c7811')


recipe_id_list = [' ']
total_calories_list = [' ']
recipe_name_list = [' ']
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
       
        # --- Meal Planner START ---

        meal_label = tk.Label(self, text = "Your Meals for the Day", bg = "#fff", fg = "#000", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
        meal_label.place(relx = 0.05, rely = 0.12)

        frame_3 = tk.Button(self, bg = "#4953f6", command=lambda: master.switch_frame(IngredientsPageBreakfast))
        frame_3.place(relwidth = 0.8, relheight = 0.15, relx = 0.1, rely = 0.2)
        breakfast_label = tk.Label(self, text = "Breakfast", bg = "#4953f6", fg = "#fff", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
        breakfast_label.place(relx = 0.1, rely = 0.22)

        frame_4 = tk.Button(self, bg = "#6953f4", command=lambda: master.switch_frame(IngredientsPageLunch))
        frame_4.place(relwidth = 0.8, relheight = 0.15, relx = 0.1, rely = 0.45)
        lunch_label = tk.Label(self, text = "Lunch", bg = "#6953f4", fg = "#fff", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
        lunch_label.place(relx = 0.1, rely = 0.47)

        frame_5 = tk.Button(self, bg = "#8953f3", command=lambda: master.switch_frame(IngredientsPageDinner))
        frame_5.place(relwidth = 0.8, relheight = 0.15, relx = 0.1, rely = 0.7)
        dinner_label = tk.Label(self, text = "Dinner", bg = "#8953f3", fg = "#fff", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
        dinner_label.place(relx = 0.1, rely = 0.72)
       
        home_button = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        home_button.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)
        
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

        profile_label = tk.Label(self, text = "Breakfast", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.05, rely = 0.1)
        
        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.65, relx = 0.1, rely = 0.2)

        total_calories_label = tk.Label(suggestion_1, text = "Total Calories For This Meal", bg = "#8953f6", fg = '#fff', font = ('Roboto', 10, 'bold'), padx = 10, pady = 5)
        total_calories_label.place(relx = 0.05, rely = 0.05)
        
        entry_total_calories = tk.Entry(suggestion_1, bg = "#fff", fg = '#000')
        entry_total_calories.place(relwidth = 0.6, relheight = 0.1, relx = 0.1, rely= 0.1)

        search_bar_label = tk.Label(suggestion_1, text = "Search Recipes", bg = "#8953f6", fg = '#fff', font = ('Roboto', 10, 'bold'), padx = 10, pady = 5)
        search_bar_label.place(relx = 0.05, rely = 0.2)

        entry_1 = tk.Entry(suggestion_1, bg = "#fff", fg = '#000')
        entry_1.place(relwidth = 0.6, relheight = 0.1, relx = 0.1, rely = 0.25)

        def search():
            try:
                int(entry_total_calories.get())
                file_cal_input_breakfast = open('cal_breakfast.txt', 'w')
                file_cal_input_breakfast.write(entry_total_calories.get())
                file_cal_input_breakfast.close()
                calorie_input_check = 'Valid'
            except ValueError:
                calorie_input_check = 'Invalid'
                    
            #Create frame and scroll bar
            my_frame = Frame(suggestion_1)
            my_scrollbar = Scrollbar(my_frame, orient = VERTICAL)

            #Listbox
            my_listbox = Listbox(my_frame, yscrollcommand=my_scrollbar.set)

            #configure scrollbar
            my_scrollbar.config(command = my_listbox.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.1, rely = 0.35, relwidth = 0.8, relheight = 0.4)   
            my_listbox.place(relx = 0, rely = 0, relwidth = 0.94, relheight = 1)

            #search recipe and add it to list box
            food = entry_1.get()
                  
            if food == '':
                no_recipe_entered_label = tk.Label(self, text = "No Recipes Found", bg = "#8953f6", fg = '#000', font = ('Roboto', 10, 'bold'), padx = 10, pady = 15)
                no_recipe_entered_label.place(relx = 0.3, rely = 0.7)
                
            else:
                request_search_recipe = requests.get('https://api.spoonacular.com/recipes/complexSearch'+api_key+'&query='+food)
                request_search_recipe_json=request_search_recipe.json()
                ids = []
                names = []
                for i in request_search_recipe_json['results']:
                    print(i['title'])
                    print(' ')
                    my_listbox.insert(END, (i['title']))
                    ids.append(i['id'])
                    names.append(i['title'])


            def select():

                if my_listbox.curselection() == ():
                    no_recipe_selected_label = tk.Label(self, text = "Please Select a Recipe", bg = "#8953f6", fg = '#000', font = ('Roboto', 10, 'bold'), padx = 10, pady = 15)
                    no_recipe_selected_label.place(relx = 0.3, rely = 0.7)
                    
                else:
                    x = my_listbox.curselection()
                    n = x[0]
                    recipe_id = ids[n]
                    file_id_input_breakfast = open('id_breakfast.txt', 'w')
                    file_id_input_breakfast.write(str(recipe_id))
                    file_id_input_breakfast.close()
                    recipe_name = names[n]
                    file_name_input_breakfast = open('name_breakfast.txt', 'w')
                    file_name_input_breakfast.write(recipe_name)
                    file_name_input_breakfast.close()
                    master.switch_frame(IngredientsPageBreakfast)
                    return

            if my_listbox.get(0) == "" or calorie_input_check == 'Invalid':
                no_recipe_found_label = tk.Label(self, text = "Invalid Input for Calories or Recipe", bg = "#8953f6", fg = '#000', font = ('Roboto', 10, 'bold'), padx = 10, pady = 15)
                no_recipe_found_label.place(relx = 0.2, rely = 0.75)
                cover_select_button = tk.Label(text = "Select", bg = "#8953f6", fg = "#8953f6")
                cover_select_button.place(relwidth = 0.2, relheight = 0.06, relx = 0.4, rely = 0.7)
            else:
                cover_previous_label = tk.Label(self, text = "Invalid Input for Calories or Recipe", bg = "#8953f6", fg = '#8953f6', font = ('Roboto', 10, 'bold'), padx = 20, pady = 15)
                cover_previous_label.place(relx = 0.2, rely = 0.75)
                select_button = tk.Button(text = "Select", bg = "#ccd1d9", fg = "#000", command=select)
                select_button.place(relwidth = 0.2, relheight = 0.06, relx = 0.4, rely = 0.7)

        enter_recipe_button = tk.Button(suggestion_1, text = "Enter", bg = "#ccd1d9", fg = "#000", command=search)
        enter_recipe_button.place(relwidth = 0.2, relheight = 0.1, relx = 0.7, rely = 0.25)
  
        home_button = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        home_button.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)
  
        
class LunchPage(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()

        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)

        profile_label = tk.Label(self, text = "Lunch", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.05, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.65, relx = 0.1, rely = 0.2)


        total_calories_label = tk.Label(suggestion_1, text = "Total Calories For This Meal", bg = "#8953f6", fg = '#fff', font = ('Roboto', 10, 'bold'), padx = 10, pady = 5)
        total_calories_label.place(relx = 0.05, rely = 0.05)


        entry_total_calories = tk.Entry(suggestion_1, bg = "#fff", fg = '#000')
        entry_total_calories.place(relwidth = 0.6, relheight = 0.1, relx = 0.1, rely = 0.1)

        search_bar_label = tk.Label(suggestion_1, text = "Search Recipes", bg = "#8953f6", fg = '#fff', font = ('Roboto', 10, 'bold'), padx = 10, pady = 5)
        search_bar_label.place(relx = 0.05, rely = 0.2)

        entry_1 = tk.Entry(suggestion_1, bg = "#fff", fg = '#000')
        entry_1.place(relwidth = 0.6, relheight = 0.1, relx = 0.1, rely = 0.25)

        def search():
            try:
                int(entry_total_calories.get())
                file_cal_input_breakfast = open('cal_lunch.txt', 'w')
                file_cal_input_breakfast.write(entry_total_calories.get())
                file_cal_input_breakfast.close()
                calorie_input_check = 'Valid'
            except ValueError:
                calorie_input_check = 'Invalid'
           
            #Create frame and scroll bar
            my_frame = Frame(suggestion_1)
            my_scrollbar = Scrollbar(my_frame, orient = VERTICAL)

            #Listbox
            my_listbox = Listbox(my_frame, yscrollcommand=my_scrollbar.set)

            #configure scrollbar
            my_scrollbar.config(command = my_listbox.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.1, rely = 0.35, relwidth = 0.8, relheight = 0.4)   
            my_listbox.place(relx = 0, rely = 0, relwidth = 0.94, relheight = 1)

            #search recipe and add it to list box
            food = entry_1.get()
            if food == '':
                no_recipe_entered_label = tk.Label(self, text = "No Recipes Found", bg = "#8953f6", fg = '#000', font = ('Roboto', 10, 'bold'), padx = 10, pady = 15)
                no_recipe_entered_label.place(relx = 0.3, rely = 0.7)
                
            else:
                request_search_recipe = requests.get('https://api.spoonacular.com/recipes/complexSearch'+api_key+'&query='+food)
                request_search_recipe_json=request_search_recipe.json()
                ids = []
                names = []
                for i in request_search_recipe_json['results']:
                    position = 0
                    my_listbox.insert(END, (i['title']))
                    ids.append(i['id'])
                    names.append(i['title'])


            def select():

                if my_listbox.curselection() == ():
                    no_recipe_selected_label = tk.Label(self, text = "Please Select a Recipe", bg = "#fff", fg = '#000', font = ('Roboto', 10), padx = 10, pady = 15)
                    no_recipe_selected_label.place(relx = 0.1, rely = 0.7)
                    
                else:
                    x = my_listbox.curselection()
                    n = x[0]
                    recipe_id = ids[n]
                    file_id_input_lunch = open('id_lunch.txt', 'w')
                    file_id_input_lunch.write(str(recipe_id))
                    file_id_input_lunch.close()
                    recipe_name = names[n]
                    file_name_input_lunch = open('name_lunch.txt', 'w')
                    file_name_input_lunch.write(recipe_name)
                    file_name_input_lunch.close()
                    master.switch_frame(IngredientsPageLunch)
                    return
     
            if my_listbox.get(0) == "" or calorie_input_check == 'Invalid':
                no_recipe_found_label = tk.Label(self, text = "Invalid Input for Calories or Recipe", bg = "#8953f6", fg = '#000', font = ('Roboto', 10, 'bold'), padx = 10, pady = 15)
                no_recipe_found_label.place(relx = 0.2, rely = 0.75)
                cover_select_button = tk.Label(text = "Select", bg = "#8953f6", fg = "#8953f6")
                cover_select_button.place(relwidth = 0.2, relheight = 0.06, relx = 0.4, rely = 0.7)
            else:
                cover_previous_label = tk.Label(self, text = "Invalid Input for Calories or Recipe", bg = "#8953f6", fg = '#8953f6', font = ('Roboto', 10, 'bold'), padx = 20, pady = 15)
                cover_previous_label.place(relx = 0.2, rely = 0.75)
                select_button = tk.Button(text = "Select", bg = "#ccd1d9", fg = "#000", command=select)
                select_button.place(relwidth = 0.2, relheight = 0.06, relx = 0.4, rely = 0.7)
                
        enter_button = tk.Button(suggestion_1, text = "Enter", bg = "#ccd1d9", fg = "#000", command=search)
        enter_button.place(relwidth = 0.2, relheight = 0.1, relx = 0.7, rely = 0.25)

        home_button = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        home_button.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)

class DinnerPage(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------

        # SUGGESTIONS

        # --- Right-Most Scrollbar ---

        profile_label = tk.Label(self, text = "Dinner", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.05, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.65, relx = 0.1, rely = 0.2)

        total_calories_label = tk.Label(suggestion_1, text = "Total Calories For This Meal", bg = "#8953f6", fg = '#fff', font = ('Roboto', 10, 'bold'), padx = 10, pady = 5)
        total_calories_label.place(relx = 0.05, rely = 0.05)
        
        entry_total_calories = tk.Entry(suggestion_1, bg = "#fff", fg = '#000')
        entry_total_calories.place(relwidth = 0.6, relheight = 0.1, relx = 0.1, rely = 0.1)

        search_bar_label = tk.Label(suggestion_1, text = "Search Recipes", bg = "#8953f6", fg = '#fff', font = ('Roboto', 10, 'bold'), padx = 10, pady = 5)
        search_bar_label.place(relx = 0.05, rely = 0.2)

        entry_1 = tk.Entry(suggestion_1, bg = "#fff", fg = '#000')
        entry_1.place(relwidth = 0.6, relheight = 0.1, relx = 0.1, rely = 0.25)

        def search():
            try:
                int(entry_total_calories.get())
                file_cal_input_breakfast = open('cal_dinner.txt', 'w')
                file_cal_input_breakfast.write(entry_total_calories.get())
                file_cal_input_breakfast.close()
                calorie_input_check = 'Valid'
            except ValueError:
                calorie_input_check = 'Invalid'
            #Create frame and scroll bar
            my_frame = Frame(suggestion_1)
            my_scrollbar = Scrollbar(my_frame, orient = VERTICAL)

            #Listbox
            my_listbox = Listbox(my_frame, yscrollcommand=my_scrollbar.set)

            #configure scrollbar
            my_scrollbar.config(command = my_listbox.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.1, rely = 0.35, relwidth = 0.8, relheight = 0.4)   
            my_listbox.place(relx = 0, rely = 0, relwidth = 0.94, relheight = 1)

            #search recipe and add it to list box
            food = entry_1.get()
            if food == '':
                no_recipe_entered_label = tk.Label(self, text = "No Recipes Found", bg = "#8953f6", fg = '#000', font = ('Roboto', 10, 'bold'), padx = 10, pady = 15)
                no_recipe_entered_label.place(relx = 0.3, rely = 0.7)
                
            else:
                request_search_recipe = requests.get('https://api.spoonacular.com/recipes/complexSearch'+api_key+'&query='+food)
                request_search_recipe_json=request_search_recipe.json()
                ids = []
                names = []
                for i in request_search_recipe_json['results']:
                    position = 0
                    my_listbox.insert(END, (i['title']))
                    ids.append(i['id'])
                    names.append(i['title'])

            def select():

                if my_listbox.curselection() == ():
                    no_recipe_selected_label = tk.Label(self, text = "Please Select a Recipe", bg = "#fff", fg = '#000', font = ('Roboto', 10), padx = 10, pady = 15)
                    no_recipe_selected_label.place(relx = 0.1, rely = 0.7)
                    
                else:
                    x = my_listbox.curselection()
                    n = x[0]
                    recipe_id = ids[n]
                    file_id_input_dinner = open('id_dinner.txt', 'w')
                    file_id_input_dinner.write(str(recipe_id))
                    file_id_input_dinner.close()
                    recipe_name = names[n]
                    file_name_input_dinner = open('name_dinner.txt', 'w')
                    file_name_input_dinner.write(recipe_name)
                    file_name_input_dinner.close()
                    master.switch_frame(IngredientsPageDinner)
                    return
                
            if my_listbox.get(0) == "" or calorie_input_check == 'Invalid':
                no_recipe_found_label = tk.Label(self, text = "Invalid Input for Calories or Recipe", bg = "#8953f6", fg = '#000', font = ('Roboto', 10, 'bold'), padx = 10, pady = 15)
                no_recipe_found_label.place(relx = 0.2, rely = 0.75)
                cover_select_button = tk.Label(text = "Select", bg = "#8953f6", fg = "#8953f6")
                cover_select_button.place(relwidth = 0.2, relheight = 0.06, relx = 0.4, rely = 0.7)
            else:
                cover_previous_label = tk.Label(self, text = "Invalid Input for Calories or Recipe", bg = "#8953f6", fg = '#8953f6', font = ('Roboto', 10, 'bold'), padx = 20, pady = 15)
                cover_previous_label.place(relx = 0.2, rely = 0.75)
                select_button = tk.Button(text = "Select", bg = "#ccd1d9", fg = "#000", command=select)
                select_button.place(relwidth = 0.2, relheight = 0.06, relx = 0.4, rely = 0.7)

        enter_button = tk.Button(suggestion_1, text = "Enter", bg = "#ccd1d9", fg = "#000", command=search)
        enter_button.place(relwidth = 0.2, relheight = 0.1, relx = 0.7, rely = 0.25)
        
        button_2 = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)

class IngredientsPageBreakfast(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------

        # SUGGESTIONS

        # --- Right-Most Scrollbar ---

        file_id_input_breakfast = open('id_breakfast.txt', 'a')
        file_id_input_breakfast.write('')
        file_id_input_breakfast.close()

        file_id_output_breakfast = open('id_breakfast.txt', 'r')
        file_id_info_breakfast = file_id_output_breakfast.readlines()
        file_id_output_breakfast.close()
        if file_id_info_breakfast == []:
            selected_recipe_id_breakfast = ' '
        else:
            selected_recipe_id_breakfast = file_id_info_breakfast[0]

        file_cal_input_breakfast = open('cal_breakfast.txt', 'a')
        file_cal_input_breakfast.write('')
        file_cal_input_breakfast.close()

        file_cal_output_breakfast = open('cal_breakfast.txt', 'r')
        file_cal_info_breakfast = file_cal_output_breakfast.readlines()
        file_cal_output_breakfast.close()
        if file_cal_info_breakfast == []:
            total_calories_breakfast = ' '
        else:
            total_calories_breakfast = float(file_cal_info_breakfast[0])

        file_name_input_breakfast = open('name_breakfast.txt', 'a')
        file_name_input_breakfast.write('')
        file_name_input_breakfast.close()

        file_name_output_breakfast = open('name_breakfast.txt', 'r')
        file_name_info_breakfast = file_name_output_breakfast.readlines()
        file_name_output_breakfast.close()
        if file_name_info_breakfast == []:
            selected_recipe_name_breakfast = ' '
        else:
            selected_recipe_name_breakfast = file_name_info_breakfast[0]
        

        ingredients_label = tk.Button(self, text = "Ingredients", bg = "#f54c49", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(IngredientsPageBreakfast))
        ingredients_label.place(relwidth=0.4, relheight=0.1, relx = 0.1, rely = 0.1)
        
        instructions_label = tk.Button(self, text = "Instructions", bg = "#8953f6", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(InstructionsPageBreakfast))
        instructions_label.place(relwidth=0.4, relheight=0.1, relx = 0.5, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#f54c49")
        suggestion_1.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)

        if total_calories_breakfast != ' ' and selected_recipe_name_breakfast != ' ' and selected_recipe_id_breakfast != ' ':
            #Create frame and scroll bar
            my_frame = Frame(suggestion_1)
            my_scrollbary = Scrollbar(my_frame.master, orient = VERTICAL)
            my_scrollbarx = Scrollbar(my_frame.master, orient = HORIZONTAL)

            #Listbox
            my_listbox = Listbox(my_frame, xscrollcommand=my_scrollbarx.set, yscrollcommand=my_scrollbary.set, font = ('Roboto', 15))

            #configure scrollbar
            my_scrollbarx.config(command = my_listbox.xview)
            my_scrollbary.config(command = my_listbox.yview)
            my_scrollbarx.pack(side=BOTTOM, fill=X)
            my_scrollbary.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
            my_listbox.place(relx = 0, rely = 0, relwidth = 0.94, relheight = 1)

            my_listbox.insert(END, selected_recipe_name_breakfast)
            my_listbox.insert(END, ' ')
            
            #Display Ingredients and amounts for recipe        
            recipe_nutrition = requests.get('https://api.spoonacular.com/recipes/'+selected_recipe_id_breakfast+'/nutritionWidget.json' + api_key)

            recipe_nutrition_json = recipe_nutrition.json()
            calories = recipe_nutrition_json['calories']

            calorie_adjustment_ratio = float(total_calories_breakfast)/float(calories)

            #Display Ingredients
            ingredients_info = requests.get('https://api.spoonacular.com/recipes/'+selected_recipe_id_breakfast+'/ingredientWidget.json'+api_key)
            ingredients_info_json = ingredients_info.json()
            
            for i in ingredients_info_json['ingredients']:
              (i['amount']).popitem()
              for j in ((i['amount']).values()):
                adjusted_value = (j['value'])*calorie_adjustment_ratio
                ingredient = ((i['name']) + ': ' + str(round(adjusted_value,2)) + ' ' + str(j['unit']))
                my_listbox.insert(END, ingredient)
                my_listbox.insert(END, '')
                
            else:
                pass
            
        button_2 = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)

        add_change_recipe = tk.Button(self, text = "Add/Change Recipe", bg = "#ccd1d9", fg = '#000', font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(BreakfastPage))
        add_change_recipe.place(relwidth=0.4, relheight=0.05, relx = 0.3, rely = 0.8)
        
class InstructionsPageBreakfast(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------

        # SUGGESTIONS

        # --- Right-Most Scrollbar ---
        file_id_input_breakfast = open('id_breakfast.txt', 'a')
        file_id_input_breakfast.write('')
        file_id_input_breakfast.close()

        file_id_output_breakfast = open('id_breakfast.txt', 'r')
        file_id_info_breakfast = file_id_output_breakfast.readlines()
        file_id_output_breakfast.close()
        if file_id_info_breakfast == []:
            selected_recipe_id_breakfast = ' '
        else:
            selected_recipe_id_breakfast = file_id_info_breakfast[0]

        file_cal_input_breakfast = open('cal_breakfast.txt', 'a')
        file_cal_input_breakfast.write('')
        file_cal_input_breakfast.close()

        file_cal_output_breakfast = open('cal_breakfast.txt', 'r')
        file_cal_info_breakfast = file_cal_output_breakfast.readlines()
        file_cal_output_breakfast.close()
        if file_cal_info_breakfast == []:
            total_calories_breakfast = ' '
        else:
            total_calories_breakfast = float(file_cal_info_breakfast[0])

        file_name_input_breakfast = open('name_breakfast.txt', 'a')
        file_name_input_breakfast.write('')
        file_name_input_breakfast.close()

        file_name_output_breakfast = open('name_breakfast.txt', 'r')
        file_name_info_breakfast = file_name_output_breakfast.readlines()
        file_name_output_breakfast.close()
        if file_name_info_breakfast == []:
            selected_recipe_name_breakfast = ' '
        else:
            selected_recipe_name_breakfast = file_name_info_breakfast[0]
        
        ingredients_label = tk.Button(self, text = "Ingredients", bg = "#f54c49", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(IngredientsPageBreakfast))
        ingredients_label.place(relwidth=0.4, relheight=0.1, relx = 0.1, rely = 0.1)
        
        instructions_label = tk.Button(self, text = "Instructions", bg = "#8953f6", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(InstructionsPageBreakfast))
        instructions_label.place(relwidth=0.4, relheight=0.1, relx = 0.5, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)
        
        if total_calories_breakfast != ' ' and selected_recipe_name_breakfast != ' ' and selected_recipe_id_breakfast != ' ':
            #Create frame and scroll bar
            my_frame = Frame(suggestion_1)
            my_scrollbary = Scrollbar(my_frame.master, orient = VERTICAL)
            my_scrollbarx = Scrollbar(my_frame.master, orient = HORIZONTAL)

            #Listbox
            my_listbox = Listbox(my_frame, xscrollcommand=my_scrollbarx.set, yscrollcommand=my_scrollbary.set, font = ('Roboto', 10, 'bold'))

            #configure scrollbar
            my_scrollbarx.config(command = my_listbox.xview)
            my_scrollbary.config(command = my_listbox.yview)
            my_scrollbarx.pack(side=BOTTOM, fill=X)
            my_scrollbary.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
            my_listbox.place(relx = 0, rely = 0, relwidth = 0.94, relheight = 1)

            my_listbox.insert(END, selected_recipe_name_breakfast)
            my_listbox.insert(END, ' ')
            #Display Recipe Instructions
            recipe_instructions = requests.get('https://api.spoonacular.com/recipes/'+selected_recipe_id_breakfast+'/analyzedInstructions' + api_key)
            recipe_instructions_json=recipe_instructions.json()

            for i in recipe_instructions_json:
              for n in i['steps']:
                #Step Number
                step_number = ('Step Number: ' + str(n['number']))
                my_listbox.insert(END, step_number)
                #Ingredients
                display_header = True
                for x in n['ingredients']:
                    if display_header == True:
                        my_listbox.insert(END,'Ingredients Needed For This Step:')
                        display_header = False
                    my_listbox.insert(END, x['localizedName'])
                #Equipment
                for y in n['equipment']:
                    my_listbox.insert(END, 'Equipment: ' + y['localizedName'])
                #Instructions
                my_listbox.insert(END, 'Instructions: ' + n['step'])
                my_listbox.insert(END, ' ')
        
        button_2 = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)
        
        add_change_recipe = tk.Button(self, text = "Add/Change Recipe", bg = "#ccd1d9", fg = '#000', font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(BreakfastPage))
        add_change_recipe.place(relwidth=0.4, relheight=0.05, relx = 0.3, rely = 0.8)

class IngredientsPageLunch(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------

        # SUGGESTIONS

        # --- Right-Most Scrollbar ---

        file_id_input_lunch = open('id_lunch.txt', 'a')
        file_id_input_lunch.write('')
        file_id_input_lunch.close()

        file_id_output_lunch = open('id_lunch.txt', 'r')
        file_id_info_lunch = file_id_output_lunch.readlines()
        file_id_output_lunch.close()
        if file_id_info_lunch == []:
            selected_recipe_id_lunch = ' '
        else:
            selected_recipe_id_lunch = file_id_info_lunch[0]

        file_cal_input_lunch = open('cal_lunch.txt', 'a')
        file_cal_input_lunch.write('')
        file_cal_input_lunch.close()

        file_cal_output_lunch = open('cal_lunch.txt', 'r')
        file_cal_info_lunch = file_cal_output_lunch.readlines()
        file_cal_output_lunch.close()
        if file_cal_info_lunch == []:
            total_calories_lunch = ' '
        else:
            total_calories_lunch = float(file_cal_info_lunch[0])

        file_name_input_lunch = open('name_lunch.txt', 'a')
        file_name_input_lunch.write('')
        file_name_input_lunch.close()

        file_name_output_lunch = open('name_lunch.txt', 'r')
        file_name_info_lunch = file_name_output_lunch.readlines()
        file_name_output_lunch.close()
        if file_name_info_lunch == []:
            selected_recipe_name_lunch = ' '
        else:
            selected_recipe_name_lunch = file_name_info_lunch[0]
        

        ingredients_label = tk.Button(self, text = "Ingredients", bg = "#f54c49", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(IngredientsPageLunch))
        ingredients_label.place(relwidth=0.4, relheight=0.1, relx = 0.1, rely = 0.1)
        
        instructions_label = tk.Button(self, text = "Instructions", bg = "#8953f6", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(InstructionsPageLunch))
        instructions_label.place(relwidth=0.4, relheight=0.1, relx = 0.5, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#f54c49")
        suggestion_1.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)

        if total_calories_lunch != ' ' and selected_recipe_name_lunch != ' ' and selected_recipe_id_lunch != ' ':
            #Create frame and scroll bar
            my_frame = Frame(suggestion_1)
            my_scrollbary = Scrollbar(my_frame.master, orient = VERTICAL)
            my_scrollbarx = Scrollbar(my_frame.master, orient = HORIZONTAL)

            #Listbox
            my_listbox = Listbox(my_frame, xscrollcommand=my_scrollbarx.set, yscrollcommand=my_scrollbary.set, font = ('Roboto', 15))

            #configure scrollbar
            my_scrollbarx.config(command = my_listbox.xview)
            my_scrollbary.config(command = my_listbox.yview)
            my_scrollbarx.pack(side=BOTTOM, fill=X)
            my_scrollbary.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
            my_listbox.place(relx = 0, rely = 0, relwidth = 0.94, relheight = 1)

            my_listbox.insert(END, selected_recipe_name_lunch)
            my_listbox.insert(END, ' ')
            
            #Display Ingredients and amounts for recipe

            recipe_nutrition = requests.get('https://api.spoonacular.com/recipes/'+selected_recipe_id_lunch+'/nutritionWidget.json' + api_key)

            recipe_nutrition_json = recipe_nutrition.json()
            calories = recipe_nutrition_json['calories']

            calorie_adjustment_ratio = float(total_calories_lunch)/float(calories)

            #Display Ingredients
            ingredients_info = requests.get('https://api.spoonacular.com/recipes/'+selected_recipe_id_lunch+'/ingredientWidget.json'+api_key)
            ingredients_info_json = ingredients_info.json()
            
            for i in ingredients_info_json['ingredients']:
              (i['amount']).popitem()
              for j in ((i['amount']).values()):
                adjusted_value = (j['value'])*calorie_adjustment_ratio
                ingredient = ((i['name']) + ': ' + str(round(adjusted_value,2)) + ' ' + str(j['unit']))
                my_listbox.insert(END, ingredient)
                my_listbox.insert(END, '')
                
            else:
                pass
            
        button_2 = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)

        add_change_recipe = tk.Button(self, text = "Add/Change Recipe", bg = "#ccd1d9", fg = '#000', font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(LunchPage))
        add_change_recipe.place(relwidth=0.4, relheight=0.05, relx = 0.3, rely = 0.8)
        
class InstructionsPageLunch(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------

        # SUGGESTIONS

        # --- Right-Most Scrollbar ---
        file_id_input_lunch = open('id_lunch.txt', 'a')
        file_id_input_lunch.write('')
        file_id_input_lunch.close()

        file_id_output_lunch = open('id_lunch.txt', 'r')
        file_id_info_lunch = file_id_output_lunch.readlines()
        file_id_output_lunch.close()
        if file_id_info_lunch == []:
            selected_recipe_id_lunch = ' '
        else:
            selected_recipe_id_lunch= file_id_info_lunch[0]

        file_cal_input_lunch = open('cal_lunch.txt', 'a')
        file_cal_input_lunch.write('')
        file_cal_input_lunch.close()

        file_cal_output_lunch = open('cal_lunch.txt', 'r')
        file_cal_info_lunch = file_cal_output_lunch.readlines()
        file_cal_output_lunch.close()
        if file_cal_info_lunch == []:
            total_calories_lunch = ' '
        else:
            total_calories_lunch = float(file_cal_info_lunch[0])

        file_name_input_lunch = open('name_lunch.txt', 'a')
        file_name_input_lunch.write('')
        file_name_input_lunch.close()

        file_name_output_lunch = open('name_lunch.txt', 'r')
        file_name_info_lunch = file_name_output_lunch.readlines()
        file_name_output_lunch.close()
        if file_name_info_lunch == []:
            selected_recipe_name_lunch = ' '
        else:
            selected_recipe_name_lunch = file_name_info_lunch[0]
        
        ingredients_label = tk.Button(self, text = "Ingredients", bg = "#f54c49", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(IngredientsPageLunch))
        ingredients_label.place(relwidth=0.4, relheight=0.1, relx = 0.1, rely = 0.1)
        
        instructions_label = tk.Button(self, text = "Instructions", bg = "#8953f6", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(InstructionsPageLunch))
        instructions_label.place(relwidth=0.4, relheight=0.1, relx = 0.5, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)
        
        if total_calories_lunch != ' ' and selected_recipe_name_lunch != ' ' and selected_recipe_id_lunch != ' ':
            #Create frame and scroll bar
            my_frame = Frame(suggestion_1)
            my_scrollbary = Scrollbar(my_frame.master, orient = VERTICAL)
            my_scrollbarx = Scrollbar(my_frame.master, orient = HORIZONTAL)

            #Listbox
            my_listbox = Listbox(my_frame, xscrollcommand=my_scrollbarx.set, yscrollcommand=my_scrollbary.set, font = ('Roboto', 10, 'bold'))

            #configure scrollbar
            my_scrollbarx.config(command = my_listbox.xview)
            my_scrollbary.config(command = my_listbox.yview)
            my_scrollbarx.pack(side=BOTTOM, fill=X)
            my_scrollbary.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
            my_listbox.place(relx = 0, rely = 0, relwidth = 0.94, relheight = 1)

            my_listbox.insert(END, selected_recipe_name_lunch)
            my_listbox.insert(END, ' ')
            #Display Recipe Instructions
            recipe_instructions = requests.get('https://api.spoonacular.com/recipes/'+selected_recipe_id_lunch+'/analyzedInstructions' + api_key)
            recipe_instructions_json=recipe_instructions.json()

            for i in recipe_instructions_json:
              for n in i['steps']:
                #Step Number
                step_number = ('Step Number: ' + str(n['number']))
                my_listbox.insert(END, step_number)
                #Ingredients
                display_header = True
                for x in n['ingredients']:
                    if display_header == True:
                        my_listbox.insert(END,'Ingredients Needed For This Step:')
                        display_header = False
                    my_listbox.insert(END, x['localizedName'])
                #Equipment
                for y in n['equipment']:
                    my_listbox.insert(END, 'Equipment: ' + y['localizedName'])
                #Instructions
                my_listbox.insert(END, 'Instructions: ' + n['step'])
                my_listbox.insert(END, ' ')
        
        button_2 = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)
        
        add_change_recipe = tk.Button(self, text = "Add/Change Recipe", bg = "#ccd1d9", fg = '#000', font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(LunchPage))
        add_change_recipe.place(relwidth=0.4, relheight=0.05, relx = 0.3, rely = 0.8)

class IngredientsPageDinner(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------

        # SUGGESTIONS

        # --- Right-Most Scrollbar ---

        file_id_input_dinner = open('id_dinner.txt', 'a')
        file_id_input_dinner.write('')
        file_id_input_dinner.close()

        file_id_output_dinner = open('id_dinner.txt', 'r')
        file_id_info_dinner = file_id_output_dinner.readlines()
        file_id_output_dinner.close()
        if file_id_info_dinner == []:
            selected_recipe_id_dinner = ' '
        else:
            selected_recipe_id_dinner = file_id_info_dinner[0]

        file_cal_input_dinner = open('cal_dinner.txt', 'a')
        file_cal_input_dinner.write('')
        file_cal_input_dinner.close()

        file_cal_output_dinner = open('cal_dinner.txt', 'r')
        file_cal_info_dinner = file_cal_output_dinner.readlines()
        file_cal_output_dinner.close()
        if file_cal_info_dinner == []:
            total_calories_dinner = ' '
        else:
            total_calories_dinner = float(file_cal_info_dinner[0])

        file_name_input_dinner = open('name_dinner.txt', 'a')
        file_name_input_dinner.write('')
        file_name_input_dinner.close()

        file_name_output_dinner = open('name_dinner.txt', 'r')
        file_name_info_dinner = file_name_output_dinner.readlines()
        file_name_output_dinner.close()
        if file_name_info_dinner == []:
            selected_recipe_name_dinner = ' '
        else:
            selected_recipe_name_dinner = file_name_info_dinner[0]
        

        ingredients_label = tk.Button(self, text = "Ingredients", bg = "#f54c49", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(IngredientsPageDinner))
        ingredients_label.place(relwidth=0.4, relheight=0.1, relx = 0.1, rely = 0.1)
        
        instructions_label = tk.Button(self, text = "Instructions", bg = "#8953f6", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(InstructionsPageDinner))
        instructions_label.place(relwidth=0.4, relheight=0.1, relx = 0.5, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#f54c49")
        suggestion_1.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)

        if total_calories_dinner != ' ' and selected_recipe_name_dinner != ' ' and selected_recipe_id_dinner != ' ':
            #Create frame and scroll bar
            my_frame = Frame(suggestion_1)
            my_scrollbary = Scrollbar(my_frame.master, orient = VERTICAL)
            my_scrollbarx = Scrollbar(my_frame.master, orient = HORIZONTAL)

            #Listbox
            my_listbox = Listbox(my_frame, xscrollcommand=my_scrollbarx.set, yscrollcommand=my_scrollbary.set, font = ('Roboto', 15))

            #configure scrollbar
            my_scrollbarx.config(command = my_listbox.xview)
            my_scrollbary.config(command = my_listbox.yview)
            my_scrollbarx.pack(side=BOTTOM, fill=X)
            my_scrollbary.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
            my_listbox.place(relx = 0, rely = 0, relwidth = 0.94, relheight = 1)

            my_listbox.insert(END, selected_recipe_name_dinner)
            my_listbox.insert(END, ' ')
            #Display Ingredients and amounts for recipe

            recipe_nutrition = requests.get('https://api.spoonacular.com/recipes/'+selected_recipe_id_dinner+'/nutritionWidget.json' + api_key)

            recipe_nutrition_json = recipe_nutrition.json()
            calories = recipe_nutrition_json['calories']

            calorie_adjustment_ratio = float(total_calories_dinner)/float(calories)

            #Display Ingredients
            ingredients_info = requests.get('https://api.spoonacular.com/recipes/'+selected_recipe_id_dinner+'/ingredientWidget.json'+api_key)
            ingredients_info_json = ingredients_info.json()
            
            for i in ingredients_info_json['ingredients']:
              (i['amount']).popitem()
              for j in ((i['amount']).values()):
                adjusted_value = (j['value'])*calorie_adjustment_ratio
                ingredient = ((i['name']) + ': ' + str(round(adjusted_value,2)) + ' ' + str(j['unit']))
                my_listbox.insert(END, ingredient)
                my_listbox.insert(END, '')
                
            else:
                pass
            
        button_2 = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)

        add_change_recipe = tk.Button(self, text = "Add/Change Recipe", bg = "#ccd1d9", fg = '#000', font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(DinnerPage))
        add_change_recipe.place(relwidth=0.4, relheight=0.05, relx = 0.3, rely = 0.8)
        
class InstructionsPageDinner(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()
        # --- Main Title ---
        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)
        # ------------------

        # SUGGESTIONS

        # --- Right-Most Scrollbar ---
        file_id_input_dinner = open('id_dinner.txt', 'a')
        file_id_input_dinner.write('')
        file_id_input_dinner.close()

        file_id_output_dinner = open('id_dinner.txt', 'r')
        file_id_info_dinner = file_id_output_dinner.readlines()
        file_id_output_dinner.close()
        if file_id_info_dinner == []:
            selected_recipe_id_dinner = ' '
        else:
            selected_recipe_id_dinner = file_id_info_dinner[0]

        file_cal_input_dinner = open('cal_dinner.txt', 'a')
        file_cal_input_dinner.write('')
        file_cal_input_dinner.close()

        file_cal_output_dinner = open('cal_dinner.txt', 'r')
        file_cal_info_dinner = file_cal_output_dinner.readlines()
        file_cal_output_dinner.close()
        if file_cal_info_dinner == []:
            total_calories_dinner = ' '
        else:
            total_calories_dinner = float(file_cal_info_dinner[0])

        file_name_input_dinner = open('name_dinner.txt', 'a')
        file_name_input_dinner.write('')
        file_name_input_dinner.close()

        file_name_output_dinner = open('name_dinner.txt', 'r')
        file_name_info_dinner = file_name_output_dinner.readlines()
        file_name_output_dinner.close()
        if file_name_info_dinner == []:
            selected_recipe_name_dinner = ' '
        else:
            selected_recipe_name_dinner = file_name_info_dinner[0]
        
        ingredients_label = tk.Button(self, text = "Ingredients", bg = "#f54c49", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(IngredientsPageDinner))
        ingredients_label.place(relwidth=0.4, relheight=0.1, relx = 0.1, rely = 0.1)
        
        instructions_label = tk.Button(self, text = "Instructions", bg = "#8953f6", fg = '#000', font = ('Roboto', 20), padx = 15, pady = 10, command=lambda: master.switch_frame(InstructionsPageDinner))
        instructions_label.place(relwidth=0.4, relheight=0.1, relx = 0.5, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.6, relx = 0.1, rely = 0.2)
        
        if total_calories_dinner != ' ' and selected_recipe_name_dinner != ' ' and selected_recipe_id_dinner != ' ':
            #Create frame and scroll bar
            my_frame = Frame(suggestion_1)
            my_scrollbary = Scrollbar(my_frame.master, orient = VERTICAL)
            my_scrollbarx = Scrollbar(my_frame.master, orient = HORIZONTAL)

            #Listbox
            my_listbox = Listbox(my_frame, xscrollcommand=my_scrollbarx.set, yscrollcommand=my_scrollbary.set, font = ('Roboto', 10, 'bold'))

            #configure scrollbar
            my_scrollbarx.config(command = my_listbox.xview)
            my_scrollbary.config(command = my_listbox.yview)
            my_scrollbarx.pack(side=BOTTOM, fill=X)
            my_scrollbary.pack(side=RIGHT, fill=Y)
            my_frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
            my_listbox.place(relx = 0, rely = 0, relwidth = 0.94, relheight = 1)

            my_listbox.insert(END, selected_recipe_name_dinner)
            my_listbox.insert(END, ' ')
            
            #Display Recipe Instructions
            recipe_instructions = requests.get('https://api.spoonacular.com/recipes/'+selected_recipe_id_dinner+'/analyzedInstructions' + api_key)
            recipe_instructions_json=recipe_instructions.json()

            for i in recipe_instructions_json:
              for n in i['steps']:
                #Step Number
                step_number = ('Step Number: ' + str(n['number']))
                my_listbox.insert(END, step_number)
                #Ingredients
                display_header = True
                for x in n['ingredients']:
                    if display_header == True:
                        my_listbox.insert(END,'Ingredients Needed For This Step:')
                        display_header = False
                    my_listbox.insert(END, x['localizedName'])
                #Equipment
                for y in n['equipment']:
                    my_listbox.insert(END, 'Equipment: ' + y['localizedName'])
                #Instructions
                my_listbox.insert(END, 'Instructions: ' + n['step'])
                my_listbox.insert(END, ' ')
        
        button_2 = tk.Button(self, text = "Home", bg = "#ccd1d9", fg = "#000", font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)
        
        add_change_recipe = tk.Button(self, text = "Add/Change Recipe", bg = "#ccd1d9", fg = '#000', font = ('Roboto', 10, 'bold'), command=lambda: master.switch_frame(DinnerPage))
        add_change_recipe.place(relwidth=0.4, relheight=0.05, relx = 0.3, rely = 0.8)

# --- Loop All Windows ---
master = BaseWindow()
master.mainloop()
