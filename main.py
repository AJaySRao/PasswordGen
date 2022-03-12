from tkinter import *
from turtle import width

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=256, height=256)
t_image = PhotoImage(file='icon.png')
canvas.create_image(123, 123, image=t_image)
canvas.grid(row=0, column=1)

#Labels-------------------------
website = Label(text='Website:')
website.grid(row=1, column=0)

username = Label(text='Email/Username:')
username.grid(row=2, column=0)

password = Label(text='Password:')
password.grid(row=3, column=0)

#Entry fields--------------------
website_field = Entry(width=35)
website_field.grid(row=1, column=1, columnspan=2, sticky='EW')

un_field = Entry(width=35)
un_field.grid(row=2, column=1, columnspan=2, sticky='EW')

pw_field = Entry(width=21)
pw_field.grid(row=3, column=1, sticky='EW')

#Buttons--------------------------
pwd_btn = Button(text='Generate Password')
pwd_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=36)
add_btn.grid(row=4, column=1 , columnspan=2, sticky='EW')

window.mainloop()