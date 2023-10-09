import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(2)
print("Server penjawab otomatis sudah siap")
data = ''

kamus = {'nama':'Asad nirot ahmadi',
         'NIM' :'L200220155',
         'angkatan':'2022'}

while data.lower() != 'keluar':
    komm,addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1204).decode()
        if data.lower() == 'keluar':
            s.close()
            break
        print('Pertanyaan: ', data.decode())
        if data in kamus:
            print("hasil :",kamus[data])
            komm.send(kamus[data].encode())
        else:
            komm.send('maaf pertanyaan tidak dimengerti'.encode())
