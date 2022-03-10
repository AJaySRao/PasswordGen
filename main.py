from tkinter import *
from turtle import width

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=40)
#window.wm_attributes('-transparentcolor', GREEN)

canvas = Canvas(width=256, height=256, highlightthickness=0)
t_image = PhotoImage(file='icon.png')
canvas.create_image(123, 123, image=t_image)
#time_text = canvas.create_text(100, 130, text='00:00', font=('Ariel', 35, 'bold'), fill='white' )
canvas.grid(row=0, column=1)


website = Label(text='Website:', font= ('Courier', 12, 'normal'))
website.grid(row=1, column=0)

username = Label(text='Email/Username:', font= ('Courier', 12, 'normal'))
username.grid(row=2, column=0)

password = Label(text='Password:', font= ('Courier', 12, 'normal'))
password.grid(row=3, column=0)

website_field = Entry(width=35)
website_field.grid(row=1, column=1, columnspan=3)

un_field = Entry(width=35)
un_field.grid(row=2, column=1, columnspan=3)

pw_field = Entry(width=21)
pw_field.grid(row=3, column=1)

g_pwd = Button(text='Generate Password', font= ('Courier', 10, 'normal'))
g_pwd.grid(row=3, column=2 , columnspan=2)


window.mainloop()