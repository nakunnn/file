import time
import sys
import os
import random
from getpass import getpass

G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
def ketik(teks, delay=0.03):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay)
    print()
clear()
ketik(f"{C}[*] Loading...{W}")
time.sleep(0.5)
ketik(f"{C}[*] Server Status... {G}HALF ONLINE{W}")
time.sleep(1)
clear()
print(f"{R}==========================={W}")
print(f"{R}       LOGIN VIP           {W}")
print(f"{R}==========================={W}")
user = input(f"{Y}Username : {W}")
pw = input(f"{Y}Password : {W}") 
ketik(f"\n{C}[*] Verifikasi Username...{W}", 0.05)
time.sleep(1.5)
ketik(f"\n{C}[*] Verifikasi password...{W}", 0.05)
time.sleep(1.5)
if pw != "VIP-092841":
    print(f"{R}[!] AKSES DITOLAK: Bukan member vip!.{W}")
    sys.exit()
print(f"{G}[+] Selamat datang, {user}!{W}")
time.sleep(1.5)
clear()
print(f"{R}======================================{W}")
print(f"{R}      [ MASUKKAN ASCII ART DI SINI ]  {W}")
print(f"{R}======================================{W}")
print(f"{G}1. Inject Auto Headshot 40%{W}")
print(f"{G}2. Bypass Anti-lag Server{W}")
print(f"{G}3. Exit{W}")
print(f"{R}======================================{W}")
pilih = input(f"{Y}Pilih menu (1/2/3): {W}")
if pilih == "1" or pilih == "2":
    ketik(f"\n{C}[*] Searching...{W}")
    time.sleep(1)
    print(f"{G}[+] Target 'com.dts.freefireth' (PID: {random.randint(1000, 9999)}){W}")
    time.sleep(1)
    print(f"{Y}[*] Injecting...{W}")
    time.sleep(1)
    for _ in range(25):
        hex_val = ''.join(random.choices('0123456789ABCDEF', k=8))
        print(f"{G}0x{hex_val} -> WRITE_MEMORY{W}")
        time.sleep(0.04)
    print(f"\n{C}[*] Compilasi...{W}")
    time.sleep(1)
    print(f"\n{Y}--------------------------------------")
    print(" STATUS: ACTIVATEDY")
    print(f"--------------------------------------{W}\n")
else:
    print(f"{R}[!] Exit.{W}")
    sys.exit()
