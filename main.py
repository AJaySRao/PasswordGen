from tkinter import *

window = Tk()
window.title("Password Generator")
window.config(padx=100, pady=60, )
#window.wm_attributes('-transparentcolor', GREEN)

canvas = Canvas(width=600, height=600, highlightthickness=0)
t_image = PhotoImage(file='icon.png')
canvas.create_image(300, 112, image=t_image)
#time_text = canvas.create_text(100, 130, text='00:00', font=('Ariel', 35, 'bold'), fill='white' )
canvas.grid(column=1, row=1)


window.mainloop()