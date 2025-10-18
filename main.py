from libs import welcome_message, exit_program
from games import tebak_angka

def menu():
    while True:
        print("Program tersedia saat ini: \n1.Game Tebak Angka \n2.Keluar Program \n\n")
        choose = int(input("Pilih program yang akan kamu jalankan: "))

        if choose == 1:
            tebak_angka.start()
        else:
            exit_program()
        
def main():
    welcome_message()
    menu()
    
if __name__ == "__main__":
    main()