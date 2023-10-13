from tkinter import *
from tkinter import messagebox as msg
import random
import string

def GneratesPasword():
   
    length = entry.get()
    entry.delete(0,END)
    if length:
        s1 =string.ascii_lowercase
        s2 =string.ascii_uppercase
        s3 =string.digits
        s4 =string.punctuation
        save = []
        save.extend(list(s1))
        save.extend(list(s2))
        save.extend(list(s3))
        save.extend(list(s4))
        password = "".join(random.sample(save,int(length)))
        box.insert(END,password)
    else:
        msg.showerror("Error", "Enter the length of the password")


# Main Part 
root = Tk()
root.title("Password Generators")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the window's dimensions to the screen's dimensions
root.geometry(f"{screen_width}x{screen_height}")
label = Label(text="Password Generators",font="Algerain 26 bold",bg="Blue")
label.grid(row=1,column=1,padx=10,pady=20)


heading = Label(root,text="Enter the length of password 👇👇",font="Algerain 15")
heading.grid(row=4,column=1)
entry = Entry(root,width=120)
entry.grid(row=5,column=1,padx=50,pady=15)

box = Listbox(root,height=10,width=30)
box.grid(row=10,column=1)

btnDelete = Button(root,text="Generates a Password", font="Algerain 14 ",width=20,height=2,bg='red',command= GneratesPasword)
btnDelete.grid(row=12,column=1,padx=10,pady=15)



root.mainloop()