import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, Text
import os

root = tk.Tk()
canvas = tk.Canvas(root, height=896, width=414, bg="#fff")
canvas.pack()

mainTitle = tk.Label(root, text="Zero Food Waste", bg = "#fff", fg = '#000', font = ('Roboto', 30, 'bold'), padx = 15, pady = 20)
mainTitle.place(relx = 0.05, rely = 0)

profile_button = tk.Button(root, bg = "#000")
profile_button.place(relwidth = 0.3, relheight = 0.15, relx = 0.1, rely = 0.12)

frame_2v2 = tk.Label(root, text="Your Profile", bg="#fff", fg='#000', font = ('Roboto', 25, 'bold'), padx = 15, pady = 15)
frame_2v2.place(relx = 0.45, rely = 0.15)

frame_3 = tk.Frame(root, bg = "#8953f6")
frame_3.place(relwidth = 0.35, relheight = 0.2, relx = 0.1, rely = 0.3)

frame_4 = tk.Frame(root, bg = "#e9574f")
frame_4.place(relwidth = 0.35, relheight = 0.2, relx = 0.55, rely = 0.3)

frame_5 = tk.Frame(root, bg = "#3c1da2")
frame_5.place(relwidth = 0.8, relheight = 0.3, relx = 0.1, rely = 0.6)

root.mainloop()