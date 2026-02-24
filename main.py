import tkinter as tk

def generate_band-name():

  city = city_entry.get()

  pet = pet_entry.get()

  result = "your band name could be "+ city + " " + pet

  result_label.config(text = result)

root = tk.tk()

root.title("BAND NAME GENERATOR")

root.geometry("400*300")

tk.Label(root,text = "city you grew up in:").pack()

city_entry.pack()

tk.Label(root,text = "pet.name:").pack()

pet_entry = tk.Entry
