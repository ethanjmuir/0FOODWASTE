import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, Text
import os

# --- Window Itself ---
root = tk.Tk()
# --- Background Layer --- 
canvas = tk.Canvas(root, height=896, width=414, bg="#fff")
canvas.pack()
# --- Right-Most Scrollbar ---

scrollbar = tk.Scrollbar(root, bg = "#fff")
scrollbar.place(relwidth = 0.5, relheight = 1.0, relx = 0.95, rely = 0)

canvas.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = canvas.yview)

mainTitle = tk.Label(root, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20)
mainTitle.place(relx = 0.05, rely = 0)

profile_label = tk.Label(root, text = "Recipe Suggestions", bg = "#fff", fg = '#000', font = ('Roboto', 25), padx = 15, pady = 10)
profile_label.place(relx = 0.05, rely = 0.1)

suggestion_1 = tk.Frame(root, bg = "#8953f6")
suggestion_1.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.2)

suggestion_2 = tk.Frame(root, bg = "#8953f6")
suggestion_2.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.5)

suggestion_3 = tk.Frame(root, bg = "#8953f6")
suggestion_3.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 0.8)

suggestion_4 = tk.Frame(root, bg = "#8953f6")
suggestion_4.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 1.4)

suggestion_5 = tk.Frame(root, bg = "#8953f6")
suggestion_5.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 1.8)

suggestion_2 = tk.Frame(root, bg = "#8953f6")
suggestion_2.place(relwidth = 0.8, relheight = 0.2, relx = 0.1, rely = 2.2)

root.mainloop()