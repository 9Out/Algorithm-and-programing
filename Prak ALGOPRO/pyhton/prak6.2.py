##Program Akun
##Dibuat oleh As'ad Nirot Ahmadi
import random
a = random.randrange(100,999)
Nama = 'Asad Nirot Ahmadi'
TempatLahir = '25 April 2004'
NamaSingkat = Nama[5:10]
username = Nama[5]+TempatLahir[:2]+TempatLahir[9:13]
password = Nama[:3]+str(a)

print('Nama:',Nama)
print('TempatLahir:',TempatLahir)
print('NamaSingkat:',NamaSingkat)
print('username:',username)
print('password:',password)
