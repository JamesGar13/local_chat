from customtkinter import *
from PIL import Image, ImageFilter

window = CTk()
window.title("Photo Redactor")
window.geometry("800x700")

file = filedialog.askopenfilename(initialdir="/",)

image = Image.open(file)

img = CTkImage(light_image=image, size=(400, 400))
label = CTkLabel(window, image=img, text="")
label.pack()

def rotate():
    global image, img
    image = image.rotate(90, expand=True)
    img = CTkImage(light_image=image, size=(400, 400))
    label.configure(image=img)

def filter_sharpen():
    global image, img
    image = image.filter(ImageFilter.SHARPEN)
    img = CTkImage(light_image=image, size=(400, 400))
    label.configure(image=img)

def convertL():
    global image, img
    image = image.convert("L")
    img = CTkImage(light_image=image, size=(400, 400))
    label.configure(image=img)


btn1 = CTkButton(window, width=100, command=rotate)
btn2 = CTkButton(window, width=100, command=filter_sharpen)
btn3 = CTkButton(window, width=100, command=convertL)

label.pack()
btn1.pack(pady=20)
btn2.pack(pady=20)
btn3.pack(pady=20)



window.mainloop()
