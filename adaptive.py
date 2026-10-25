from customtkinter import *

window = CTk()

window.title("Adaptive Window")
window.geometry("400x400")
window.configure(fg_color="gray")

btn1 = CTkButton(window, text="Click me", fg_color="red")


btn1.place(
    relx=1,
    rely=1,
    anchor="se"
)

window.mainloop()

