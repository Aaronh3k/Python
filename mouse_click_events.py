import tkinter as tk  

window=tk.Tk()
def left(event):
    print('this is left')

def right(event):
    print("this is right")

def mid(event):
    print("this is middle")
frame=tk.Frame(window,width=300,height=200)
frame.pack()
frame.bind('<Button-1>',left)
frame.bind('<Button-2>',mid)
frame.bind('<Button-3>',right)
frame.pack()
window.mainloop()
