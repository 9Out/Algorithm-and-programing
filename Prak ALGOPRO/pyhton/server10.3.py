import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 50003))
s.listen(4)
print("Server ON")

save = "Data tersimpan"
sisiAlas = ''
tinggi = ''
pesan = ''

while pesan.lower() != 'hitung':
    komm, addr = s.accept()
    while pesan.lower() != 'hitung':
        pesan = komm.recv(1234).decode()
        if pesan.lower() == 'hitung':
            luasAlas = sisiAlas*sisiAlas
            sisiTegak = sisiAlas*tinggi/2
            luasPiramid = luasAlas+(4*sisiTegak)
            print("Luas Piramid: ", luasPiramid)
            hasil = str(luasPiramid)
            komm.send(hasil.encode())
            s.close()
            break
        elif sisiAlas == '':
            sisiAlas = int(pesan)
            print('sisi alas = ',sisiAlas)
            komm.send(save.encode())
        elif tinggi == '':
            tinggi = int(pesan)
            print('tinggi segitiga piramid = ', tinggi)
            komm.send(save.encode())

