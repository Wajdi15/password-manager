from tkinter import *
from tkinter import messagebox
from template import *
import pyperclip
import json
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list.extend([random.choice(symbols) for char in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for char in range(nr_numbers)])
    random.shuffle(password_list)

    new_password = "".join(password_list)
    password[1].delete(0, END)
    password[1].insert(END, string=new_password)
    pyperclip.copy(new_password)  # The password to be copied to the clipboard.


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_website = website[1].get()  # get the entry value
    new_username = user_name[1].get()
    new_password = password[1].get()
    new_data = {new_website: {"password": new_password, "user_name": new_username}}
    if len(new_website) > 0 and len(new_password) > 0 and len(new_username) > 0:
        is_ok = messagebox.askokcancel(title=new_website, message="Are you sure ?")
        if is_ok:
            # Use try catch to create a file if we got a FileNotFoundError
            try:
                with open("my_passwords.json", "r") as my_passwords:
                    data = json.load(my_passwords)
                    data.update(new_data)
                with open("my_passwords.json", "w") as my_passwords:
                    json.dump(data, my_passwords, indent=2)
            except FileNotFoundError:
                with open("my_passwords.json", "w") as my_passwords:
                    json.dump(new_data, my_passwords, indent=2)
            finally:
                website[1].delete(0, END)  # get the entry value
                user_name[1].delete(0, END)
                password[1].delete(0, END)

    else:
        messagebox.showerror(title="Oops",
                             message="Please dont leave any fields empty!")  # a popup for showing a error message


def search():
    try:
        with open("my_passwords.json", "r") as my_passwords:
            data = json.load(my_passwords)
            website_value = website[1].get()  # get the entry value
            if website_value in data:
                messagebox.showinfo(title=website_value,
                                    message=f"user_name : {data[website_value]['user_name']}\npassword : {data[website_value]['password']}")
            else:
                messagebox.showerror(title="Not found", message="This website is not in your saved accounts")
    except FileNotFoundError:
        messagebox.showerror(title="Not found", message="Add accounts to the list first")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
# canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
# inputs
# return a list content the label and the input in case you need to use config
website = input_template("Website :", 21, 0, 1)
user_name = input_template("Email/Username :", 21, 0, 2)
password = input_template("Password :", 21, 0, 3)
# buttons
search = btn_template("Search", grid_column=2, grid_row=1, btn_width=15,command=search)
generate = btn_template("Generate Password", grid_column=2, grid_row=3, btn_width=15,command=password_generator)
Add = btn_template("Add", grid_column=1, grid_row=4, btn_width=18, command=save)
window.mainloop()
