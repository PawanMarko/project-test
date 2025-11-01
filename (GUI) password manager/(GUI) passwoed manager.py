# DAY 29 !!

import tkinter as tk 
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ----------------------------(password GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  
  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  
  password_list = password_letters + password_symbols + password_numbers
  
  shuffle(password_list)
  password = "".join(password_list)
  
  password_entry.delete(0, tk.END)
  password_entry.insert(0, password)
  
  # copy password to clipboard..
  window.clipboard_clear()
  window.clipboard_append(password)
  window.update()

  
# ---------------------------- SAVE(password ------------------------------- #
def save_password():
  website = websit_entry.get()
  email = email_entry.get()
  password =password_entry.get()
  new_data = {
    website: {
      "email": email,
      "password": password,
    }
  }
  
  if len(website) == 0 or len(email) == 0 or len(password) == 0:
    messagebox.showwarning(title="OOPs", message="Please don't leave any fields empty!")
    return
  else:
    try:
      with open("data.json", "r") as data_file:
        # reading old data..
        data = json.load(data_file)
        
    except FileNotFoundError:
      with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)
        
    else:
      # Updateing old data with new data..
      data.update(new_data)
      
      with open(r"C:\Users\Pawan Marko\data.json", "w") as data_file:
        #Saveing the updated data..
        json.dump(data, data_file, indent=4)

    finally:
      websit_entry.delete(0,tk.END)
      password_entry.delete(0, tk.END)
      
      
# find password!!

def find_password():
  website = websit_entry.get()
  try:
    with open("data.json")as data_file:
      data = json.load(data_file)
      
  except FileExistsError:
    messagebox.showinfo(title="website", message="No data Fil found")
    
  else:
    if website in data:
        email = data[website] ["email"]
        password = data[website] ["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
    else:
      messagebox.showinfo(title="Error", message="No detalis for {website} exists.")
      
      
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("..My(password Manager..")
window.config(padx=50, pady=50, bg="white")

# Canvas + logo
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = tk.PhotoImage(file=r"C:\Users\Pawan Marko\Documents\Coding\Python\logo.png") # make sure logo.png exists in same folder
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

# lables..
websit_lable = tk.Label(text="Websit:", bg="white")
websit_lable.grid(row=1, column=0)
email_lable = tk.Label(text="Email/Username:", bg="white")
email_lable.grid(row=2, column=0)
password_lable = tk.Label(text="Password:", background="white")
password_lable.grid(row=3, column=0)

# Entries..
websit_entry = tk.Entry(width=25)
websit_entry.grid(row=1, column=1)
websit_entry.focus() # Cursor starts here..

email_entry = tk.Entry(width=25)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "naruto@7gmail.com")# pre-fill with default email

password_entry = tk.Entry(width=25)
password_entry.grid(row=3, column=1) 


# BUTTON..
generate_button = tk.Button(text="Generate Passward", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tk.Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()
