import pyodbc
from tkinter import messagebox


def connect_database():
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=MARIA_HP\\SQLEXPRESS;'
                              'DATABASE=master;'  # Use master to create the new database
                              'Trusted_Connection=yes;')
        mycursor = conn.cursor()

    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong: {e}')
        return

    try:
        # Create the database if it doesn't exist (run separately to avoid multi-statement transaction issue)
        mycursor.execute('''
            IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'Employee_database')
            BEGIN
                EXEC('CREATE DATABASE Employee_database')
            END
        ''')
        conn.commit()  # Commit the database creation

        # Use the newly created database
        mycursor.execute('USE Employee_database')

        # Create the table if it doesn't exist
        mycursor.execute('''
            IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'data')
            CREATE TABLE data (
                Id VARCHAR(20), 
                Name VARCHAR(50), 
                Job VARCHAR(50), 
                Team VARCHAR(20), 
                Manager VARCHAR(50), 
                Salary DECIMAL(10,2), 
                Phone VARCHAR(14), 
                Email VARCHAR(100)
            )
        ''')
        conn.commit()  # Commit the table creation

        messagebox.showinfo('Success', 'Database and table created successfully!')

    except Exception as e:
        messagebox.showerror('Error', f'Error while creating database or table: {e}')

    finally:
        # Clean up
        mycursor.close()
        conn.close()


def insert(id, name, job, team, manager, salary, telephone, email):
    print('insert')


connect_database()
