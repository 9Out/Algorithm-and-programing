import shelve
berkas = shelve.open("nn")
print("NIM            : "+berkas["biodata"][0])
print("Tanngal Lahir  : "+berkas["biodata"][1])
print("Nama           : "+berkas["biodata"][2])
print("Kota Asal      : "+berkas["biodata"][3])
berkas.close()
