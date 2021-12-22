"""
Program python sederhana - Gunting batu kertas
"""
from random import randint
saya = ["Batu", "Kertas", "Gunting"]
computer = saya[randint(0,2)]
player = False

while player == False:
    player = input("\n","Batu, Gunting, Kertas? ")
    pemain = player.capitalize()
    if pemain == computer:
        print("boot memilih ",computer)
        print("Seri!")
    elif pemain == "Batu":
        if computer == "Kertas":
            print("boot memilih ",computer)
            print("Anda Kalah!", computer, "menutup", pemain)
        else:
            print("boot memilih ",computer)
            print("Anda Menang!", pemain, "memukul", computer)
    elif pemain == "Kertas":
        if computer == "Gunting":
            print("boot memilih ",computer)
            print("Anda Kalah!", computer, "memotong", pemain)
        else:
            print("boot memilih ",computer)
            print("Anda Menang!", pemain, "menutup", computer)
    elif pemain == "Gunting":
        if computer == "Batu":
            print("boot memilih ",computer)
            print("Anda Kalah...", computer, "memukul", pemain)
        else:
            print("boot memilih ",computer)
            print("Anda Menang!", pemain, "memotong", computer)
    else:
        print("Input tidak valid. Perhatikan penulisan Anda!")
    
    player = False
    computer = saya[randint(0,2)]
