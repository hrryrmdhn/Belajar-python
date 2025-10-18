import socket

    
def welcome_message():
    desktop = socket.gethostname()
    line = "-" * (len(desktop) + 4)
    print(line)
    print(f"- {desktop} -")
    print(line)
    print("*^____^* : Selamat Datang...\n")
    
def exit_program():
    line = "-" * (len("＞︿＜ : Sampai jumpa lagi") + 3)
    print(line)
    print(f"＞︿＜ : Sampai jumpa lagi")
    print(line)
    exit()
    
if __name__ == "__main__":
    welcome_message()
    exit_program()
    