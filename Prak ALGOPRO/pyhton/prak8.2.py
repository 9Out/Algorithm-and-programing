
indeks = {
    "Celcius    ":  "c",
    "Fahrenheit ":  "f",
    "selesai    ": "s"
    }
print("~Indeks Satuan suhu~")

def konversiCelsius(suhu):
    if(satuanSuhu == "c"): 
        farenheit = (9 / 5) * suhu + 32
        print('suhu', suhu, 'Celcius setara dengan', farenheit, 'Fahrenheit')
        return farenheit
def konversiFarenheit(suhu):
     if(satuanSuhu == "f"):
        celsius = (suhu - 32)* 5/9
        print('suhu', suhu, 'Fahrenheit setara dengan', celsius, 'Celsius')
        return celsius
    
for i in indeks:
    print("Satuan suhu:",i,"\t Indeks:", indeks[i])
    
suhu = float(input("Masukkan suhu: "))
satuanSuhu = input("Masukkan indeks suhu: ")

while satuanSuhu != "s" :
    if(satuanSuhu == "c"):
        konversiCelsius(suhu)
        suhu = float(input("Masukkan suhu: "))
        satuanSuhu = input("Masukkan indeks suhu: ")
    if(satuanSuhu == "f"):
        konversiFarenheit(suhu)
        suhu = float(input("Masukkan suhu: "))
        satuanSuhu = input("Masukkan indeks suhu: ")
print("terima kasih")
