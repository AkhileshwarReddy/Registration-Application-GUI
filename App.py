from tkinter import *
from tkinter.ttk import *
import zerosms

def test():
    n = name.get()
    p = phone.get()
    e = email.get()
    g = gender.get()
    dob = com_3.get()+"/"+com_2.get()+"/"+com_1.get()
    root.destroy()
    f=open("sdetails.txt","a+")
    if g==1:
        msg = "\nName : "+n+"\n"+"Phone No : "+p+"\n"+"Email : "+e+"\n"+"DoB : "+dob+"\n"+"Gender: Male\n\n"
    else:
        msg = "\nName : "+n+"\n"+"Phone No : "+p+"\n"+"Email : "+e+"\n"+"DoB : "+dob+"\n"+"Gender: Female\n\n"
    f.write(msg)
    f.write("_____________________________________________________________")
    
    sendsms(p, msg)


def sendsms(p, msg):
    root = Tk()
    root.geometry("300x300")
    lbl = Label(root,text="Member Registered Successfully", font = ("comic Sans Ms",10))
    lbl.pack()
    user = "" #your Way2sms phone number
    pass = "" #your Way2sms password
    zerosms.sms(phno=user,passwd=pass,message=msg,receivernum=p)


root = Tk()
root.geometry("300x300")
root.title("Registration Form")

#Labels

lbl_1 = Label(root, text="Name       : ", font=("comic Sans Ms",10)).grid(row=0,column=0)
lbl_2 = Label(root, text="Phone No : ", font=("comic Sans Ms",10)).grid(row=1,column=0)
lbl_3 = Label(root, text="Email      : ", font=("comic Sans Ms",10)).grid(row=2,column=0)
lbl_4 = Label(root, text="DOB       :", font=("comic Sans Ms",10)).grid(row=3,column=0)
lbl_5 = Label(root, text="Year:", font=("comic Sans Ms",10)).grid(row=4,column=0,sticky=W)
lbl_6 = Label(root, text="Month:", font=("comic Sans Ms",10)).grid(row=5,column=0,sticky=W)
lbl_7 = Label(root, text="Date:", font=("comic Sans Ms",10)).grid(row=6,column=0,sticky=W)
lbl_7 = Label(root, text="Gender   :", font=("comic Sans Ms",10)).grid(row=7,column=0,sticky=W)



name = StringVar()
phone = StringVar()
email = StringVar()
gender = IntVar()

#Entry's

ent_1 = Entry(root, width=30, textvariable=name).grid(row=0,column=1)
ent_2 = Entry(root, width=30, textvariable=phone).grid(row=1,column=1)
ent_3 = Entry(root, width=30, textvariable=email).grid(row=2,column=1)

#Combo Box for DOB

com_1 = Combobox(root)
com_2 = Combobox(root)
com_3 = Combobox(root)

com_1['values'] = ("----",'1995','1996','1997','1998','1999','2000')
com_2['values'] = ("---", 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
com_3['values'] = ("--",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)

com_1.current(0)
com_2.current(0)
com_3.current(0)

com_1.grid(row=4,column=1,sticky=W)
com_2.grid(row=5,column=1,sticky=W)
com_3.grid(row=6,column=1,sticky=W)

#Radio buttons for gender

rad_1 = Radiobutton(root, text='Male', value=1, variable=gender).grid(row=7,column=1,sticky=E)
rad_2 = Radiobutton(root, text='Female', value=2, variable=gender).grid(row=7,column=1,sticky=W)

# Submit Button

sub = Button(root, text = "Submit", command=test).grid(row=10,column=1,sticky=W)


root.mainloop()
