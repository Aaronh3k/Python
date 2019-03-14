import tkinter as tk 

window=tk.Tk()
window.title('GUI')
def usn():
    print('4NM15EC002')

def dob():
    print('05/12/1997')

def dept():
    print('E&C')

def sec():
    print('A')

menu=tk.Menu(window)

submenu=tk.Menu(menu)
menu.add_cascade(label='File',menu=submenu)
submenu.add_command(label='New File')
submenu.add_command(label='New Window')
submenu.add_command(label='Open')
submenu.add_command(label='Save')
submenu.add_separator()
submenu.add_command(label='Exit',command=window.quit)

submenu1=tk.Menu(menu)
menu.add_cascade(label='Edit',menu=submenu1)
submenu1.add_command(label='Undo')
submenu1.add_command(label='Redo')
submenu1.add_command(label='Cut')
submenu1.add_command(label='Copy')

submenu2=tk.Menu(menu)
menu.add_cascade(label='View',menu=submenu2)
submenu2.add_command(label='Debug')
submenu2.add_command(label='Search')

submenu3=tk.Menu(menu)
menu.add_cascade(label='Info',menu=submenu3)
sub=tk.Menu(submenu3)
submenu3.add_cascade(label='User',menu=sub)
sub1=tk.Menu(sub)
sub.add_cascade(label='Aaron',menu=sub1)
sub1.add_command(label='USN',command=usn)
sub1.add_command(label='DOB',command=dob)
sub1.add_command(label='DEPT',command=dept)
sub1.add_command(label='SEC',command=sec)


window.config(menu=menu)
window.mainloop()
