
kamus = {'Segitiga       ': 'L = 0.5 * a * t',
         'Persegi        ': 'L = s ** 2',
         'Persegi panjang': 'L = p * l',
         'Lingkaran      ': 'L = phi * r ** 2',
         'Jajaran genjang': 'L = a  * t'}        
keys = list (kamus.keys())
values = list (kamus.values())
no = 0
print('No  | Nama bangun     | Rumus Luas')
print('-'*4+'|'+'-'*17+'|'+'-'*17)

for math in kamus:
    no += 1
    print(f"{no}   | {math} | {kamus[math]}")



