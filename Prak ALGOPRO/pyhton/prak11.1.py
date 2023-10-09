from tkinter import Tk, Label, Entry, mainloop
from tkinter import LEFT, RIGHT

app = Tk(className = "Aplikasi dengan tabel")

l = Label(app, text='Data diri',
font=('Arial', 30, 'bold')).grid()

l2 = Label(app, text='Nama')
l2.grid(row=1, column=0)
e2 = Entry(app)
e2.grid(row=1, column=1)

l3 = Label(app, text='NIM')
l3.grid(row=2, column=0)
e3 = Entry(app)
e3.grid(row=2, column=1)

l4 = Label(app, text='Buku favorit')
l4.grid(row=3, column=0)
e4 = Entry(app)
e4.grid(row=3, column=1)

l5 = Label(app, text='Idola di kalangan sahabat')
l5.grid(row=4, column=0)
e5 = Entry(app)
e5.grid(row=4, column=1)

l6 = Label(app, text='Motto')
l6.grid(row=5, column=0)
e6 = Entry(app)
e6.grid(row=5, column=1)

app,mainloop()
