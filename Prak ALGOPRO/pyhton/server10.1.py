import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50001))
s.listen(5)
data = ''

print("Server penjawab otomatis sudah siap")

kamus = {'nama':'Asad nirot ahmadi',
         'NIM' :'L200220155',
         'angkatan':'2022'}

while (data.lower() != 'keluar'):
    komm,addr = s.accept()
    while (data.lower() != 'keluar'):
        data = komm.recv(1204).decode('utf-8')
        if (data.lower() == 'keluar'):
            s.close()
            break
        if data in kamus:
            print('hasil: ', kamus[data])
            komm.send(kamus[data].encode('utf-8'))
        else:
            komm.send('maaf perintah tidak dimengerti'.encode('utf-8'))
