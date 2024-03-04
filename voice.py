import speech_recognition as sr
import subprocess

# Tanımlanan fonksiyon, kullanıcının söylediği metni tanır ve buna göre işlem yapar.
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bir dil seçin: Türkçe veya İngilizce")
        print("Şimdi konuşun...")
        audio = recognizer.listen(source)

    try:
        # Tanımlanan dil modeliyle tanınan metni yazdırır.
        spoken_text = recognizer.recognize_google(audio, language='tr-TR')  # Türkçe için 'tr-TR' kullanılıyor.
        print("Söylenen: " + spoken_text)
        if "Türkçe" in spoken_text:
            subprocess.run(["python", "tr_voice.py"])
        elif "İngilizce" in spoken_text:
            subprocess.run(["python", "eng_voice.py"])
        else:
            print("Anlaşılamadı.")
    except sr.UnknownValueError:
        print("Ses anlaşılamadı.")
    except sr.RequestError as e:
        print("Google Speech Recognition servisi çalışmıyor; {0}".format(e))

# Ana fonksiyon, konuşmayı tanıyan fonksiyonu çağırır.
if __name__ == "__main__":
    recognize_speech()
