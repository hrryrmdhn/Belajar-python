import random

print("Peraturan:\n~ Dalam game ini pemain bertugas untuk menebak angka misteri\n~ Pemain diberi kesempatan untuk menebak sebanyak 9 kali\n~ Rentang angka yang harus ditebak ditentukan berdasarkan tingkat kesulitan\n~ Terdapat 4 tingkat kesulitan diantaranya:\n Mudah: 1-200\n Normal: 1-500\n Sulit: 1-1000\n Extreme: 1-1500\n")

while True:
    difficult = input("\nSilahkan pilih tingkat kesulitan [Mudah/Normal/Sulit/Extreme] ").capitalize()
    while difficult != "Mudah" and difficult != "Normal" and difficult != "Sulit" and difficult != "Extreme":
        difficult = input("Hanya tersedia 4 tingkat kesulitan [Mudah/Normal/Sulit/Extreme] ").capitalize()

        if difficult == "Mudah":
            mysterious_number = random.randint(1, 200)
        elif difficult == "Normal":
            mysterious_number = random.randint(1, 500)
        elif difficult == "Sulit":
            mysterious_number = random.randint(1,1000)
        else:
            mysterious_number = random.randint(1, 1500)
        
    print(f"Tingkat kesulitan yang kamu pilih adalah: {difficult}\n")

    max_try = 9
    try_value = 0
    history_number = []

    while try_value != max_try:
        answer = int(input("Coba tebak angka misterinya: "))
        try_value += 1
        chance = max_try - try_value
        history_number.append(answer)
        
        if answer == mysterious_number :
            print("----------------------------------------------------------------------------------------------")
            print(f"Hebat!! \n~ Kamu berhasil menebak angka misterinya yaitu {mysterious_number} dengan percobaan sebanyak: {len(history_number)} kali\n~ Riwayat tebakan: {history_number}\n")
            break
        elif answer < mysterious_number:
            print("Tebakanmu masih terlalu kecil")
            print(f"Sisa kesempatan mu: {chance}\n")
        elif answer > mysterious_number:
            print("Angkanya terlalu besarrr")
            print(f"Sisa kesempatan mu: {chance}\n")
        
    else:
        print(f"Kamu kalah!! Kesempatanmu sudah habis. Angka misterinya adalah: {mysterious_number}\nRiwayat tebakan: {history_number}")
        
    again = input("Ingin bermain lagi? [y/n] ").lower()
    if again == "n":
        break