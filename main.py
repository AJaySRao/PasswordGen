from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json


#----------------------------------------------Password Generator-----------------------------------------------
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]  
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter+password_numbers+password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    pw_field.insert(0, password)
    pyperclip.copy(password)

#-----------------------------------------------------FUNCTION------------------------------------------------
def search_m():
    website = website_field.get()
    try:
        with open('data.json', 'r') as doc_search:
            text = json.load(doc_search)
    except FileExistsError:
        messagebox.showerror(title='Error', message="No data file found!")
    else:
        if website in text:
            messagebox.showinfo(title=website, message=f"Email: {text[website]['email']} \nPassword: {text[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f'No details for {website} exists!')
            

def data_write(content):
    with open("data.json", 'w') as doc:
        json.dump(content, doc, indent=4)

def add_data():
    website_data = website_field.get()
    email_data = un_field.get()
    pw_data = pw_field.get()

    new_data = {
        website_data:{
            "email": email_data,
            "password": pw_data
        }
    }
    
    if len(website_data) == 0 or len(pw_data) == 0:
        messagebox.showwarning(title='Warning', message="Please don't leave any fileds empty!")
    else:
        ok = messagebox.askokcancel(title='Website', message=f'These are the details entered: \nEmail: {email_data}\nPassword: {pw_data}')
        if ok:
            try:
                with open("data.json", "r") as doc:
                    data = json.load(doc) #Read old data

            except FileNotFoundError:
                data_write(new_data)

            else:
                data.update(new_data) #Update old data with new data
                data_write(data)

            website_field.delete(0, END)
            pw_field.delete(0, END)

#----------------------------------------------------------UI---------------------------------------------------
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=256, height=256)
t_image = PhotoImage(file='icon.png')
canvas.create_image(123, 123, image=t_image)
canvas.grid(row=0, column=1)

#Labels------------------------------------------------------
website = Label(text='Website:')
website.grid(row=1, column=0)

username = Label(text='Email/Username:')
username.grid(row=2, column=0)

password = Label(text='Password:')
password.grid(row=3, column=0)

#Entry fields-------------------------------------------------
website_field = Entry(width=11)
website_field.grid(row=1, column=1, sticky='EW')
website_field.focus()

un_field = Entry(width=25)
un_field.grid(row=2, column=1, columnspan=2, sticky='EW')
un_field.insert(0, '@gmail.com')

pw_field = Entry(width=11)
pw_field.grid(row=3, column=1, sticky='WE')

#Buttons-------------------------------------------------------
search_btn = Button(text='Search', width=15, command=search_m)
search_btn.grid(row=1, column=2)

pwd_btn = Button(text='Generate Password', width=15, command=generate_pass)
pwd_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=25, command=add_data)
add_btn.grid(row=4, column=1 , columnspan=2, sticky='EW')




window.mainloop()