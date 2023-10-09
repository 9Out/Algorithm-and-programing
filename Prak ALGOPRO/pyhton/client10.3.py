import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = 'localhost'
s.connect((hostname, 50003))
print('Menghitung luas piramid')

pesan = ''
sisiAlas = ''
tinggi = ''

while pesan != 'hitung':
    if sisiAlas == '':
        sisiAlas = input('Masukkan sisi alas: ')
        s.send(sisiAlas.encode())
        response = s.recv(1234).decode()
        print('Respon:',response)
    elif tinggi == '':
        tinggi = input('Masukkan tinggi segitiga: ')
        s.send(tinggi.encode())
        response = s.recv(1234).decode()
        print('Respon:',response)
    else:
        pesan = input('Pesan: ')
        s.send(pesan.encode())    

hasil = s.recv(1234).decode()
print('Respons: ', hasil)
s.close()
