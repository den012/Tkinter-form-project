from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()

root.geometry("1000x800")
root.configure(bg="#ffffff")
root.title("App")

# fonts
Font_title = ("Comic Sans MS", 22, "bold")
Font_tuple = ("Comic Sans MS", 16, "bold")
Font_button = ("Comic Sans MS", 13)

# LOGIC
# create table
'''
cursor.execute("""CREATE TABLE addresses(
    firstName text,
    lastName text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")'''


# create functions
def checkEntry():
    check=None
    if fName.get=="" or lName.get=="" or address.get()=="" or city.get=="" or state.get()=="" or zipcode.get()=="":
        check=False
    else:
        check=True


def delete():
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    cursor = conn.cursor()

    # delete a record
    cursor.execute("DELETE from addresses WHERE oid=" + deleteBox.get())
    # commit changes
    conn.commit()

    # close connection
    conn.close()


def submit():
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    cursor = conn.cursor()

    # Insert Into table
    if checkEntry():
        cursor.execute("INSERT INTO addresses VALUES(:fName,:lName,:address,:city,:state,:zipcode)",
                       {
                           'fName': fName.get(),
                           'lName': lName.get(),
                           'address': address.get(),
                           'city': city.get(),
                           'state': state.get(),
                           'zipcode': zipcode.get()
                       })

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear the text box
    fName.delete(0, END)
    lName.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT *,oid FROM addresses")
    records = cursor.fetchall()
    print(records)

    printRecords = ""
    '''for record in records:
        printRecords += "First name: " + str(record[0]) + "\n" + "Last name: " + str(
            record[1]) + "\n" + "Address: " + str(record[2]) + "\n" + "State: " + str(
            record[3]) + "\n" + "Id: " + str(record[6]) + "\n\n"'''

    # create new window
    newWindow = Toplevel()

    totalRows = len(records)
    totalCols = len(records[0]) if records else 0

    for i in range(totalRows):
        for j in range(totalCols):
            e = Entry(newWindow, width=20, fg='pink', font=Font_tuple)
            e.grid(row=i, column=j)
            e.insert(END, records[i][j])

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# img
addButon = ImageTk.PhotoImage(Image.open("addbuton.png"))
showButon = ImageTk.PhotoImage(Image.open("showbuton.png"))
deleteButon = ImageTk.PhotoImage(Image.open("delete.png"))

canvas = Canvas(
    root,
    bg="#ffffff",
    height=800,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    500.0, 400.0,
    image=background_img)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    655.5, 294.5,
    image=entry0_img)

fName = Entry(
    bd=0,
    bg="#f3f3f3",
    highlightthickness=0,
    font=Font_tuple)

fName.place(
    x=558.5, y=275,
    width=194.0,
    height=37)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    297.5, 294.5,
    image=entry1_img)

lName = Entry(
    bd=0,
    bg="#f3f3f3",
    highlightthickness=0,
    font=Font_tuple
)

lName.place(
    x=200.5, y=275,
    width=194.0,
    height=37)

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(
    297.5, 376.5,
    image=entry2_img)

address = Entry(
    bd=0,
    bg="#f3f3f3",
    highlightthickness=0,
    font=Font_tuple
)

address.place(
    x=200.5, y=357,
    width=194.0,
    height=37)

entry3_img = PhotoImage(file=f"img_textBox3.png")
entry3_bg = canvas.create_image(
    650.5, 458.5,
    image=entry3_img)

city = Entry(
    bd=0,
    bg="#f3f3f3",
    highlightthickness=0,
    font=Font_tuple
)

city.place(
    x=553.5, y=439,
    width=194.0,
    height=37)

entry4_img = PhotoImage(file=f"img_textBox4.png")
entry4_bg = canvas.create_image(
    650.5, 376.5,
    image=entry4_img)

state = Entry(
    bd=0,
    bg="#f3f3f3",
    highlightthickness=0,
    font=Font_tuple)

state.place(
    x=553.5, y=357,
    width=194.0,
    height=37)

entry5_img = PhotoImage(file=f"img_textBox5.png")
entry5_bg = canvas.create_image(
    297.5, 458.5,
    image=entry5_img)

zipcode = Entry(
    bd=0,
    bg="#f3f3f3",
    highlightthickness=0,
    font=Font_tuple)

zipcode.place(
    x=200.5, y=439,
    width=194.0,
    height=37)

entry6_img = PhotoImage(file=f"img_textBox6.png")
entry6_bg = canvas.create_image(
    665.5, 552.0,
    image=entry6_img)

deleteBox = Entry(
    bd=0,
    bg="#f3f3f3",
    highlightthickness=0,
    font=Font_tuple
)

deleteBox.place(
    x=635.0, y=521,
    width=61.0,
    height=60)

# Create submit button
submitButton = Button(root, image=addButon, borderwidth=0, highlightthickness=0, command=submit)
submitButton.place(x=160, y=510)

# create query button
queryButton = Button(root, image=showButon, borderwidth=0, highlightthickness=0, command=query)
queryButton.place(x=200, y=600)

# create a delete button
deleteButton = Button(root, image=deleteButon, borderwidth=0, highlightthickness=0, command=delete)
deleteButton.place(x=570, y=600)

root.resizable(False, False)
root.mainloop()
