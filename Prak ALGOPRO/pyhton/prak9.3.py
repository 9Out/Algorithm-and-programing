import shelve
berkas = open("L200220155", "r")

nim = berkas.readline()
tgl = berkas.readline()
nam = berkas.readline()
kot = berkas.readline()

berkas = shelve.open("nn")
berkas["biodata"] = [nim,tgl,nam,kot]
berkas.close()
