data = {
    'a' : 'Nirot','N' : 'L200220155', 'A' : 'Perumahan griya teratai permai',
    'P' : '12345', 't' : 'solo', 'G' : 'pria', 'm' : 'Mahasiswa' 
    }
dataBantuan = [
    "pilihan yang tersedia:",
    'a menampilkan Nama',
    'N menampilkan NIM',
    'A menampilkan Alamat',
    'P menampilkan kode pos',
    't menmpilkan asal',
    'G menampilkan gender',
    'm menampilkan status',
    'K untuk keluar'
    ]

def cari (use):
    if (use) in (data):
        return (data[use])
    else:
        return('perintah tidak dikenal')
def bantuan():
    for x in dataBantuan:
        print(x)

bantuan()
use = input("Pilihan saudara: ")
while use != 'K':
    if use == 'b':
        bantuan()
        use = input("Pilihan saudara: ")
    else:
        q = cari(use)
        print(q)
        use = input("Pilihan saudara: ")
print("terima kasih.")
