waktu = ('pagi', 'siang', 'sore', 'petang', 'malam')
nama = input("Masukkan nama saudara: ")
jam = float(input("Pukul berapa sekarang? "))

if(jam >= 5 and jam <10):
    print('selamat',waktu[0], nama)
elif(jam >= 10 and jam < 15):
    print('selamat',waktu[1], nama)
elif(jam >= 15 and jam < 17):
    print('selamat',waktu[2], nama)
elif(jam >= 17 and jam < 20):
    print('selamat',waktu[3], nama)
else:
    print('selamat',waktu[4], nama)
