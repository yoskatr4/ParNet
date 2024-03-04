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
    saat = input("Alarmı ne zaman kurmak istersiniz? (SS:DD): ")
    while True:
        su_an = datetime.datetime.now()
        su_an_saati = su_an.strftime("%H:%M")
        if su_an_saati == saat:
            print("Alarm Çalıyor!")
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
    print("CPU Kullanımı:", psutil.cpu_percent(interval=1), "%")
    print("CPU Frekansı:", psutil.cpu_freq().current, "MHz")

def bellek_durumu():
    bellek = psutil.virtual_memory()
    print("Toplam Bellek:", bellek.total // (1024 ** 3), "GB")
    print("Kullanılan Bellek:", bellek.used // (1024 ** 3), "GB")
    print("Boşta:", bellek.available // (1024 ** 3), "GB")

def bilgisayar_calisma_suresi():
    sure = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    print("\n---- Bilgisayar Çalışma Süresi ----")
    print("Bilgisayar Çalışma Süresi:", sure)
def gpu_durumu():
    try:
        output = subprocess.check_output(["nvidia-smi", "--query-gpu=utilization.gpu,memory.total,memory.used",
                                          "--format=csv,noheader,nounits"])
        gpu_utilizasyonu, bellek_toplam, bellek_kullanilan = output.decode().strip().split(',')
        print("GPU Kullanımı:", gpu_utilizasyonu.strip(), "%")
        print("Toplam Bellek:", round(int(bellek_toplam.strip()) / 1024, 2), "GB")
        print("Kullanılan Bellek:", round(int(bellek_kullanilan.strip()) / 1024, 2), "GB")
    except Exception as e:
        print("Nvidia GPU bulunamadı veya erişilemedi.")
while True:
    print("\nNe yapmak istersiniz?")
    print("1. Saati Göster")
    print("2. Tarihi Göster")
    print("3. Alarm Kur")
    print("4. Google'da Ara")
    print("5. YouTube'da Ara")
    print("6. Sistem Durumu")
    print("7. Kaç Saat Boyunca Çalıştın")
    print("8. E-posta Gönderme")
    print("9. Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        saat_goster()
    elif secim == "2":
        tarih_goster()
    elif secim == "3":
        alarm_kur()
    elif secim == "4":
        arama = input("Google'da ne aramak istersiniz? (Çıkmak için 'q' ya basın): ")
        if arama.lower() == 'q':
            print("Programdan çıkılıyor...")
            break
        kelime_ara_google(arama)
    elif secim == "5":
        arama = input("YouTube'da ne aramak istersiniz? (Çıkmak için 'q' ya basın): ")
        if arama.lower() == 'q':
            print("Programdan çıkılıyor...")
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
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
