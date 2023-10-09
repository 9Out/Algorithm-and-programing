import socket, platform

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50002))
s.listen(5)
data=''
print("Server Program komunikasi tentang server Siap!")

while data.lower() != 'quit':
    komm, addr = s.accept()
    while data.lower() !='quit':
        data = komm.recv(3124).decode('utf-8')
        if data.lower() == 'quit':
            s.close()
            break
        elif data.lower() == 'machine':
            response = platform.machine()
            komm.send(response.encode('utf-8'))
        elif data.lower() == 'release':
            response = platform.release()
            komm.send(response.encode('utf-8'))
        elif data.lower() == 'system':
            response = platform.system()
            komm.send(response.encode('utf-8'))
        elif data.lower() == 'version':
            response = platform.version()
            komm.send(response.encode('utf-8'))
        elif data.lower() == 'node':
            response = platform.node()
            komm.send(response.encode('utf-8'))
        else:
            komm.send("unknown command".encode('utf-8'))
