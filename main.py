from tkinter import *
from tkinter import messagebox
from template import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_website = website[1].get()  # get the entry value
    new_username = user_name[1].get()
    new_password = password[1].get()
    if len(new_website) > 0 and len(new_password) > 0 and len(new_username) > 0:
        is_ok = messagebox.askokcancel(title=new_website, message="Are you sure ?")
        if is_ok:
            with open("my_passwords.txt", "a") as my_passwords:
                my_passwords.write(f"{new_website} | {new_username} | {new_password}\n")
                website[1].delete(0, END)  # get the entry value
                user_name[1].delete(0, END)
                password[1].delete(0, END)
    else:
        messagebox.showerror(title="Oops", message="Please dont leave any fields empty!")  # a popup for showing a error message


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
generate = btn_template("Generate Password", grid_column=2, grid_row=3, command=save)
Add = btn_template("Add", grid_column=1, grid_row=4, btn_width=36, command=save, columnspan=2)
window.mainloop()
