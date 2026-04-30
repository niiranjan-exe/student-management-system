import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="electronics123",
    database="studentmanagementsystem1")
mycursor = con.cursor()
def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions','Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications','Id Already Exist try another id...',parent=addroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenmttable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='LightSteelBlue2')
    addroot.resizable(False,False)
#----------------------------------------------------------------------- Add studenmt Labels-------------------------------------------------------------------------------

    idlabel = Label(addroot,text='Enter Id : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text='Enter Address : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text='Enter D.O.B : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

####----------------------------------------------------------- Add student Entry---------------------------------------------------------------------------------------------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
############-------------------------------------------------- add button ---------------------------------------------------------------------------
    
    submitbtn = Button(addroot,text='Submit',font=('times',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='OliveDrab3',command=submitadd)
    submitbtn.place(x=100,y=420)



    addroot.mainloop()

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")

        def execute_search(query, param):
            mycursor.execute(query, (param,))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

        try:
            if id:
                execute_search('SELECT * FROM studentdata1 WHERE id=%s', id)
            if name:
                execute_search('SELECT * FROM studentdata1 WHERE name=%s', name)
            elif mobile:
                execute_search('SELECT * FROM studentdata1 WHERE mobile=%s', mobile)
            elif email:
                execute_search('SELECT * FROM studentdata1 WHERE email=%s', email)
            elif address:
                execute_search('SELECT * FROM studentdata1 WHERE address=%s', address)
            elif gender:
                execute_search('SELECT * FROM studentdata1 WHERE gender=%s', gender)
            elif dob:
                execute_search('SELECT * FROM studentdata1 WHERE dob=%s', dob)
            elif addeddate:
                execute_search('SELECT * FROM studentdata1 WHERE addeddate=%s', addeddate)
            else:
                messagebox.showwarning('Input Error', 'Please enter at least one search criteria')
        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}')
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='LightSteelBlue2')

    searchroot.resizable(False,False)
#------------------------------------------------------------------------------ Add studenmt Labels-------------------------------------------
    idlabel = Label(searchroot,text='Enter Id : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text='Enter Mobile : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text='Enter Email : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(searchroot,text='Enter Address : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text='Enter Gender : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(searchroot,text='Enter D.O.B : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(searchroot,text='Enter Date : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

#----------------------------------------------------------- Add student Entry -----------------------------------------------------------------------

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    
############---------------------------------------------------- add button --------------------------------------------------------------------
    
    submitbtn = Button(searchroot,text='Submit',font=('times',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='OliveDrab3',command=search)
    submitbtn.place(x=100,y=480)



    searchroot.mainloop()
    
def deletestudent():
    try:
        cc = studenmttable.focus()
        content = studenmttable.item(cc)
        pp = content['values'][0]
        strr = 'DELETE FROM studentdata1 WHERE id=%s'
        mycursor.execute(strr, (pp,))
        con.commit()
        messagebox.showinfo('Notifications', f'Id {pp} deleted successfully...')
        
        strr = 'SELECT * FROM studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenmttable.insert('', END, values=vv)
    except Exception as e:
        messagebox.showerror('Error', f'Error: {e}')

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenmttable.insert('', END, values=vv)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='LightSteelBlue2')
    updateroot.resizable(False,False)


#---------------------------------------------------------------- Add studenmt Labels-------------------------------------------------------------------------
    
    idlabel = Label(updateroot,text='Enter Id : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter Name : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text='Enter Mobile : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text='Enter Email : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(updateroot,text='Enter Address : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text='Enter Gender : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(updateroot,text='Enter D.O.B : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text='Enter Date : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel = Label(updateroot,text='Enter Time : ',bg='LightSteelBlue4',font=('times',20,'bold'),fg='LightGoldenrod1',relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)

##-------------------------------------------------------------- Add student Entry -------------------------------------------------------------------
    
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=dateval)
    timeentry.place(x=250,y=490)
    
#------------------------------------------------------------------ add button ----------------------------------------------------------------------
    
    submitbtn = Button(updateroot,text='Submit',font=('times',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='OliveDrab3',command=update)
    submitbtn.place(x=100,y=540)
    cc = studenmttable.focus()
    content = studenmttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()
def showstudent():
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenmttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenmttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))


def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        root.destroy()


#********************************************************** Connecttion of Database **************************************************************
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected connected to the database ....',parent=dbroot)

        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database ....',parent=dbroot)
        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='dark slate blue')
