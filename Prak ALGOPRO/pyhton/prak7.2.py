password = 'nirot'
kesempatan = 1


while kesempatan <= 3 :
    a = input('masukkan password: ')
    if(a != password):
        print("Maaf,anda salah memasukkan password")
        kesempatan += 1
        if(kesempatan > 3):
             print('Anda telah mencoba 3 kali. Akses anda ditolak.')
    else:
        print("Anda berhasil login")
        break
