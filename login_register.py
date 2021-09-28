import tkinter
from tkinter import *
import time
import os
from tkinter import messagebox
from tkinter import font

main_screen = Tk()
main_screen.geometry("500x500")
main_screen.configure(bg="#9893cc")
global username
global password
global gender
global verdict
global login_pass
global username_entry
global password_entry
username = StringVar()
password = StringVar()
gender = StringVar()
login_pass = StringVar()

def result():
    global result_screen
    dash_screen.destroy()
    result_screen = Toplevel()
    result_screen.title('Results')
    result_screen.geometry("500x500")
    result_screen.configure(bg="#b1e3db")
    file_data = open(username.get(),"r")
    file_data = file_data.read()
    file_data = file_data.split('\n')
    Label(result_screen,text="Result of Student: "+username.get(),font=('Arial',20),bg="#b1e3db").place(x=150,y=55)
    Frame(result_screen,height=270,width=350,bg="black").place(x=100,y=100)
    reg_number = Label(result_screen,text="JSC REGISTRATION NUMBER : "+file_data[2],fg="White",bg="black",font=('Arial',10)).place(x=150,y=170)
    roll_number = Label(result_screen,text="JSC ROLL NUMBER : "+file_data[3],bg="black",fg="white",font=('Arial',10)).place(x=150,y=200)
    gpa = Label(result_screen,text="JSC GPA : "+file_data[4],bg="black",fg="white",font=('Arial',10)).place(x=150,y=235)
    
    return




# validating the login screen

def login_validate():

    list = os.listdir()
    if username.get() not in list:
        messagebox.showerror("Error","Account not found!!")
        return 
    if username.get() == "" or password.get() == "" :
            messagebox.showerror("Error","All fields required")
            return 
    else:
        file_data = open(username.get(),"r")
        file_data = file_data.read()
        file_data = file_data.split('\n')
        login_pass = file_data[0]
        
        if login_pass == password.get():
            messagebox.showinfo("Login","Account logged in successfully!")   
            log_screen.destroy() 
            
            # opening a dashboard for the user
            global dash_screen
            dash_screen = Toplevel()
            dash_screen.title("Student Profile")
            dash_screen.configure(bg="#d6e3b1")
            dash_screen.geometry("500x500")
            Label(dash_screen,text="Welcome "+username.get(),font=('Arial',20),bg="#d6e3b1").place(x=185,y=55)
            Frame(dash_screen,height=270,width=300,bg="black").place(x=100,y=100)
            # results option
            Button(dash_screen,text="View Results",height=2,width=10,command=result).place(x=210,y=150)
            Button(dash_screen,text="View Payment",height=2,width=10).place(x=210,y=220)
            

            dash_screen.mainloop()

            return 
        if login_pass != password.get():
            messagebox.showerror("Error","Incorrect username or password!")
            return

# validating the register screen    
  
def register_validate():
    found = False
    list = os.listdir()
    if username.get() == "" or password.get() == "" or gender.get() == "":
        messagebox.showerror("Error","All fields required")
        return 
    for name in list:
        if username.get() not in list:
            # creating a username file
            file = open(username.get(),"w")
            file.write(password.get())
            file.write("\n")
            file.write(gender.get())
            file.close()
            # creating a username_result file
            file = open(username.get()+'_result',"w")
            file.close()

            # creating a username_payment file
            file = open(username.get()+'_payment',"w")
            for i in range(0,12):
                file.write('Not Paid'+'\n')
            file.close()
            messagebox.showinfo("Register",f"Account successfully registered with username {username.get()}")
            reg_screen.destroy()
            return   
        else:
            messagebox.showerror("Error",f"{username.get()} already exists!")
            return 
            
# register screen
def register():
    global reg_screen
    reg_screen = Toplevel()
    reg_screen.configure(bg="#9893cc")
    reg_screen.title("Register")
    reg_screen.geometry("500x500")
    Frame(reg_screen,bg="black",width=500,height=50).place(x=0,y=0)
    Label(reg_screen,text="REGISTER",bg="black",font='Arial',fg="yellow").place(x=230,y=10)
    
    username_label = Label(reg_screen,text="Username",bg="#9893cc",font=('Arial',10)).place(x=100,y=200)
    username_entry = Entry(reg_screen,textvariable=username).place(x=170,y=200) 
    password_label = Label(reg_screen,text="Password",bg="#9893cc",font=('Arial',10)).place(x=100,y=250)
    password_entry = Entry(reg_screen,textvariable=password,show="*").place(x=170,y=250) 
    gender_label = Label(reg_screen,text="Gender",bg="#9893cc",font=('Arial',10)).place(x=100,y=300)
    gender_entry = Entry(reg_screen,textvariable=gender).place(x=170,y=300)
    temp_name = username.get()
    temp_pass = password.get()
    temp_gender = gender.get()
    
    
    
    
    submit = Button(reg_screen,text="Register",command=register_validate).place(x=200,y=350)
    reg_screen.mainloop()

# login screen
def login():
    global log_screen
    log_screen = Toplevel()
    log_screen.configure(bg="#9893cc")
    log_screen.title("LOGIN")
    log_screen.geometry("500x500")
    Frame(log_screen,bg="black",width=500,height=50).place(x=0,y=0)
    Label(log_screen,text="LOGIN",bg="black",font='Arial',fg="yellow").place(x=230,y=10)
    
    username_label = Label(log_screen,text="Username",bg="#9893cc",font=('Arial',10)).place(x=100,y=200)
    username_entry = Entry(log_screen,textvariable=username).place(x=170,y=200) 
    password_label = Label(log_screen,text="Password",bg="#9893cc",font=('Arial',10)).place(x=100,y=250)
    password_entry = Entry(log_screen,textvariable=password,show="*").place(x=170,y=250) 
    submit = Button(log_screen,text="Login",command=login_validate).place(x=200,y=350)

    log_screen.mainloop()



# the main screen

Frame(main_screen,width=500,height=40,bg="#1c1b1a").place(x=0,y=0)
Label(main_screen,text="Main Window",bg="#1c1b1a",fg="Yellow",font='Arial').place(x=240,y=10)

Frame(main_screen,height=300,width=250,bg="#141410").place(x=150,y=100)

log_button = Button(main_screen,text="Login",fg="green",width=20,command=login).place(x=200,y=200)
reg_button = Button(main_screen,text="Register",fg="green",width=20,command=register).place(x=200,y=250)


main_screen.mainloop()
    