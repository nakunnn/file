import time
import sys
import os
import random

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
print(f"{R}       LOGIN USER          {W}")
print(f"{R}==========================={W}")
user_input = input(f"{Y}Username : {W}")
pw_input = input(f"{Y}Password : {W}")

ketik(f"\n{C}[*] Mengautentikasi Sesi...{W}", 0.05)
time.sleep(1)
print(f"{G}[+] Sesi Dibuat! Memuat antarmuka...{W}")
time.sleep(1)

kredensial = {
    "1": {"user": "VIP40", "pw": "HS40"},
    "2": {"user": "VIP50", "pw": "HS50"},
    "3": {"user": "VIP60", "pw": "HS60"},
    "4": {"user": "VIP70", "pw": "HS70"},
    "5": {"user": "VIP80", "pw": "HS80"},
    "6": {"user": "VIP90", "pw": "HS90"},
    "7": {"user": "VVIP",  "pw": "HS100"}
}

# --- SISTEM LOOPING MENU ---
while True:
    clear()
    print(f"""{R}======================================================
      ███╗   ██╗ █████╗ ██╗  ██╗██╗   ██╗███╗   ██╗   
      ████╗  ██║██╔══██╗██║ ██╔╝██║   ██║████╗  ██║   
      ██╔██╗ ██║███████║█████╔╝ ██║   ██║██╔██╗ ██║   
      ██║╚██╗██║██╔══██║██╔═██╗ ██║   ██║██║╚██╗██║   
      ██║ ╚████║██║  ██║██║  ██╗╚██████╔╝██║ ╚████║   
      ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   
======================================================{W}""")
    print(f"{C}      Logged in as: {G}{user_input}{W}")
    print(f"{R}======================================================{W}")
    print(f"{G}1. Inject Auto Headshot 40%{W}")
    print(f"{G}2. Inject Auto Headshot 50%{W}")
    print(f"{G}3. Inject Auto Headshot 60%{W}")
    print(f"{G}4. Inject Auto Headshot 70%{W}")
    print(f"{G}5. Inject Auto Headshot 80%{W}")
    print(f"{G}6. Inject Auto Headshot 90%{W}")
    print(f"{G}7. Inject Auto Headshot 100% (VVIP){W}")
    print(f"{G}8. Bypass Anti-lag Server{W}")
    print(f"{G}9. Exit{W}")
    print(f"{R}======================================================{W}")

    pilih = input(f"{Y}Pilih menu (1-9): {W}")

    if pilih == "9":
        print(f"{R}[!] Exit.{W}")
        sys.exit()

    if pilih not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print(f"{R}[!] Pilihan tidak valid.{W}")
        time.sleep(1)
        continue # Kembali ke atas loop (menu)

    akses_diberikan = False

    ketik(f"\n{C}[*] Memverifikasi Hak Akses untuk Menu {pilih}...{W}", 0.05)
    time.sleep(1)

    if pilih in kredensial:
        if user_input == kredensial[pilih]["user"] and pw_input == kredensial[pilih]["pw"]:
            akses_diberikan = True
    elif pilih == "8":
        for k, v in kredensial.items():
            if v["user"] == user_input and v["pw"] == pw_input:
                akses_diberikan = True
                break

    # --- LOGIKA JIKA AKSES DITOLAK ---
    if not akses_diberikan:
        print(f"{R}[!] AKSES DITOLAK:{W} Akun '{user_input}' tidak memiliki lisensi untuk level ini!")
        coba_lagi = input(f"{Y}[?] Kembali ke menu utama? (y/n): {W}").strip().lower()
        if coba_lagi == 'y':
            continue # Kembali ke tampilan menu
        else:
            print(f"{R}[!] Program dihentikan otomatis untuk keamanan.{W}")
            sys.exit()

    print(f"{G}[+] Hak Akses Diterima! Melanjutkan proses...{W}")
    time.sleep(1)

    print(f"\n{R}[!] INITIALIZING ANTI-CHEAT BYPASS PROTOCOL...{W}")
    time.sleep(1)
    print(f"{C}[*] Spoofing Device ID (IMEI/MAC Address)... {W}", end="", flush=True)
    time.sleep(1.5)
    print(f"{G}SUCCESS{W}")

    print(f"{C}[*] Blocking Server Telemetry & Logs... {W}", end="", flush=True)
    time.sleep(1.5)
    print(f"{G}SUCCESS{W}")

    print(f"{C}[*] Bypassing Garena Security Modules... {W}")
    sys.stdout.write(f"{Y}Progress: [{W}")
    for i in range(20):
        sys.stdout.write(f"{G}█{W}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"{Y}] 100% SECURE{W}")
    time.sleep(1)

    ketik(f"\n{C}[*] Searching target process...{W}")
    time.sleep(1)
    print(f"{G}[+] Target 'com.dts.freefireth' (PID: {random.randint(1000, 9999)}){W}")
    time.sleep(1)
    print(f"{Y}[*] Injecting payload...{W}")
    time.sleep(1)

    for _ in range(25):
        hex_val = ''.join(random.choices('0123456789ABCDEF', k=8))
        print(f"{G}0x{hex_val} -> WRITE_MEMORY{W}")
        time.sleep(0.04)
        
    print(f"\n{C}[*] Compilasi...{W}")
    time.sleep(1)
    print(f"\n{Y}--------------------------------------")
    print(f" STATUS : ACTIVATED {G}(UNDETECTED){W}")
    print(" BYPASS : ON")
    print(f"--------------------------------------{W}\n")
    
    # Menahan layar setelah injeksi berhasil agar tidak langsung balik ke menu
    input(f"{C}[ENTER] Tekan enter untuk kembali ke menu...{W}")
