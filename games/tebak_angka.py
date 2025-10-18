import random

def start():
    print("\nDalam game ini terdapat 3 tingkat kesulitan diantaranya:\nMudah = 1-200 \nNormal = 1-500 \nSulit = 1-1000 \nExtreme = 1-1500")

    while True:
        difficult = input("Silahkan pilih tingkat kesulitan yang kamu mau [Mudah/Normal/Sulit/Extreme] ").capitalize()
        while difficult != "Mudah" and difficult != "Normal" and difficult != "Sulit" and difficult != "Extreme":
            difficult = input("Pilihannya cuma 3 itu ajaa [Mudah/Normal/Sulit/Extreme] ").capitalize()

        if difficult == "Mudah":
            mysterious_number = random.randint(1, 200)
        elif difficult == "Normal":
            mysterious_number = random.randint(1, 500)
        elif difficult == "Extreme":
            mysterious_number = random.randint(1, 1500)
        else:
            mysterious_number = random.randint(1, 1000)
            
            
        print(f"Tingkat kesulitan yang kamu pilih adalah: {difficult} \n")


        max_try = 8
        try_do = 0
        answer = 0
        try_lots = []

        while try_do < max_try:
            answer = int(input("Tebak angka misterinya: "))
            try_do += 1
            remainder_chance = max_try - try_do
            try_lots.append(answer)
            
            if answer == mysterious_number:
                print("-------------------------------------------------------------------------")
                print(f"CONGRATULATIONS 🏆\n~ kamu berhasil menebak angka misteri yaitu {mysterious_number} dalam {len(try_lots)} kali percobaan\n~ Riwayat tebakanmu: {try_lots}\n")
                break
                
            elif abs(answer - mysterious_number) <= 1 and answer != mysterious_number:
                print("<= Udah deket, dikit lagi! =>")
                print(f"Sisa kesempatan menebak: {remainder_chance}\n")
            elif answer > mysterious_number:
                print("<= Wah masih terlalu besar =>")
                print(f"Sisa kesempatan menebak: {remainder_chance}\n")
            elif answer < mysterious_number:
                print("<= Angka nya masih terlalu kecil =>")
                print(f"Sisa kesempatan menebak: {remainder_chance}\n")
                
        else:
            print("---------------------------------------------------------------------")
            print(f"KAMU KALAH 🤪\n~ Batas kesempatan menebakmu sudah habis, angka misterinya adalah :{mysterious_number}\n~ Riwayat tebakanmu: {try_lots}\n")
        
        main_lagi = input("Ingin main lagi? [y/n] ").lower()
        if main_lagi == "n":
            return True
            
if __name__ == "__main__":
    start()