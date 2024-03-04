import datetime
import time
import winsound
import webbrowser
import psutil
import subprocess

baslangic_zamani = datetime.datetime.now()

def saat_goster():
    su_an = datetime.datetime.now()
    saat = su_an.strftime("%H:%M:%S")
    print("Saat:", saat)

def tarih_goster():
    su_an = datetime.datetime.now()
    tarih = su_an.strftime("%d-%m-%Y")
    print("Tarih:", tarih)

def alarm_kur():
    saat = input("When would you like to set the alarm (SS:DD): ")
    while True:
        su_an = datetime.datetime.now()
        su_an_saati = su_an.strftime("%H:%M")
        if su_an_saati == saat:
            print("The alarm is sounding!")
            winsound.Beep(1000, 1000)  # Alarm çalındığında bip sesi çal
            break
        time.sleep(10)  # 10 saniye bekleyerek sürekli kontrol et

def kelime_ara_google(kelime):
    url = "https://www.google.com/search?q=" + kelime
    webbrowser.open_new_tab(url)

def kelime_ara_youtube(kelime):
    url = "https://www.youtube.com/results?search_query=" + kelime
    webbrowser.open_new_tab(url)
def cpu_durumu():
    print("CPU Utilization:", psutil.cpu_percent(interval=1), "%")
    print("CPU Frequency:", psutil.cpu_freq().current, "MHz")

def bellek_durumu():
    bellek = psutil.virtual_memory()
    print("Total Memory:", bellek.total // (1024 ** 3), "GB")
    print("Memory Used:", bellek.used // (1024 ** 3), "GB")
    print("Idle:", bellek.available // (1024 ** 3), "GB")

def bilgisayar_calisma_suresi():
    sure = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    print("\n---- Computer Working Time ----")
    print("Computer Working Time:", sure)
def gpu_durumu():
    try:
        output = subprocess.check_output(["nvidia-smi", "--query-gpu=utilization.gpu,memory.total,memory.used",
                                          "--format=csv,noheader,nounits"])
        gpu_utilizasyonu, bellek_toplam, bellek_kullanilan = output.decode().strip().split(',')
        print("GPU Utilization:", gpu_utilizasyonu.strip(), "%")
        print("Total Memory:", round(int(bellek_toplam.strip()) / 1024, 2), "GB")
        print("Memory Used:", round(int(bellek_kullanilan.strip()) / 1024, 2), "GB")
    except Exception as e:
        print("Nvidia GPU could not be found or accessed.")
while True:
    print("\nNe yapmak istersiniz?")
    print("1. Show Time")
    print("2. Show Date")
    print("3. Set Alarm ")
    print("4. Google it")
    print("5. Search YouTube")
    print("6. System Status")
    print("7. How Many Hours Did You Work")
    print("8. Send Email")
    print("9. Exit")

    secim = input("Make your choice: ")

    if secim == "1":
        saat_goster()
    elif secim == "2":
        tarih_goster()
    elif secim == "3":
        alarm_kur()
    elif secim == "4":
        arama = input("What would you like to search for on Google? (Press 'q' to exit): ")
        if arama.lower() == 'q':
            print("Exiting the program...")
            break
        kelime_ara_google(arama)
    elif secim == "5":
        arama = input("What would you like to search for on YouTube? (Press 'q' to exit): ")
        if arama.lower() == 'q':
            print("Exiting the program...")
            break
        kelime_ara_youtube(arama)
    
    elif secim == "6":
        print("\n")
        cpu_durumu()
        print("\n")
        bellek_durumu()
        print("\n")
        gpu_durumu()
    
    elif secim == "7":
        bilgisayar_calisma_suresi()

    elif secim == "8":
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")

    elif secim == "9":
        print("Exiting the program...")
        break
    else:
        print("Invalid selection. Please try again.")
