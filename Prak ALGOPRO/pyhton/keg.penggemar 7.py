import datetime
from time import sleep

waktu = datetime.datetime.now()
detik = waktu.second

while detik != 0:
    waktu = datetime.datetime.now()
    detik = waktu.second

    NowHour = str(waktu.hour)
    NowMinute = str(waktu.minute)
    NowSecond = str(waktu.second)

    print(NowHour+':'+NowMinute+':'+NowSecond)

    sleep(1)

print("jam praktikum sudah habis, Silahkan pulang")
