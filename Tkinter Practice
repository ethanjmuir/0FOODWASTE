import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, Text
import os

# --- Establishing the Window Itself ---
root = tk.Tk()
# --- Background Layer --- 
canvas = tk.Canvas(root, height=896, width=414, bg="#fff")
canvas.pack()

# --- "Zero Food Waste Program" Title ---
mainTitle = tk.Label(root, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20)
mainTitle.place(relx = 0.05, rely = 0)

# --- Profile START ---
profile_button = tk.Button(root, bg = "#000")
profile_button.place(relwidth = 0.3, relheight = 0.12, relx = 0.1, rely = 0.12)

profile_label = tk.Label(root, text = "Your Profile", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
profile_label.place(relx = 0.45, rely = 0.15)
# --- Profile END ---

# --- Suggestions START ---
suggestions_label = tk.Label(root, text = "Recipe Suggestions", bg = "#fff", fg = "#000", font = ('Roboto', 18, 'bold'), padx = 15, pady = 5)
suggestions_label.place(relx = 0.05, rely = 0.26)

previous_button = tk.Button(root, text = "<", bg = "#000")
previous_button.place(relwidth = 0.075, relheight = 0.2, relx = 0, rely = 0.32)

next_button = tk.Button(root, text = ">", bg = "#000")
next_button.place(relwidth = 0.075, relheight = 0.2, relx = 0.925, rely = 0.32)

frame_3 = tk.Frame(root, bg = "#8953f6")
frame_3.place(relwidth = 0.35, relheight = 0.2, relx = 0.1, rely = 0.32)

frame_4 = tk.Frame(root, bg = "#e9574f")
frame_4.place(relwidth = 0.35, relheight = 0.2, relx = 0.55, rely = 0.32)

button_1 = tk.Button(root, text = "< Previous Page", bg = "#000")
button_1.place(relwidth = 0.35, relheight = 0.05, relx = 0.1, rely = 0.535)

separator = tk.Frame(root, bg = "#000")
separator.place(relwidth = 0.005, relheight = 0.05, relx = 0.5, rely = 0.535)

button_2 = tk.Button(root, text = "Next Page >", bg = "#000")
button_2.place(relwidth = 0.35, relheight = 0.05, relx = 0.55, rely = 0.535)
# --- Suggestions END ---

# --- Portions Adjustment Box START ---
frame_5 = tk.Frame(root, bg = "#3c1da2")
frame_5.place(relwidth = 0.8, relheight = 0.3, relx = 0.1, rely = 0.6)

adjust_portions = tk.Label(root, text = "Adjust Portions", bg = "#3c1da2", fg = "#fff", font = ('Roboto', 25), padx = 15, pady = 10)
adjust_portions.place(relx = 0.1, rely = 0.6)

people_amount = tk.Label(root, text = "People Amount", bg = "#3c1da2", fg = "#f54c49", font = ('Roboto', 20), padx = 15, pady = 10)
people_amount.place(relx = 0.1, rely = 0.7)

entry_1 = tk.Entry(root, bg = "#f54c49")
entry_1.place(relwidth = 0.3, relheight = 0.05, relx = 0.55, rely = 0.71)

average_cals = tk.Label(root, text="Average Calories", bg = "#3c1da2", fg = "#f54c49", font = ('Roboto', 20), padx = 15, pady = 10)
average_cals.place(relx = 0.1, rely = 0.8)

entry_2 = tk.Entry(root, bg = "#f54c49")
entry_2.place(relwidth = 0.3, relheight = 0.05, relx = 0.55, rely = 0.81)
# --- Portions Adjustment Box END ---

root.mainloop()
