from customtkinter import *
import random
import string

window = CTk()
window.title("Password Generator")
window.geometry("500x500")

title = CTkLabel(
    window,
    text="Password Generator",
    font=("Arial", 24)
)
title.pack(pady=20)

password = CTkEntry(
    window,
    width=350,
    height=40,
    font=("Arial", 18)
)
password.pack(pady=10)

frame = CTkFrame(
    window,
    width=350,
    height=350,
    fg_color="white",
)
frame.pack_propagate(False)
frame.pack(pady=10)


lowercase = CTkCheckBox(
    frame,
    text="Lowercase letters (a-z)"
)

uppercase = CTkCheckBox(
    frame,
    text="Uppercase letters (A-Z)"
)

numbers = CTkCheckBox(
    frame,
    text="Numbers (0-9)"
)

special = CTkCheckBox(
    frame,
    text="Special characters (!@#$...)"
)


lowercase.grid(row=0, column=0, padx=20, pady=10, sticky="w")
uppercase.grid(row=1, column=0, padx=20, pady=10, sticky="w")
numbers.grid(row=2, column=0, padx=20, pady=10, sticky="w")
special.grid(row=3, column=0, padx=20, pady=10, sticky="w")

def print_text():
    symbols = ""

    if lowercase.get():
        symbols += string.ascii_lowercase

    if uppercase.get():
        symbols += string.ascii_uppercase

    if numbers.get():
        symbols += string.digits

    if special.get():
        symbols += string.punctuation

    if symbols == "":
        password.configure(placeholder_text="Choose something!")
        return

    result = ""

    for i in range(10):
        result += random.choice(symbols)

    password.delete(0, "end")
    password.insert(0, result)


generate_btn = CTkButton(
    frame,
    text="Generate",
    width=200,
    height=40,
    command=print_text
)

generate_btn.grid(row=4, column=0, padx=20, pady=20,)


window.mainloop()




