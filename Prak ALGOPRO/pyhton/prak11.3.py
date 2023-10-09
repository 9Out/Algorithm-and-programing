from tkinter import*

app = Tk()

l = Label(app, text='Data diri',
font=('Arial', 30, 'bold')).grid(row=0, column=0)
la = Label(app, text='bangun yang saya dapat adalah piramid yang merupakan bangun ruang limas segi empat')
la.grid()

l1 = Label(app, text='Sisi alas:')
l1.grid(row=10, column=0)
str1 = StringVar()
e1 = Entry(app, textvariable=str1)
e1.grid(row=10, column=1)

l2 = Label(app, text='Tinggi Segitiga:')
l2.grid(row=15, column=0)
str2 = StringVar()
e2 = Entry(app, textvariable=str2)
e2.grid(row=15, column=1)
c = StringVar()

def hitung(*args):
    a = str1.get()
    b = str2.get()
    luasAlas = int(a) * int(a)
    sisiTegak= int(a) * int(b)/2
    luasPiramid = luasAlas + (4*sisiTegak)
    c.set(luasPiramid)

b1 = Button(app, text='Hitung luas', command = hitung)
b1.grid(row=20, column=0)
b1.grid(padx=25, pady =15)
l3 = Label(app, text='Luas').grid(row=20, column=1)
e3 = Entry(app, textvariable=c)
e3.grid(row=20, column=2)

app, mainloop()
