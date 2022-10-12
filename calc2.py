from tkinter import *

root=Tk()
root.title('Smart Calculator')
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')

logoImage=PhotoImage(file='logo.png')
logoLabel=Label(root, image=logoImage, bg='dodgerblue3')
logoLabel.grid(row=0, column=0)


entryField=Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

micImage=PhotoImage(file='microphone.png')
micButton=Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='dodgerblue3')
micButton.grid(row=0, column=7)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]

rowValue=1
columnValue=0
for i in button_text_list:
    button=Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white', font=('arial', 15, 'bold'), activebackground='dodgerblue3')
    button.grid(row=rowValue,column=columnValue, pady=1)
    columnValue+=1
    if columnValue>7:
        rowValue+=1
        columnValue=0

root.mainloop()