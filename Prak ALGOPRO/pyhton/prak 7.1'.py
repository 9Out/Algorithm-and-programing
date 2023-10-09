print('No  | Nama bangun     | Rumus Luas')
print('-'*4+'|'+'-'*17+'|'+'-'*17)

kamus = {
        1:{1: 'Segitiga', 2: 'L = 0.5 * a * t'},
        2:{1: 'Persegi', 2: 'L = s ** 2'},
        3:{1: 'Persegi panjang', 2: 'L = p * l'},
        4:{1: 'Lingkaran', 2: 'L = pi * r ** 2'},
        5:{1: 'Jajaran genjang', 2: 'L = a  * t'}        
        }
for i in range(1, 6):
    a=4-len(str(i))
    b=16-(len(kamus[i][1]))
    print(str(i)+' '*a+'|', kamus[i][1]+' '*b+'|', kamus[i][2])

  
        
