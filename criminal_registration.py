import sqlite3
import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import re
import random

window = tk.Tk()
window.geometry("700x700")
window.title("REGISTRATION FORM")
window.configure(background="grey")

Fullname = tk.StringVar()
address = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.StringVar()
var = tk.IntVar()
age = tk.IntVar()
file_path = ""
status = tk.StringVar()
registerno = tk.StringVar()

value = random.randint(1, 1000)
print(value)

def show():
    global file_path
    file_path = askopenfilename(initialdir="D:\criminal_identification (2) (1) DATA ADDED\criminal_identification/profile images", title='Select Image', filetypes=[("all files", "*.*")])
    
    print(file_path)
    return file_path

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB():
    global file_path
    fname = Fullname.get()
    addr = address.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    photo1 = file_path
    Status = status.get()
    Reg = registerno.get()

    errors = []
    if not all([fname, addr, email, mobile, gender, Status, Reg]):
        errors.append("All fields are required.")

    if len(mobile) != 10 or not mobile.isdigit():
        errors.append("Mobile number should be exactly 10 digits and contain only digits.")

    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        errors.append("Invalid email address.")

    if not photo1:
        errors.append("Please upload a photo.")

    if time <= 0:
        errors.append("Age should be greater than 0.")

    if errors:
        ms.showerror("Error", "\n".join(errors))
        return

    try:
        sqliteConnection = sqlite3.connect('evaluation.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM registration WHERE registerno=?", (Reg,))
        if cursor.fetchone():
            ms.showerror("Error", "Registration number should be unique.")
            return

        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO registration
                                  (Fullname, address, Email, Phoneno, Gender, age , photo, status, registerno) 
                                  VALUES (?,?,?,?,?,?,?,?,?)"""

        empPhoto = convertToBinaryData(photo1)
        data_tuple = (fname, addr, email, mobile, gender, time, empPhoto, Status, Reg)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")
    ms.showinfo("Criminal Record", "Criminal Registration Completed !!")
    window.destroy()

image2 = Image.open('slide.jpg')
image2 = image2.resize((700, 700))
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(window, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="#192841", fg="white")
l1.place(x=190, y=50)

l2 = tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=130, y=150)
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=330, y=150)

l3 = tk.Label(window, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l3.place(x=130, y=200)
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=330, y=200)

l5 = tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l5.place(x=130, y=250)
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=330, y=250)

l6 = tk.Label(window, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l6.place(x=130, y=300)
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=330, y=300)

l7 = tk.Label(window, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l7.place(x=130, y=350)
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=var, value=1).place(x=330, y=350)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=var, value=2).place(x=440, y=350)

l8 = tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l8.place(x=130, y=400)
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=330, y=400)

l4 = tk.Button(window, text="Upload Photo :", width=12, font=("Times new roman", 15, "bold"), bg="snow", command=show)
l4.place(x=130, y=450)

l9 = tk.Label(window, text="Status :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l9.place(x=130, y=500)

list1 = ['Criminal Person', 'Missing Person']
droplist = tk.OptionMenu(window, status, *list1)
droplist.config(width=20)
status.set('Select Status of Person')
droplist.place(x=330, y=500)

l10 = tk.Label(window, text="Register No.", width=13, font=("Times new roman", 15, "bold"), bg="snow")
l10.place(x=130, y=550)

t10 = tk.Entry(window, textvar=registerno, width=20, font=('', 15), show="*")
t10.place(x=330, y=550)

btn = tk.Button(window, text="Register", bg="#192841", font=("", 20), fg="white", width=9, height=1, command=insertBLOB)
btn.place(x=260, y=620)

window.mainloop()
