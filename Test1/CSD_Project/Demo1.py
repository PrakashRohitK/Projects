from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox
from tkinter import ttk
import sqlite3
root = Tk()
root.geometry('900x900')
root.title("Registration Form")
ID=IntVar()
Fullname = StringVar()
Email = StringVar()
Age=IntVar()
var = StringVar()
s = StringVar()
var1 = StringVar()
Phone=IntVar()
Addr = StringVar()
def database():
    id = ID.get()
    name1 = Fullname.get()
    email = Email.get()
    gender = var.get()
    state = s.get()
    prog = var1.get()
    age=Age.get()
    phone=Phone.get()
    addr=Addr.get()

    conn = sqlite3.connect('Form.db')

    if(id!='' and name1!='' and email!='' and gender!='' and state!='' and prog!='' and age!='' and phone!=''and addr!=''):
        print("Connected to SQLite")
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS Student (ID INTEGER,Fullname TEXT,Email TEXT,Gender TEXT,State TEXT,TechSKills TEXT,Age INTEGER,PhoneNumber INTEGER,,Address TEXT)')
        cursor.execute(
            'INSERT INTO Student (ID,FullName,Email,Gender,State,TechSkills,Age,PhoneNumber,Address) VALUES(?,?,?,?,?,?,?,?,?)',
            (id, name1, email, gender, state, prog, age, phone,addr))
        conn.commit()
        print("Record added Successfully 👍 ")
        tkinter.messagebox.showinfo("Registration Form", "Thank You for Registering")
        # root.geometry('200x200')
    else:
        tkinter.messagebox.showinfo("Registration Form", "Please Fill All the Fields!!")

