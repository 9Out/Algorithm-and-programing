import socket

hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50001))
print("Program komunikasi tentang diri")

pesan = ''

while pesan.lower() != 'keluar':
    pesan = input('Perintah: ')
    s.send(pesan.encode('utf-8'))
    if pesan.lower() != 'keluar':
        response = s.recv(1204).decode('utf-8')
        print('jawab: ', response)
print("jawab: Siap!!")
s.close()
