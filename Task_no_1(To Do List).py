from tkinter import *
from tkinter import messagebox as msg
def AddTask():
    task = entry.get()
    if task:
        box.insert(END,task)
        entry.delete(0,END)
    else:
        msg.showwarning("Plz Enter the task in the list")

def DeleteTask():
    try:
        deletedata = box.curselection()[0]
        box.delete(deletedata)
    except IndexError:
       msg.showwarning("Plz Select the task from the box")



root = Tk()
root.title("To Do List")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the window's dimensions to the screen's dimensions
root.geometry(f"{screen_width}x{screen_height}")
label = Label(text="TO DO LIST",font="Algerain 26 bold",bg="Blue")
label.grid(row=1,column=1,padx=10,pady=20)


heading = Label(root,text="Enter the task in the list 👇👇",font="Algerain 15")
heading.grid(row=4,column=1)
entry = Entry(root,width=120)
entry.grid(row=5,column=1,padx=50,pady=15)

btn = Button(root,text="Add A Task", font="Algerain 14 ",width=20,height=2,bg='red',command=AddTask)
btn.grid(row=8,column=1,padx=10,pady=15)

box = Listbox(root,height=20,width=100)
box.grid(row=10,column=1)

btnDelete = Button(root,text="Delete A Task", font="Algerain 14 ",width=20,height=2,bg='red',command=DeleteTask)
btnDelete.grid(row=12,column=1,padx=10,pady=15)



root.mainloop()