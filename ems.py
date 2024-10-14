
from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database



#Functions
def add_employee():
    if idEntry.get()=='' or nameEntry.get()=='' or  teamEntry.get()=='' or managerEntry.get()=='' or salaryEntry.get()=='' or telephoneEntry.get()=='' or emailEntry.get()=='':
       messagebox.showerror('Error', 'All fields are required')
    else:
        database.insert(idEntry.get(), nameEntry.get(), jobBox.get(), teamEntry.get, managerEntry.get(), salaryEntry.get(), telephoneEntry.get(), emailEntry.get() )
#GUI PART
window=CTk()
window.geometry('1030x680+100+100')
window.resizable(False,False)
window.title('Employee Management System')
window.configure(fg_color='#0e6655')
logo=CTkImage(Image.open('emsimage.jpg'),size=(1030,168))
logoLabel=CTkLabel(window,image=logo, text='')
logoLabel.grid(row=0, column=0, columnspan=2)

leftFrame=CTkFrame(window, fg_color='#0e6655')
leftFrame.grid(row=1, column=0)

idLabel=CTkLabel(leftFrame, text='Employee Id', font=('arial', 18, 'bold'),text_color='white')
idLabel.grid(row=0, column=0, padx=20, pady=15, sticky='w')

idEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
idEntry.grid(row=0, column=1)

nameLabel=CTkLabel(leftFrame, text='Employee Name', font=('arial', 18, 'bold'),text_color='white')
nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky='w')

nameEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
nameEntry.grid(row=1, column=1)

jobLabel=CTkLabel(leftFrame, text='Job Role', font=('arial', 18, 'bold'),text_color='white')
jobLabel.grid(row=2, column=0, padx=20, pady=15, sticky='w')
job_options=['Full-Stack Developer', 'DevOps Engineer', 'Data Scientist', 'Business Analyst', 'Delivery Manager',
             'Network Engineer', 'UX/UI Desjgner', 'IT Consultant', 'Technical Writer', 'Team Leader']
jobBox=CTkComboBox(leftFrame, values=job_options, font=('arial', 15),width=180, state='readonly')
jobBox.grid(row=2, column=1)

teamLabel=CTkLabel(leftFrame, text='Team', font=('arial', 18, 'bold'),text_color='white')
teamLabel.grid(row=3, column=0, padx=20, pady=15, sticky='w')

teamEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
teamEntry.grid(row=3, column=1)

managerLabel=CTkLabel(leftFrame, text='Line Manger', font=('arial', 18, 'bold'),text_color='white')
managerLabel.grid(row=4, column=0, padx=20, pady=15, sticky='w')

managerEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
managerEntry.grid(row=4, column=1)

salaryLabel=CTkLabel(leftFrame, text='Annual Salary', font=('arial', 18, 'bold'),text_color='white')
salaryLabel.grid(row=5, column=0, padx=20, pady=15, sticky='w')

salaryEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
salaryEntry.grid(row=5, column=1)

telephoneLabel=CTkLabel(leftFrame, text='Telephone', font=('arial', 18, 'bold'),text_color='white')
telephoneLabel.grid(row=6, column=0, padx=20, pady=15, sticky='w')

telephoneEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
telephoneEntry.grid(row=6, column=1)

emailLabel=CTkLabel(leftFrame, text='Email', font=('arial', 18, 'bold'),text_color='white')
emailLabel.grid(row=7, column=0, padx=20, pady=15, sticky='w')

emailEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
emailEntry.grid(row=7, column=1)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1, column=1)

search_options=['Employee Id', 'Employee Name', 'Job Role', 'Team', 'Line Manager', 'Annual Salary',
                'Phone number', 'email' ]
searchBox=CTkComboBox(rightFrame, values=search_options, font=('arial', 15),state='readonly')
searchBox.grid(row=0, column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame, font=('arial', 15, 'bold'))
searchEntry.grid(row=0, column=1)

searchButton=CTkButton(rightFrame,  text='Search', width=100)
searchButton.grid(row=0, column=2)

showallButton=CTkButton(rightFrame,  text='Show All', width=100)
showallButton.grid(row=0, column=3, pady=5)

tree=ttk.Treeview(rightFrame, height =13)
tree.grid(row=1, column=0, columnspan=4)

tree['columns']=('Employee Id', 'Employee Name', 'Job Role', 'Team', 'Line Manager', 'Annual Salary',
                'Phone Number', 'Email')
tree.heading('Employee Id', text='Employee Id')
tree.heading('Employee Name', text='Employee Name')
tree.heading('Job Role', text='Job Role')
tree.heading('Team', text='Team')
tree.heading('Line Manager', text='Line Manager')
tree.heading('Annual Salary', text='Annual Salary')
tree.heading('Phone Number', text='Phone Number')
tree.heading('Email', text='Email')

tree.config(show='headings')
tree.column('Employee Id', anchor=CENTER, width=100)
tree.column('Employee Name', anchor=CENTER, width=115)
tree.column('Job Role', anchor=CENTER, width=100)
tree.column('Team', anchor=CENTER, width=80)
tree.column('Line Manager', anchor=CENTER, width=100)
tree.column('Annual Salary', anchor=CENTER, width=100)
tree.column('Phone Number', anchor=CENTER, width=110)
tree.column('Email', anchor=CENTER, width=100)

style=ttk.Style()
style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))

scrollbar=ttk.Scrollbar(rightFrame, orient=VERTICAL,)
scrollbar.grid(row=1, column=4, sticky='ns')

buttonFrame=CTkFrame(window, fg_color='#0e6655')
buttonFrame.grid(row=2, column=0, columnspan=2)

newButton=CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15 )
newButton.grid(row=0, column=0, pady=5)

addButton=CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15,
                    command=add_employee)
addButton.grid(row=0, column=1, pady=5, padx=5)

updateButton=CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15 )
updateButton.grid(row=0, column=2, pady=5, padx=5)

deleteButton=CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15 )
deleteButton.grid(row=0, column=3, pady=5, padx=5)

deleteallButton=CTkButton(buttonFrame, text='Delete All', font=('arial', 15, 'bold'), width=160, corner_radius=15 )
deleteallButton.grid(row=0, column=4, pady=5, padx=5)
window.mainloop()