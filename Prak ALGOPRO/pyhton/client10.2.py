import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = 'localhost'
s.connect((hostname,50002))
print("Program komunikasi tentang server")

pesan = ''

while pesan.lower() != 'quit':
    pesan = input('Command: ')
    s.send(pesan.encode('utf-8'))
    if pesan.lower() != 'quit':
        respon = s.recv(3124).decode('utf-8')
        print('Response: ', respon)
print("Response: Thank you")
s.close()
        
    
