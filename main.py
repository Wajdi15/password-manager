from tkinter import *
from template import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


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
website = input_template("Website :", 35, 0, 1, columnspan=2)
user_name = input_template("Email/Username :", 35, 0, 2, columnspan=2)
password = input_template("Password :", 21, 0, 3)
# buttons
generate = btn_template("Generate Password", grid_column=2, grid_row=3)
Add = btn_template("Add", grid_column=1, grid_row=4, btn_width=36, columnspan=2)

window.mainloop()
