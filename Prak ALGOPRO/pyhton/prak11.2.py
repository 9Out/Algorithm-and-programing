from tkinter import*

app = Tk()

l1 = Label(app, text='Angka 1')
l1.grid(row=0, column=0)
str1 = StringVar()
e1 = Entry(app, textvariable=str1)
e1.grid(row=0, column=1)

l2 = Label(app, text='Angka 2')
l2.grid(row=1, column=0)
str2 = StringVar()
e2 = Entry(app, textvariable=str2)
e2.grid(row=1, column=1)
c = StringVar()

def plus(*args):
    a = str1.get()
    b = str2.get()
    tambah = int(a) + int(b)
    c.set(tambah)
def min(*args):
    a = str1.get()
    b = str2.get()
    kurang = int(a) - int(b)
    c.set(kurang)
def kali(*args):
    a = str1.get()
    b = str2.get()
    kali = int(a) * int(b)
    c.set(kali)
def bagi(*args):
    a = str1.get()
    b = str2.get()
    bagi = int(a) / int(b)
    c.set(bagi)
def hapus():
    str1.set(0)
    str2.set(0)
    c.set(0)

b1 = Button(app, text='+', command=plus)
b1.grid(row=2, column=0)
b1.grid(padx=25, pady =10)
b2 = Button(app, text='-', command=min)
b2.grid(row=2, column=1)
b2.grid(padx=25, pady =10)
b3 = Button(app, text='x', command=kali)
b3.grid(row=2, column=2)
b3.grid(padx=25, pady =10)
b4 = Button(app, text=':', command=bagi)
b4.grid(row=2, column=3)
b4.grid(padx=25, pady =10)
b5 = Button(app, text='Hapus', command=hapus)
b5.grid(row=4, columnspan=3)
b5.grid(padx=25, pady =10)

l3 = Label(app, text='Hasil').grid(row=3, column=0)
e3 = Entry(app, textvariable=c)
e3.grid(row=3, column=1)
e3.grid(padx=15, pady=10)

app, mainloop()

    
