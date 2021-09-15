from tkinter import *
root = Tk()
#Database
import sqlite3
conn = sqlite3.connect("Database")
cur = conn.cursor()

conn.execute(f'''CREATE TABLE IF NOT EXISTS Customers (
        qrcode INTEGER,
        FirstName TEXT,
        LastName TEXT,
        State TEXT,
        City TEXT,
        EmailAddress TEXT,
        ZipCode INTEGER,
        PhoneNumber INTEGER)''')

conn.execute(f'''CREATE TABLE IF NOT EXISTS Product (
        qrcode INTEGER,
        name TEXT,
        gradeRangeMinimum INTEGER,
        gradeRangeMaximum INTEGER,
        Price INTEGER)''')

conn.execute(f'''CREATE TABLE IF NOT EXISTS Sales (
        qrcode INTEGER,
        PersonsName TEXT,
        Date TEXT,
        Quantity INTEGER)''')

conn.commit()
conn.close()

def getCustomer(ID):
    cursor = sqlite3.connect("Database").cursor()
    cursor.execute('SELECT * FROM Customers')
    allcustomers = cursor.fetchall()

    for cusomer in allcustomers:
        if str(ID) == str(allcustomers[0]):
            print(cusomer)
            return cusomer

def RemoveFromDatabase(ID, modify):
    conn = sqlite3.connect("Database")
    conn.execute(f'''DELETE from Customers where id = {id}''')
    conn.commit()
    conn.close()

def EditSales():
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window")
    newWindow1.geometry("335x150")
    newWindow1.geometry("+300+300")
    newWindow1.configure(bg="black")

    Topframe = Frame(newWindow1, width=335, height=15)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="  Edit Sales", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    centerframe = Frame(newWindow1, width=31, height=15)
    centerframe.grid(row=1, column=0)
    centerframe.configure(bg='black')
    # Page1
    Top1 = Label(centerframe, text="Persons name", font=("Helvetica", 10))
    Top1.grid(row=0, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=0, column=3)
    Top1.configure(bg='black', fg='white')

    # Page1
    Top1 = Label(centerframe, text="Date", font=("Helvetica", 10))
    Top1.grid(row=1, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=1, column=3)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Quanity", font=("Helvetica", 10))
    Top1.grid(row=4, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=4, column=3)
    Top1.configure(bg='black', fg='white')

    Input = Button(centerframe, text="     Search     ")
    Input.grid(row=6, column=1)
    Input.configure(bg='grey', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=6, column=0)
    Top1.configure(bg='black', fg='white')

    Input = Button(centerframe, text="     Input     ", height=1)
    Input.grid(row=6, column=4)
    Input.configure(bg='grey', fg='white')

