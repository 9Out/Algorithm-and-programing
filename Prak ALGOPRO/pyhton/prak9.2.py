berkas = open("L200220155", "a")
berkas.write("\nSurakarta")
berkas.close()

berkas = open("L200220155", "r")
nim = berkas.readline()
tgl = berkas.readline()
nam = berkas.readline()
kot = berkas.readline()

dd = tgl[:2]
mm = tgl[3:5]
yyyy = tgl[6:]

tgl = mm+"/"+dd+"/"+yyyy

print(nam)
print(kot, tgl)
print(nim)
berkas.close()
