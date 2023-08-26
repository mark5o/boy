import tkinter  as ttk
from tkinter import font
app=ttk.Tk()
app.title('Attendeance System')
app.geometry('600x400')

font_=font.Font(size=20)
ttk.Label(  
    app,
    text='Face Recognition Based Attendance System',
    font=font_
).pack()

def register():
    app.destroy()
    import login_admin
    with('opr','w') as f:
        f.write('register')
        import login_admin
        
def attendance():
    print('Attendance')

def clear_data():
    app.destroy()
    with open('opr','w') as f:
        f.write('clear')
        import login_admin
        
ttk.Button(app, text='Register', command=register, font=font_,
           height=3, width=20,bg='green',
           ).pack(expand=True)
ttk.Button(app, text='Attendance', command=register, font=font_,
           height=3, width=20,bg='blue',
           ).pack(expand=True)
ttk.Button(app, text='Clear Data', command=register, font=font_,
           height=3, width=20,bg='red'
           ).pack(expand=True)



app.mainloop()