def EditProduct():
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window")
    newWindow1.geometry("335x150")
    newWindow1.geometry("+300+300")
    newWindow1.configure(bg="black")

    Topframe = Frame(newWindow1, width=335, height=15)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="  Edit Product", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    centerframe = Frame(newWindow1, width=31, height=15)
    centerframe.grid(row=1, column=0)
    centerframe.configure(bg='black')
    # Page1
    Top1 = Label(centerframe, text="Item name", font=("Helvetica", 10))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=0, column=1)
    Top1.configure(bg='black', fg='white')

    # Page1
    Top1 = Label(centerframe, text="Minimum grade level", font=("Helvetica", 10))
    Top1.grid(row=1, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=1, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Maximum grade level", font=("Helvetica", 10))
    Top1.grid(row=4, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=4, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Price", font=("Helvetica", 10))
    Top1.grid(row=5, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=5, column=1)
    Top1.configure(bg='black', fg='white')

    bottomframe = Frame(newWindow1, width=335, height=15)
    bottomframe.grid(row=6, column=0)
    bottomframe.configure(bg='grey')

    Input = Button(centerframe, text="     Search     ")
    Input.grid(row=6, column=1)
    Input.configure(bg='grey', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=6, column=0)
    Top1.configure(bg='black', fg='white')

    Input = Button(centerframe, text="     Input     ", height=1)
    Input.grid(row=6, column=3)
    Input.configure(bg='grey', fg='white')

def EditEmploee():
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window")
    newWindow1.geometry("335x150")
    newWindow1.geometry("+300+300")
    newWindow1.configure(bg="black")

    Topframe = Frame(newWindow1, width=335, height=15)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="  Edi Employee", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    centerframe = Frame(newWindow1, width=31, height=15)
    centerframe.grid(row=1, column=0)
    centerframe.configure(bg='black')
    # Page1
    Top1 = Label(centerframe, text="First Name", font=("Helvetica", 10))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=0, column=1)
    Top1.configure(bg='black', fg='white')

    # Page1
    Top1 = Label(centerframe, text=" Last Name", font=("Helvetica", 10))
    Top1.grid(row=0, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=0, column=3)
    Top1.configure(bg='black', fg='white')

    # Page1
    Top1 = Label(centerframe, text="Mailing Address", font=("Helvetica", 10))
    Top1.grid(row=1, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=1, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="City", font=("Helvetica", 10))
    Top1.grid(row=1, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=1, column=3)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="State", font=("Helvetica", 10))
    Top1.grid(row=4, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=4, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Zip Code", font=("Helvetica", 10))
    Top1.grid(row=4, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=4, column=3)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Email Address", font=("Helvetica", 10))
    Top1.grid(row=5, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=5, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Phone Number", font=("Helvetica", 10))
    Top1.grid(row=5, column=2)
    Top1.configure(bg='black', fg='white')

    CosumerID = Text(centerframe, width=5, height=1)
    CosumerID.grid(row=5, column=3)
    CosumerID.configure(bg='black', fg='white')

    #Input = Button(centerframe, text="     Search     ", command=lambda: getCustomer(CosumerID))
    #Input.grid(row=6, column=1)
    #Input.configure(bg='grey', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=6, column=0)
    Top1.configure(bg='black', fg='white')

    Input = Button(centerframe,text="     Input     ", height=1)
    Input.grid(row=6, column=3)
    Input.configure(bg='grey', fg='white')

def AddEmploee():
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window")
    newWindow1.geometry("335x150")
    newWindow1.geometry("+300+300")
    newWindow1.configure(bg="black")

    Topframe = Frame(newWindow1, width=335, height=15)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="  Add Employee", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    centerframe = Frame(newWindow1, width=31, height=15)
    centerframe.grid(row=1, column=0)
    centerframe.configure(bg='black')
    # Page1
    Top1 = Label(centerframe, text="First Name", font=("Helvetica", 10))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=0, column=1)
    Top1.configure(bg='black', fg='white')

    # Page1
    Top1 = Label(centerframe, text=" Last Name", font=("Helvetica", 10))
    Top1.grid(row=0, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=0, column=3)
    Top1.configure(bg='black', fg='white')

    # Page1
    Top1 = Label(centerframe, text="Mailing Address", font=("Helvetica", 10))
    Top1.grid(row=1, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=1, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="City", font=("Helvetica", 10))
    Top1.grid(row=1, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=1, column=3)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="State", font=("Helvetica", 10))
    Top1.grid(row=4, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=4, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Zip Code", font=("Helvetica", 10))
    Top1.grid(row=4, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=4, column=3)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Email Address", font=("Helvetica", 10))
    Top1.grid(row=5, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=5, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Phone Number", font=("Helvetica", 10))
    Top1.grid(row=5, column=2)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=5, column=3)
    Top1.configure(bg='black', fg='white')

    bottomframe = Frame(newWindow1, width=335, height=15)
    bottomframe.grid(row=6, column=0)
    bottomframe.configure(bg='grey')

    Input = Button(bottomframe,text="Input",width=46, height=1)
    Input.grid(row=0, column=0)
    Input.configure(bg='grey', fg='white')

def AddProduct():
    WndowProductAdd = Toplevel(root)
    WndowProductAdd.title("New Window")
    WndowProductAdd.geometry("335x150")
    WndowProductAdd.geometry("+300+300")
    WndowProductAdd.configure(bg="black")

    Topframe = Frame(WndowProductAdd, width=335, height=15)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="  Add Product", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    centerframe = Frame(WndowProductAdd, width=31, height=15)
    centerframe.grid(row=1, column=0)
    centerframe.configure(bg='black')
    # Page1
    Top1 = Label(centerframe, text="Item name",font=("Helvetica", 10))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    ItemName = Text(centerframe, width=5, height=1,textvariable=ProductName)
    ItemName.grid(row=0, column=1)
    ItemName.configure(bg='black', fg='white')

    # Page1
    Top1 = Label(centerframe, text="Minimum grade level", font=("Helvetica", 10))
    Top1.grid(row=1, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=1, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Maximum grade level", font=("Helvetica", 10))
    Top1.grid(row=4, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=4, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Price", font=("Helvetica", 10))
    Top1.grid(row=5, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=5, column=1)
    Top1.configure(bg='black', fg='white')

    bottomframe = Frame(WndowProductAdd, width=335, height=15)
    bottomframe.grid(row=6, column=0)
    bottomframe.configure(bg='grey')

    Input = Button(bottomframe, text="Input",command=ProductAdded, width=46, height=1)
    Input.grid(row=0, column=0)
    Input.configure(bg='grey', fg='white')

def AddSales():
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window")
    newWindow1.geometry("335x150")
    newWindow1.geometry("+300+300")
    newWindow1.configure(bg="black")

    Topframe = Frame(newWindow1, width=335, height=15)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="  Add Sales", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    centerframe = Frame(newWindow1, width=31, height=15)
    centerframe.grid(row=1, column=0)
    centerframe.configure(bg='black')
    # Page1
    Top1 = Label(centerframe, text="Persons name", font=("Helvetica", 10))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=0, column=1)
    Top1.configure(bg='black', fg='white')

    # Page1
    Top1 = Label(centerframe, text="Date", font=("Helvetica", 10))
    Top1.grid(row=1, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=1, column=1)
    Top1.configure(bg='black', fg='white')

    Top1 = Label(centerframe, text="Quanity", font=("Helvetica", 10))
    Top1.grid(row=4, column=0)
    Top1.configure(bg='black', fg='white')

    Top1 = Text(centerframe, width=5, height=1)
    Top1.grid(row=4, column=1)
    Top1.configure(bg='black', fg='white')

    bottomframe = Frame(newWindow1, width=335, height=15)
    bottomframe.grid(row=6, column=0)
    bottomframe.configure(bg='grey')

    Input = Button(bottomframe, text="Input", width=46, height=1)
    Input.grid(row=0, column=0)
    Input.configure(bg='grey', fg='white')

def employees():
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window")
    newWindow1.geometry("335x150")
    newWindow1.geometry("+300+300")
    newWindow1.configure(bg="black")

    Topframe = Frame(newWindow1, width=310, height=150)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="    employees", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')
    #EnterPerson
    middleframe = Frame(newWindow1, width=310, height=150)
    middleframe.grid(row=1, column=0)
    middleframe.configure(bg='black')

    # Set Buttons
    Employ = Label(middleframe, text="         ", height=4)
    Employ.configure(bg='black')
    Employ.grid(row=0, column=0)

    Employ = Button(middleframe, text="   Enter   \n   employ   ",command=AddEmploee, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=1)

    Employ = Label(middleframe, text="           ", height=4)
    Employ.configure(bg='black')
    Employ.grid(row=0, column=2)

    Employ = Button(middleframe, text="   Edit   \n   employ   ", command=EditEmploee, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=3)
    #goback
    Employ = Button(newWindow1, text="         Go Back To Welcome Page        ", font=("Helvetica", 14),command=newWindow1.destroy)
    Employ.configure(bg='grey')
    Employ.grid(row=2, column=0,columnspan=2)

def Product():
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window")
    newWindow1.geometry("335x150")
    newWindow1.geometry("+300+300")
    newWindow1.configure(bg="black")

    Topframe = Frame(newWindow1, width=310, height=150)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="             Products           ", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')
    #EnterPerson
    middleframe = Frame(newWindow1, width=310, height=150)
    middleframe.grid(row=1, column=0)
    middleframe.configure(bg='black')

    # Set Buttons
    Employ = Button(middleframe, text="   Enter   \n   Product   ",command=AddProduct, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=0)

    Employ = Label(middleframe, text="                 ", height=4)
    Employ.configure(bg='black')
    Employ.grid(row=0, column=1)

    Employ = Button(middleframe, text="   Edit   \n   Product   ", command=EditProduct, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=2)
    #goback
    Employ = Button(newWindow1, text="         Go Back To Welcome Page        ", font=("Helvetica", 14),command=newWindow1.destroy)
    Employ.configure(bg='grey')
    Employ.grid(row=2, column=0, columnspan=2)

def Sales():
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window")
    newWindow1.geometry("335x150")
    newWindow1.geometry("+300+300")
    newWindow1.configure(bg="black")

    Topframe = Frame(newWindow1, width=310, height=150)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="               Sales              ", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')
    #EnterPerson
    middleframe = Frame(newWindow1, width=310, height=150)
    middleframe.grid(row=1, column=0)
    middleframe.configure(bg='black')

    # Set Buttons
    Employ = Button(middleframe, text="     Edit     \n     Sales     ",command=EditSales, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=0)

    Employ = Label(middleframe, text="                 ", height=4)
    Employ.configure(bg='black')
    Employ.grid(row=0, column=1)

    Employ = Button(middleframe, text="     Enter     \n     Sales     ", command=AddSales, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=2)
    #goback
    Employ = Button(newWindow1, text="         Go Back To Welcome Page        ", font=("Helvetica", 14),command=newWindow1.destroy)
    Employ.configure(bg='grey')
    Employ.grid(row=2, column=0, columnspan=2)

def Reports():
    newWindow1 = Toplevel(root)
    newWindow1.title("New Window")
    newWindow1.geometry("335x150")
    newWindow1.geometry("+300+300")
    newWindow1.configure(bg="black")

    Topframe = Frame(newWindow1, width=310, height=150)
    Topframe.grid(row=0, column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="             Reports           ", font=("Helvetica", 25))
    Top1.grid(row=0, column=0)
    Top1.configure(bg='black', fg='white')
    #EnterPerson
    middleframe = Frame(newWindow1, width=310, height=150)
    middleframe.grid(row=1, column=0)
    middleframe.configure(bg='black')

    # Set Buttons
    Employ = Button(middleframe, text="Customer\nlist", font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=0)

    Employ = Label(middleframe, text="                 ", height=4)
    Employ.configure(bg='black')
    Employ.grid(row=0, column=1)

    Employ = Button(middleframe, text="Product\nSales", command=Product, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=2)
    #goback
    Employ = Button(newWindow1, text="     Go Back To Welcome Page    ", font=("Helvetica", 14),command=newWindow1.destroy)
    Employ.configure(bg='grey')
    Employ.grid(row=2, column=0,columnspan=2)

def StartingPage():
    root.geometry("335x150")
    root.configure(bg="black")
    root.geometry("+300+300")
    #top
    Topframe = Frame(root,width=310, height=150)
    Topframe.grid(row=0,column=0)
    Topframe.configure(bg='grey')
    # Page1
    Top1 = Label(Topframe, text="         Welcome         ",font=("Helvetica", 25))
    Top1.grid(row=0,column=0)
    Top1.configure(bg='black', fg='white')

    middleframe = Frame(root, width=310, height=150)
    middleframe.grid(row=1, column=0)
    middleframe.configure(bg='black')

    # Set Buttons
    Employ = Button(middleframe, text="Enter/Edit\nEmployees", command=employees, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=0)

    Employ = Label(middleframe, text=" ",height=4)
    Employ.configure(bg='black')
    Employ.grid(row=0, column=1)

    Employ = Button(middleframe, text="Enter/Edit\nProduct", command=Product, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=2)

    Employ = Label(middleframe, text=" ", height=4)
    Employ.configure(bg='black')
    Employ.grid(row=0, column=3)

    Employ = Button(middleframe, text="Enter/Edit\nSales", command=Sales, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=4)

    bottomframe = Frame(root, width=310)
    bottomframe.grid(row=2, column=0)
    bottomframe.configure(bg='grey')

    Employ = Button(bottomframe, text="                         Reports                         ", command=Reports, font=("Helvetica", 14))
    Employ.configure(bg='grey')
    Employ.grid(row=0, column=0)

#code starts here
StartingPage()
root.mainloop()