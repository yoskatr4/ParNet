import datetime
import time
import winsound
import webbrowser
import psutil
import subprocess
import speech_recognition as sr

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

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Komut bekleniyor...")
        audio = recognizer.listen(source)

    try:
        spoken_text = recognizer.recognize_google(audio, language='tr-TR')
        print("Anlaşılan Komut:", spoken_text)
        if "saat" in spoken_text:
            saat_goster()
        elif "tarih" in spoken_text:
            tarih_goster()
        elif "alarm" in spoken_text:
            alarm_kur()
        elif "Google" in spoken_text:
            kelime = spoken_text.split("Google'da ")[1]
            kelime_ara_google(kelime)
        elif "YouTube" in spoken_text:
            kelime = spoken_text.split("YouTube'da ")[1]
            kelime_ara_youtube(kelime)
        elif "sistem" in spoken_text:
            cpu_durumu()
            bellek_durumu()
            gpu_durumu()
        elif "çalışma süresi" in spoken_text:
            bilgisayar_calisma_suresi()
        elif "mail" in spoken_text:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
        elif "çıkış" in spoken_text:
            print("Programdan çıkılıyor...")
            return False
    except sr.UnknownValueError:
        print("Ses anlaşılamadı.")
    except sr.RequestError as e:
        print("Google Speech Recognition servisi çalışmıyor; {0}".format(e))

if __name__ == "__main__":
    while True:
        print('''
Saati Göster             [saat]
Tarihi Göster            [tarih]     
Alarm Kur                [alarm]
Google'da Ara            [Google'da <kelime>]    
YouTube'da Ara           [YouTube'da <kelime>]
Sistem Durumu            [sistem]
E-posta Gönderme         [mail]
Çıkış                    [çıkış]
''')
        while True:
            if not recognize_speech():
                break
