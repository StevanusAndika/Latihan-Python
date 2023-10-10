import speech_recognition as srec
from gtts import gTTS
import os

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        print('Mendengarkan....')
        suara = mendengar.listen(source, phrase_time_limit=5)
        try:
            print('Diterima...')
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        except:
            pass

    # Check if the variable 'dengar' is defined
    if dengar is not None:
        return dengar
    else:
        print('Tidak ada perintah yang diterima.')
        return None

def ngomong(teks, bahasa='id', putar=True):
    namafile = 'Ngomong.mp3'
    def reading():
        suara = gTTS(text=teks, lang=bahasa, slow=False)
        suara.save(namafile)
        if putar:
            os.system(f'start {namafile}')
    reading()

def run_freya():
    print('Gadis koleris yang suka berimajinasi, terangi harimu dengan senyuman karamelku. Halo,aku Freya!')
    Layanan = perintah()
    if Layanan is not None:
        ngomong(Layanan)

run_freya()
