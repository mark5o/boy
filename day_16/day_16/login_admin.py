import tkinter  as ttk
from tkinter import font
login_app=ttk.Tk()
login_app.title('Login')
login_app.geometry('600x400')
login_app.grid_columnconfigure(0,weight=1)
font_=font.Font(size=20)
 
uname = ttk.Variable(login_app)
pwd = ttk.Variable(login_app)

ttk.Label(
    login_app,
    text='Enter your Credentials',
    font=font_
).place(100, y=20)
ttk.Label(login_app,text='Username').place(x=100,y=80)
ttk.Entry(login_app,font=font_, textvariable=uname).place(x=250,y=80)

ttk.Label(login_app,text='Password').place(x=100,y=130)
ttk.Entry(login_app,font=font_,show='*',textvariable=pwd).place(x=250,y=130)
 
def submit():   
    op=''
    with open('opr','r') as f:
        op = f.read()
        if len(op) > 0:
            userid: uname.get()
            password: pwd.get()
            p=open('pwd').read()
            if userid == 'admin' and password == p:
                print('Login successful')
            else:
                print('Login Failed')    
        

ttk.Button(
  login_app,text='Submit', font=font_,width=10,height=2,
  command=submit,
).place(x=250,y=220)

def back():
    login_app.destroy()
    with open('opr','w') as f:
        f.write('')
    import app

ttk.Button(login_app,text='< Back',font=font_,height=1,width=6,
           command=back,
           ).place(x=20,y=340)

login_app.mainloop()