import datetime
import time
import winsound
import webbrowser
import psutil
import subprocess
import speech_recognition as sr

def show_time():
    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%H:%M:%S")
    print("Time:", time_str)

def show_date():
    current_time = datetime.datetime.now()
    date_str = current_time.strftime("%d-%m-%Y")
    print("Date:", date_str)

def set_alarm():
    alarm_time = input("When do you want to set the alarm? (HH:MM): ")
    while True:
        current_time = datetime.datetime.now()
        current_hour_minute = current_time.strftime("%H:%M")
        if current_hour_minute == alarm_time:
            print("Alarm is ringing!")
            winsound.Beep(1000, 1000)  # Beep when the alarm rings
            break
        time.sleep(10)  # Check continuously after every 10 seconds

def search_word_google(word):
    url = "https://www.google.com/search?q=" + word
    webbrowser.open_new_tab(url)

def search_word_youtube(word):
    url = "https://www.youtube.com/results?search_query=" + word
    webbrowser.open_new_tab(url)

def cpu_status():
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
    print("CPU Frequency:", psutil.cpu_freq().current, "MHz")

def memory_status():
    memory = psutil.virtual_memory()
    print("Total Memory:", memory.total // (1024 ** 3), "GB")
    print("Used Memory:", memory.used // (1024 ** 3), "GB")
    print("Available Memory:", memory.available // (1024 ** 3), "GB")

def uptime():
    uptime_duration = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    print("\n---- System Uptime ----")
    print("System Uptime:", uptime_duration)

def gpu_status():
    try:
        output = subprocess.check_output(["nvidia-smi", "--query-gpu=utilization.gpu,memory.total,memory.used",
                                          "--format=csv,noheader,nounits"])
        gpu_utilization, total_memory, used_memory = output.decode().strip().split(',')
        print("GPU Usage:", gpu_utilization.strip(), "%")
        print("Total Memory:", round(int(total_memory.strip()) / 1024, 2), "GB")
        print("Used Memory:", round(int(used_memory.strip()) / 1024, 2), "GB")
    except Exception as e:
        print("Nvidia GPU not found or accessible.")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for command...")
        audio = recognizer.listen(source)

    try:
        spoken_text = recognizer.recognize_google(audio)
        print("Spoken Command:", spoken_text)
        if "time" in spoken_text:
            show_time()
        elif "date" in spoken_text:
            show_date()
        elif "alarm" in spoken_text:
            set_alarm()
        elif "Google" in spoken_text:
            word = spoken_text.split("Google for ")[1]
            search_word_google(word)
        elif "YouTube" in spoken_text:
            word = spoken_text.split("Search YouTube for ")[1]
            search_word_youtube(word)
        elif "system" in spoken_text:
            cpu_status()
            memory_status()
            gpu_status()
        elif "uptime" in spoken_text:
            uptime()
        elif "email" in spoken_text:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
        elif "exit" in spoken_text:
            print("Exiting the program...")
            return False
    except sr.UnknownValueError:
        print("Speech could not be understood.")
    except sr.RequestError as e:
        print("Google Speech Recognition service is not working; {0}".format(e))

if __name__ == "__main__":
    while True:
        print('''
Show Time                [time]
Show Date                [date]     
Set Alarm                [alarm]
Search Google            [Google for <word>]    
Search YouTube           [Search YouTube for <word>]
System Status            [system]
System Uptime            [uptime]
Send Email               [email]
Exit                     [exit]
''')
        while True:
            if not recognize_speech():
                break
