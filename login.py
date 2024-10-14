import customtkinter
from customtkinter import *
from PIL import Image
from customtkinter import CTkImage
from tkinter import messagebox

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Please Enter Valid Username and Password')
    elif usernameEntry.get() == 'maria' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'You have successfully logged in')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Incorrect Username/Password')

root=CTk()
root.geometry('930x487')
root.resizable(0, 0)
root.title('Login page')
image= CTkImage(Image.open('loginimage.jpg'),size=(630,387))
imageLabel=CTkLabel(root,image=image, text='')
imageLabel.place(x=10,y=50)

headingLabel=CTkLabel(root,text='Employee Management System', font=customtkinter.CTkFont(family='Goudy Old Style',
                                                                                         size=20, weight='bold'),
                                                                                         text_color='#75A2A5')
headingLabel.place(x=660, y=50)

usernameEntry= CTkEntry(root, placeholder_text='Enter Your Username', width=180)
usernameEntry.place(x=700,y=120)

passwordEntry= CTkEntry(root, placeholder_text='Enter Your Password', width=180, show='*')
passwordEntry.place(x=700,y=190)

loginButton=CTkButton(root, text='Login', width=180, command=login)
loginButton.place(x=700, y=260)

root.mainloop()