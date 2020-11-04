import requests
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, Text
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

        # --- Profile START ---
        profile_button = tk.Button(self, bg = "#000")
        profile_button.place(relwidth = 0.3, relheight = 0.12, relx = 0.1, rely = 0.12)
        profile_label = tk.Label(self, text = "Your Profile", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.45, rely = 0.15)
        # ---------------------

        # --- Meal Planner START ---

        meal_label = tk.Label(self, text = "Monday", bg = "#fff", fg = "#000", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
        meal_label.place(relx = 0.05, rely = 0.26)

        previous_button = tk.Button(self, text = "<", bg = "#000")
        previous_button.place(relwidth = 0.075, relheight = 0.15, relx = 0, rely = 0.47)

        next_button = tk.Button(self, text = ">", bg = "#000")
        next_button.place(relwidth = 0.075, relheight = 0.15, relx = 0.925, rely = 0.47)

        frame_3 = tk.Frame(self, bg = "#4953f6")
        frame_3.place(relwidth = 0.8, relheight = 0.15, relx = 0.1, rely = 0.32)

        frame_4 = tk.Frame(self, bg = "#6953f4")
        frame_4.place(relwidth = 0.8, relheight = 0.15, relx = 0.1, rely = 0.47)

        frame_5 = tk.Frame(self, bg = "#8953f3")
        frame_5.place(relwidth = 0.8, relheight = 0.15, relx = 0.1, rely = 0.62)

        button_1 = tk.Button(self, text = "Suggestions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(SuggestionsPage))
        button_1.place(relwidth = 0.2, relheight = 0.05, relx = 0.1, rely = 0.9,)

        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.35, rely = 0.9)

        button_2 = tk.Button(self, text = "Planner", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)

        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.65, rely = 0.9)

        button_3 = tk.Button(self, text = "Instructions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(InstructionsPage))
        button_3.place(relwidth = 0.2, relheight = 0.05, relx = 0.7, rely = 0.9)

        # ------------------------

class SuggestionsPage(tk.Canvas):
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

        profile_label = tk.Label(self, text = "Recipe Suggestions", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.05, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.2)

        suggestion_2 = tk.Frame(self, bg = "#8953f6")
        suggestion_2.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.5)

        suggestion_3 = tk.Frame(self, bg = "#8953f6")
        suggestion_3.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.8)

        button_1 = tk.Button(self, text = "Suggestions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(SuggestionsPage))
        button_1.place(relwidth = 0.2, relheight = 0.05, relx = 0.1, rely = 0.9,)

        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.35, rely = 0.9)

        button_2 = tk.Button(self, text = "Planner", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)

        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.65, rely = 0.9)

        button_3 = tk.Button(self, text = "Instructions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(InstructionsPage))
        button_3.place(relwidth = 0.2, relheight = 0.05, relx = 0.7, rely = 0.9)
        
class InstructionsPage(tk.Canvas):
    def __init__(self, suggestions):
        tk.Canvas.__init__(self, suggestions)
        tk.Canvas(self, height=896, width=414, bg="#fff").pack()

        tk.Label(self, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20).place(relx = 0.05, rely = 0)

        profile_label = tk.Label(self, text = "Instructions", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
        profile_label.place(relx = 0.05, rely = 0.1)

        suggestion_1 = tk.Frame(self, bg = "#8953f6")
        suggestion_1.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.2)

        suggestion_2 = tk.Frame(self, bg = "#8953f6")
        suggestion_2.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.6)
        '''
        '''
        suggestion_3 = tk.Frame(self, bg = "#8953f6")
        suggestion_3.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.26)

        suggestion_4 = tk.Frame(self, bg = "#8953f6")
        suggestion_4.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.26)

        button_1 = tk.Button(self, text = "Suggestions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(SuggestionsPage))
        button_1.place(relwidth = 0.2, relheight = 0.05, relx = 0.1, rely = 0.9,)

        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.35, rely = 0.9)

        button_2 = tk.Button(self, text = "Planner", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(MainPage))
        button_2.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)

        separator = tk.Frame(self, bg = "#000")
        separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.65, rely = 0.9)

        button_3 = tk.Button(self, text = "Instructions", bg = "#ccd1d9", fg = "#000", command=lambda: master.switch_frame(InstructionsPage))
        button_3.place(relwidth = 0.2, relheight = 0.05, relx = 0.7, rely = 0.9)

# --- Loop All Windows ---
master = BaseWindow()
master.mainloop()

# --- THE PROGRAM BEHIND THE APP ---

#search recipe
food = str(input('what u wanna eat?: '))
print('')
request_search_recipe = requests.get('https://api.spoonacular.com/recipes/complexSearch'+api_key+'&query='+food)
request_search_recipe_json=request_search_recipe.json()
print(request_search_recipe_json)

for i in request_search_recipe_json['results']:
    print(i['title'])
    print(i['id'])
    print('')

#get recipe instructions/info
input_id = str(input('what is the id of the recipe you want?: '))

print('')
recipe_instructions = requests.get('https://api.spoonacular.com/recipes/'+ input_id+'/analyzedInstructions' + api_key)

recipe_instructions_json=recipe_instructions.json()

print(recipe_instructions_json)

for i in recipe_instructions_json:
    for n in i['steps']:
        #Step Number
        print('Step Number: ' + str(n['number']))
        #Ingredients
        display_header = True
        for x in n['ingredients']:
            while display_header == True:
                print('Ingredients List:')
                display_header = False
            print(x['localizedName'])
        #Equipment
        for y in n['equipment']:
            print('Equipment: ' + y['localizedName'])
        #Instructions
        print('Instructions: ' + n['step'])
        print('')

#get recipe nutrition calorie stuff

recipe_nutrition = requests.get('https://api.spoonacular.com/recipes/1003464/nutritionWidget.json' + api_key)

recipe_nutrition_json = recipe_nutrition.json()
calories = recipe_nutrition_json['calories']

recipe_info = requests.get('https://api.spoonacular.com/recipes/1003464/information?apiKey=782bba4ef5fd462d81b2102ebb96fe55&includeNutrition=false')

recipe_info_json = recipe_info.json()
servings = recipe_info_json['servings']

total_calories = input(str('how many cal u eat: '))

calorie_adjustment_ratio = float(total_calories)/float(calories)
adjusted_servings= round(float(total_calories)*(float(servings)/float(calories)),0)
print('This will create about ' + str(adjusted_servings) + ' serving(s) from this meal')
print('')
#adjust amount of ingredient to match desired calorie size
ingredients_info = requests.get('https://api.spoonacular.com/recipes/1003464/ingredientWidget.json'+api_key)

ingredients_info_json = ingredients_info.json()
#print(ingredients_info_json)
for i in ingredients_info_json['ingredients']:
    print(i['name'])
    (i['amount']).popitem()
    for j in ((i['amount']).values()):
        print(j['value'])
        adjusted_value = (j['value'])*calorie_adjustment_ratio
        round(adjusted_value,2)
        print(str(adjusted_value) + ' ' + str(j['unit']))
        print('')