from tkinter import *


def input_template(label_title, input_width, grid_column, grid_row, columnspan=None):
    """Generate a a simple text input"""
    label = Label(text=label_title)
    label.grid(column=grid_column, row=grid_row)
    input = Entry(width=input_width)
    input.grid(column=grid_column + 1, row=grid_row, columnspan=columnspan)
    return [label, input]


def btn_template(text,grid_column, grid_row, command, btn_width=None, btn_height=None, columnspan=None):
    btn = Button(text=text, command=command, width=btn_width, height=btn_height)
    btn.grid(column=grid_column, row=grid_row, columnspan=columnspan)
    return btn
