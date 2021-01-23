# IMPORTANT please perform - pip install tkcalendar - before running the program.

from tkinter import *
from tkcalendar import *
import sqlite3
from tkinter import messagebox as mb

# Creating or Connecting to a database
conn = sqlite3.connect('activity_point.db')

# cursor
c = conn.cursor()

# table creation

c.execute("""CREATE TABLE IF NOT EXISTS points (
        name text,
        roll_no text,
        join_year text,
        branch text,
        dob text,
        points int
    )
    """)
conn.commit()  # connection commiting

conn.close()  # connection closing

root = Tk()
root.title("Activity Point Calculator")
name_var = StringVar()
roll_var = StringVar()
year_var = StringVar(root)
bra_var = StringVar(root)
year_var.set("2017")
bra_var.set("IT")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
dob = StringVar()
cal = Calendar(root, selectmode="day", year=2021, month=1, day=21)

points = 0


# root.configure(background='black')
def click():

    one = str(name_var.get())
    two = str(roll_var.get())
    three = str(year_var.get())
    four = str(bra_var.get())
    five = int(var1.get())
    six = int(var2.get())
    seven = int(var3.get())
    eight = int(var4.get())
    nine = int(var5.get())
    ten = str(cal.get_date())

    if five + six + seven +eight + nine == 5:
        point = 50
    elif five + six + seven +eight + nine == 4:
        point = 40
    elif five + six + seven +eight + nine == 3:
        point = 30
    elif five + six + seven +eight + nine == 2:  
        point = 20
    elif five + six + seven +eight + nine == 1:  
        point = 10
    elif five + six + seven +eight + nine == 1: 
        point = 0

    mb.showerror("Registered Data ",("You have been registered, Your Activity point is ",point))
    conn = sqlite3.connect('activity_point.db')
    c = conn.cursor()

    # inserting into table

    c.execute("INSERT INTO points VALUES (:name, :roll, :yearj, :branch, :date, :pts)",

              {
                  'name': one,
                  'roll': two,
                  'yearj': three,
                  'branch': four,
                  'date': ten,
                  'pts': point,
              }
              )

    c.execute("SELECT * FROM points")
    print(c.fetchall())
    
    conn.commit()
    conn.close()
     #Refreshes all the inputs and makes them empty
    inputName.delete(0,END)
    inputRoll.delete(0,END)
    acBox1.deselect()
    acBox2.deselect()
    acBox3.deselect()
    acBox4.deselect()
    acBox5.deselect()

# label definitions
space = Label(root, text=" ",)
nameLabel = Label(root, text="Name : ",)
rollLabel = Label(root, text="Roll Number : ")
yearLabel = Label(root, text="Year of study : ")
dobLabel = Label(root, text="Date of Birth : ")
braLabel = Label(root, text="Branch : ")
acLabel = Label(root, text="Activities Participated In")


# inputs
inputName = Entry(root, textvariable=name_var,)
inputRoll = Entry(root, textvariable=roll_var,)

inputYof = OptionMenu(root, year_var, "2017", "2018", "2019", "2020")
inputBra = OptionMenu(root, bra_var, "IT", "EC", "MECH", "EEE", "CIV")

acBox1 = Checkbutton(root, text="Music", variable=var1)
acBox2 = Checkbutton(root, text="Workshop", variable=var2)
acBox3 = Checkbutton(root, text="Literary", variable=var3)
acBox4 = Checkbutton(root, text="Internship", variable=var4)
acBox5 = Checkbutton(root, text="Volunteering", variable=var5)

myButton = Button(root, text="submit", command=click)

# label packings
nameLabel.grid(row=1, column=0)
rollLabel.grid(row=2, column=0)
yearLabel.grid(row=3, column=0)
dobLabel.grid(row=4, column=0)
braLabel.grid(row=5, column=0)
space.grid(row=6, column=1)
acLabel.grid(row=7, column=0)

# input packings
inputName.grid(row=1, column=1)
inputRoll.grid(row=2, column=1)
inputYof.grid(row=3, column=1)
cal.grid(row=4, column=1)
inputBra.grid(row=5, column=1)

space.grid(row=6, column=1)
acBox1.grid(row=7, column=1)
acBox2.grid(row=8, column=1)
acBox3.grid(row=9, column=1)
acBox4.grid(row=10, column=1)
acBox5.grid(row=11, column=1)
space.grid(row=12, column=1)

myButton.grid(row=13, column=1)

root.mainloop()  # looping until x is clicked