def deleteRecord():
    try:
        sqliteConnection = sqlite3.connect('Form.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        z1=input("Enter Id value to Delete:")
        # Deleting single record now
        cursor.execute(f"""DELETE from Student where id ={z1} """)
        sqliteConnection.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
def updateSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('Form.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        z1=input("Enter Column name:")
        z2=input("Enter updated value:")
        z3=input("Enter id value:")
        cursor.execute(f"UPDATE Student SET '{z1}'='{z2}' WHERE id='{z3}'")
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def Table_format():
    c = Toplevel(root)
    c.geometry('800x800')
    c.title("Details")
    tv = ttk.Treeview(c)
    style = ttk.Style()
    style.theme_use('clam')

    def fix_map(option):
        return [elm for elm in style.map('Treeview', query_opt=option)
                if elm[:2] != ('!disabled', '!selected')]

    style.map('Treeview', foreground=fix_map('foreground'),
              background=fix_map('background'))
    tv.tag_configure('bold', font=('', 0, 'bold'), foreground='red')

    tv['columns'] = ('ID', 'FULLNAME', 'EMAIL', 'GENDER', 'State','Tech Skills','Age','PhoneNumber','Address')
    tv.column('#0', width=0, stretch=NO)
    tv.column('ID', anchor=CENTER, width=120)
    tv.column('FULLNAME', anchor=CENTER, width=120)
    tv.column('EMAIL', anchor=CENTER, width=120)
    tv.column('GENDER', anchor=CENTER, width=120)
    tv.column('State', anchor=CENTER, width=120)
    tv.column('Tech Skills', anchor=CENTER, width=120)
    tv.column('Age', anchor=CENTER, width=120)
    tv.column('PhoneNumber', anchor=CENTER, width=120)
    tv.column('Address', anchor=CENTER, width=120)

    tv.heading('#0',text='', anchor=CENTER)
    tv.heading('ID', text='ID',anchor=CENTER)
    tv.heading('FULLNAME', text='FULLNAME',anchor=CENTER)
    tv.heading('EMAIL', text='EMAIL',anchor=CENTER)
    tv.heading('GENDER', text='GENDER',anchor=CENTER)
    tv.heading('State',text='State',anchor=CENTER)
    tv.heading('Tech Skills', text='Tech Skills',anchor=CENTER)
    tv.heading('Age',text='Age' ,anchor=CENTER)
    tv.heading('PhoneNumber', text='PhoneNumber',anchor=CENTER)
    tv.heading('Address', text='Address', anchor=CENTER)
    conn = sqlite3.connect("Form.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Student")
    rows = cur.fetchall()
    for row in rows:
        tv.insert("", tkinter.END, values=row)
    conn.close()
    tv.pack()
img=Image.open(r"F:\Downloads\bg.jpg")
img1=img.resize((1000, 1000))
back_end=ImageTk.PhotoImage(img1)
lb=Label(root,image=back_end)
lb.place(x=0,y=0,height=900,width=900)
label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)
root.wm_attributes('-transparentcolor', '#ab23ff')
label_1 = Label(root, text="ID", width=10, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=ID)
entry_1.place(x=270, y=130)
label_2 = Label(root, text="FullName", width=15, font=("bold", 10))
label_2.place(x=80, y=170)

entry_2 = Entry(root, textvar=Fullname)
entry_2.place(x=270, y=170)

label_3 = Label(root, text="Email", width=10, font=("bold", 10))
label_3.place(x=80, y=210)

entry_3 = Entry(root, textvar=Email)
entry_3.place(x=270, y=210)

label_4 = Label(root, text="Gender", width=10, font=("bold", 10))
label_4.place(x=80, y=260)

Radiobutton(root, text="Male", padx=5, variable=var, value="Male").place(x=270, y=260)
Radiobutton(root, text="Female", padx=20, variable=var, value="Female").place(x=350, y=260)

label_5 = Label(root, text="State", width=10, font=("bold", 10))
label_5.place(x=80, y=300)

list1 = ['Andhra Pradesh', 'Telangana', 'Maharashtra', 'Bihar', 'TamilNadu', 'MadhyaPradesh','Chhattisgarh','Haryana'];

droplist = OptionMenu(root, s, *list1)
droplist.config(width=15)
s.set('Select Your State')
droplist.place(x=270, y=300)

label_6 = Label(root, text="Tech Skills", width=12, font=("bold", 10))
label_6.place(x=80, y=350)
Radiobutton(root, text="Java", variable=var1,value="Java").place(x=270, y=350)
Radiobutton(root, text="Python", variable=var1,value="Python").place(x=350, y=350)
Radiobutton(root, text="C", variable=var1,value="C").place(x=430, y=350)
Radiobutton(root, text="Mysql", variable=var1,value="Mysql").place(x=510, y=350)
Radiobutton(root, text="ALL", variable=var1,value="ALL").place(x=590, y=350)
label_7 = Label(root, text="Age", width=10, font=("bold", 10))
label_7.place(x=80, y=390)

entry_7 = Entry(root, textvar=Age)
entry_7.place(x=270, y=390)
label_8 = Label(root, text="PhoneNumber", width=10, font=("bold", 10))
label_8.place(x=80, y=420)

Phone_entry_8 = Entry(root,textvar=Phone)
Phone_entry_8.place(x=270, y=420)
label_9 = Label(root, text="Address", width=15, font=("bold", 10))
label_9.place(x=80, y=470)
addr_entry_9 = Entry(root,textvar=Addr)
addr_entry_9.place(x=270, y=470,width=200,
        height=70)
Button(root, text='Submit', width=20, bg='white', fg='black', command=database).place(x=180, y=590)
Button(root, text='View Data', width=20, bg='white', fg='black', command=Table_format).place(x=400, y=590)
def display_msg():
    tkinter.messagebox.showinfo(title='Form', message='🙂Thank You🙂')
    root.destroy()

root.protocol('WM_DELETE_WINDOW', display_msg)

image1 = Image.open("images1.png")
test1 = ImageTk.PhotoImage(image1)
label1 = Label(image=test1)
label1.image = test1
label1.place(x=550, y=75)
while True:
    print('''
             *******************************************
            | 🙂Welcome to Student Registration Form!🙂| 
            |You can do the following operations:       |
            |1) Add a Record                            |
            |2) Update a Record                         |
            |3) Delete a Record                         |
            |4) End the system                          |
             *******************************************
            ''')
    option = int(input("Enter an option: "))
    if option==1: root.mainloop()
    elif option==2: updateSqliteTable()
    elif option==3: deleteRecord()
    elif option==4:
        print("Thank you")
        break
    else:
        print("Enter a valid option!")
"""
while True:
    print('''
             *******************************************
            | 🙂Welcome to Student Registration Form!🙂 | 
            |You can do the following operations:       |
            |1) Add a Record                            |
            |2) Update a Record                         |
            |3) Delete a Record                         |
            |4) End the system                          |
             *******************************************
            ''')
    option = int(input("Enter an option: "))
    if option==1: root.mainloop()
    elif option==2: updateSqliteTable()
    elif option==3: deleteRecord()
    elif option==4:
        print("Thank you")
        break
    else:
        print("Enter a valid option!")


"""