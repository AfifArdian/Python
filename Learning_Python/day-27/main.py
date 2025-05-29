from tkinter import *

# Tkinter Layout Manager
# pack(), place(x= ?, y= ?), grid(colum= ?, row= ?)


def button_clicked():
    print("I Got Clicked")
    new_text = entry.get()
    label.config(text=new_text)

#Creating a new window and configurations
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#Labels
label = Label(text="I Am a Label")
label.config(text="This is new text")
label.grid(column=0, row=0)

#Buttons
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Buttons 2
new_button = Button(text="Dont Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

#Entries
entry = Entry(width=30)
print(entry.get())
entry.grid(column=3, row=2)



window.mainloop()

