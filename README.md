# BAND-NAME-GENERATOR
This is a Band Name Generator. It is written using python. 

import tkinter as tk

def generate_band_name():

  city = city_entry.get()
  
  pet = pet_entry.get()
  
  result = "your band name could be" + city + " " + pet
  
  result_label.config(text = result)

root = tk.tk()

root.title("band name generator ")

root.geometry("400*300)

tk.label(root,text = "city you grew up in:").pack()

city_entry.pack()

tk.label(root,text="pet.name:").pack

pet.entry = tk.entry
