import tkinter as tk

def pt():
    print("nonono")

window=tk.Tk()
window.title('GUI')
#window.mainloop()

label1=tk.Label(window,text='name')
label2=tk.Label(window,text='password')
entry1=tk.Entry()
entry2=tk.Entry()

label1.grid(row=0,sticky='E')
label2.grid(row=1,sticky='E')
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
c=tk.Checkbutton(window,text='keep me logged in')
c.grid(columnspan='2')
bt=tk.Button(window,text='click',command=pt)
bt.grid()

tk.mainloop()