#-------------------------------------------------------------- Connectdb Labels --------------------------------------------------------------------
    
    hostlabel = Label(dbroot,text="Enter Host : ",bg='LightGoldenrod1',font=('times',20,'bold'),relief=GROOVE
                      ,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='LightGoldenrod1',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='LightGoldenrod1',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

#--------------------------------------------------------------- Connectdb Entry -------------------------------------------------------------------------
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('times',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('times',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('times',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

#-------------------------------------------------------- Connectdb button -------------------------------------------------------------------------
    
    submitbutton = Button(dbroot,text='Submit',font=('times',15,'bold'),bg='OliveDrab3',bd=5,width=20,activebackground='blue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=110,y=190)

    dbroot.mainloop()
    
#**************************************************************************************************************************************************
    
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='  Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)
    
#********************************************************************* INTRO SLIDER ********************************************************************
    
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title('Student Management System')
root.config(bg='LightSteelBlue2')
root.geometry('1360x700+0+0')

root.resizable(True,True)

################################################################### Frames #########################################################################

##---------------------------------------------------------------------------- dataentry frame -----------------------------------------------------

DataEntryFrame = Frame(root,bg='LightSteelBlue4',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel = Label(DataEntryFrame,text='--------------Welcome--------------',width=30,font=('times',22,' bold'),bg='LightSteelBlue4',fg='LightGoldenRod1')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('times',20,'bold'),bd=6,bg='LightGoldenRod1',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('times',20,'bold'),bd=6,bg='LightGoldenRod1',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('times',20,'bold'),bd=6,bg='LightGoldenRod1',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('times',20,'bold'),bd=6,bg='LightGoldenRod1',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('times',20,'bold'),bd=6,bg='LightGoldenRod1',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export data',width=25,font=('times',20,'bold'),bd=6,bg='LightGoldenRod1',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7.  Exit',width=25,font=('times',20,'bold'),bd=6,bg='LightGoldenRod1',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

##---------------------------------------------------------- Show data frame ---------------------------------------------------------------------------

ShowDataFrame = Frame(root,bg='black',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=770,height=600)

##---------------------------------------------------------  Showdataframe ----------------------------------------------------------------------------

style = ttk.Style()
style.configure('Treeview.Heading',font=('times',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),background='grey95',foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenmttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                         yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenmttable.xview)
scroll_y.config(command=studenmttable.yview)
studenmttable.heading('Id',text='Id')
studenmttable.heading('Name',text='Name')
studenmttable.heading('Mobile No',text='Mobile No')
studenmttable.heading('Email',text='Email')
studenmttable.heading('Address',text='Address')
studenmttable.heading('Gender',text='Gender')
studenmttable.heading('D.O.B',text='D.O.B')
studenmttable.heading('Added Date',text='Added Date')
studenmttable.heading('Added Time',text='Added Time')
studenmttable['show'] = 'headings'
studenmttable.column('Id',width=100)
studenmttable.column('Name',width=200)
studenmttable.column('Mobile No',width=200)
studenmttable.column('Email',width=300)
studenmttable.column('Address',width=200)
studenmttable.column('Gender',width=100)
studenmttable.column('D.O.B',width=150)
studenmttable.column('Added Date',width=150)
studenmttable.column('Added Time',width=150)
studenmttable.pack(fill=BOTH,expand=1)

############################################################## Slider ##############################################################################

ss = '* Welcome to Student Management System *'
count = 0
text = ''

##################################

SliderLabel = Label(root,text=ss,font=('times',29,' bold'),relief=RIDGE,borderwidth=4,width=35,bg='dark slate grey',fg='LightGoldenRod1')
SliderLabel.place(x=260,y=2)

############################################################## clock ##################################################################################

clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='green yellow')
clock.place(x=2,y=2)
tick()

########################################################## ConnectDatabaseButton #####################################################################

connectbutton = Button(root,text='Connect To Database',width=16,font=('times',18,' bold'),relief=RIDGE,borderwidth=4,bg='green yellow',
                       activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=1125,y=2)
root.mainloop()