import time as t
import pyautogui as pg
import wikipedia
import subprocess
import urllib.parse
import pyttsx3
import speech_recognition as sr
import pygetwindow as gw
from datetime import datetime as dt
import threading as th


jarvis_sifre = "Tony Stark"
x, y = pg.position()
# ---- Ses Motoru ----


engine = pyttsx3.init()
voices = engine.getProperty('voices')

def jarvis_konus(metin):
    engine.setProperty('voice', voices[0].id)  # 0. ses
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 0.1)
    engine.say(metin)
    engine.runAndWait()

def nexus_konus(metin):
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)  # 1. ses
    else:
        engine.setProperty('voice', voices[0].id)  # fallback
    engine.setProperty('rate', 210)
    engine.setProperty('volume', 0.1)
    engine.say(metin)
    engine.runAndWait()

def saat_kac():
    simdi = dt.now()
    saat = simdi.strftime("%H:%M:%S")
    print(f"The current time is {saat}, sir.")
    jarvis_konus(f"The current time is {saat}, sir.")

def zamanlayici(saniye):
    def geri_sayim():
        jarvis_konus(f"Timer set for {saniye} seconds, sir.")
        t.sleep(saniye)
        jarvis_konus("Time is up, sir.")

    th.Thread(target=geri_sayim).start()

def hava_durumu(komut):
    jarvis_konus("I am giving you the current weather information, sir.")
    if not chrome_acik_mi():
        pg.press("win")
        t.sleep(0.8)
        pg.write("chrome", interval=0.1)
        pg.press("enter")
        t.sleep(3)
    pg.hotkey("ctrl", "l")
    t.sleep(0.3)
    pg.hotkey("ctrl", "t")
    pg.write("https://www.accuweather.com/tr/tr/istanbul/318251/daily-weather-forecast/318251", interval=0.05)
    pg.press("enter")
    jarvis_konus("I'm opened Weather forecast sir")
# ---- Wikipedia fonksiyonu ----
def wiki_arastir(konu):
    wikipedia.set_lang("tr")

def insta_mesaj(kisi, mesaj):
    jarvis_konus(f"Okey, I'm Opening İnstagram and sending message to {kisi} sir.")
    if not chrome_acik_mi():
        pg.press("win")
        t.sleep(0.4)
        pg.write("chrome")
        t.sleep(0.4)
        pg.press("enter")
        t.sleep(3)
    pg.hotkey("ctrl", "l")
    t.sleep(0.4)
    pg.write("instagram")
    pg.press("enter")
    t.sleep(6)
    pg.click(33, 455, duration=0.5)
    t.sleep(1)
    pg.click(247, 184, duration=0.5)
    t.sleep(0.4)
    pg.write(mesaj, interval=0.5)
    t.sleep(0.2)
    pg.press("enter")
    jarvis_konus("İnstagram message sent successfully sir.")

def ezan_vakti():
    jarvis_konus("Okey sir I'm opening times of namaz!")
    pg.press("win")
    t.sleep(5)
    pg.hotkey("ctrl", "l")
    t.sleep(1)
    pg.write("https://namazvakitleri.diyanet.gov.tr/tr-TR/9541/istanbul-icin-namaz-vakti", interval=0.05)
    t.sleep(2)
    pg.press("enter"), jarvis_konus("The site is opened sir")
    

def haber_komutu():
    jarvis_konus("I'm opening the news web site and live news!")
    pg.press("win")
    t.sleep(0.5)
    pg.write("chrome", interval=0.05)
    t.sleep(0.5)
    pg.press("enter")
    t.sleep(5)
    pg.hotkey("ctrl", "t")
    t.sleep(1)
    pg.hotkey("ctrl", "l")
    t.sleep(0.4)
    pg.write("https://www.cnnturk.com/", interval=0.05), jarvis_konus("I'm opening cnnturk's web site sir.")
    t.sleep(3)
    pg.hotkey("ctrl", "t")
    t.sleep(0.4)
    pg.write("y")
    pg.press("enter")
    pg.hotkey("tab")
    t.sleep(0.4)
    pg.hotkey("tab")
    t.sleep(0.4)
    pg.hotkey("tab")
    t.sleep(0.4)
    pg.hotkey("tab")
    t.sleep(0.4)
    pg.write("cnn canlı", interval=0.2), jarvis_konus("I'm opening cnnturk live on youtube.")
    t.sleep(0.3)
    pg.press("enter")
    pg.hotkey("tab")
    t.sleep(0.4)
    pg.hotkey("tab")
    t.sleep(0.4)
    pg.hotkey("enter")
    t.sleep(0.4)
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("enter")
    jarvis_konus("Sir mission complated!")



def telefon_b_acik_mi():
    try:
        tasks = subprocess.check_output("tasklist", shell=True).decode().lower()
        return "phoneexperiencehost.exe" in tasks
    except:
        return False


# ---- Chrome açık mı ----
def chrome_acik_mi():
    try:
        tasks = subprocess.check_output("tasklist", shell=True).decode().lower()
        return "chrome.exe" in tasks
    except:
        return False

def turkce_to_ingilizce(metin):
    ceviri_tablosu = str.maketrans(
        "çÇğĞıİöÖşŞüÜ",
        "cCgGiIoOsSuU"
    )
    return metin.translate(ceviri_tablosu)


def whatsapp_mesaj_at():
    jarvis_konus("Who should I send the message to sir?")
    kisi = input("Mesaj kime gidecek efendim? ")

    jarvis_konus("What is the message sir?")
    mesaj = input("Mesaj: ")

    # 🔥 Türkçe karakterleri otomatik düzelt
    kisi = turkce_to_ingilizce(kisi)
    mesaj = turkce_to_ingilizce(mesaj)

    jarvis_konus(f"Opening WhatsApp and sending message to {kisi} sir.")

    pg.press("win")
    t.sleep(0.7)
    pg.write("whatsapp", interval=0.1)
    pg.press("enter")
    t.sleep(10)

    pg.hotkey("ctrl", "f")
    t.sleep(0.5)

    pg.write(kisi, interval=0.1)
    t.sleep(1)

    pg.press("tab")
    pg.press("tab")
    t.sleep(1)
    pg.press("enter")
    t.sleep(1)

    pg.write(mesaj, interval=0.05)
    t.sleep(1)
    pg.press("enter"), jarvis_konus("WhatsApp message sent successfully sir.")


def telefonu_one_getir():
    try:
        for w in gw.getWindowsWithTitle("Telefon"):
            if w.isMinimized:
                w.restore()
            else:
                w.minimize()
                w.restore()
            w.activate()
            return True
    except Exception as e:
        print("Hata:", e)
        return False

    return False




def telefon_baglantisi(kisi):

    if not telefon_b_acik_mi():
        subprocess.Popen("start ms-phone:", shell=True)
        t.sleep(5)
    # Arama kısmına git
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    t.sleep(1)
    pg.press("enter")
    t.sleep(1)

    pg.write(kisi, interval=0.15)
    t.sleep(2)

    pg.press("down")
    t.sleep(1)

    pg.press("enter")
    t.sleep(1)

    # Ara butonuna git
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.05)
    pg.press("tab")
    t.sleep(0.5)
    pg.press("enter")
    jarvis_konus(f"I'm calling {kisi} sir")

def not_alma(metin):
    jarvis_konus("Okey sir I'm opening notbook and I will write what have you want.")
    pg.press("win")
    t.sleep(0.5)
    pg.write("not defteri", interval=1)
    t.sleep(0.5)
    pg.press("enter")
    t.sleep(1)
    pg.hotkey("ctrl", "t")
    t.sleep(1)
    pg.write(metin, interval=1)
    jarvis_konus("okey sir I'm writed")

def maçkolik(spor):
    jarvis_konus("okey sir I'm opening mackolik at web site")
    if not chrome_acik_mi():
        pg.press("win")
        t.sleep(0.4)
        pg.write("chrome", interval=0.2)
        t.sleep(0.4)
        pg.press("enter")
        t.sleep(3)
    
    pg.press("win")
    pg.write("chrome", interval=0.05)
    t.sleep(0.5)
    pg.press("enter")
    t.sleep(3)
    pg.hotkey("ctrl", "l")
    t.sleep(0.5)
    
    
    while True:
        
        if spor == "basketbol":
            pg.write("https://www.mackolik.com/basketbol/canli-sonuclar", interval=0.05)
            t.sleep(1)
            pg.press("enter")
            jarvis_konus("Basketball statics is opened sir")
            break
        elif spor == "futbol":
            pg.write("https://www.mackolik.com/futbol/canli-sonuclar", interval=0.05)
            t.sleep(1)
            pg.press("enter")
            jarvis_konus("Football statics is opened sir")
            break
        else:
            jarvis_konus("I don't understand you sir")
            continue
    jarvis_konus("Matchkolik is opened sir")


# ---- Google araştırma ----
def google_arastir_insansi(konu):
    if not chrome_acik_mi():
        pg.press("win")
        t.sleep(0.8)
        pg.write("chrome", interval=0.1)
        pg.press("enter")
        t.sleep(3)
    pg.press("tab")
    t.sleep(1)
    pg.press("enter")
    t.sleep(1)
    pg.hotkey("ctrl", "l")
    t.sleep(0.3)
    pg.hotkey("ctrl", "t")
    arama_url = f"https://www.google.com/search?q={urllib.parse.quote(konu)}"
    pg.write(arama_url, interval=0.05)
    pg.press("enter")
    jarvis_konus("subject searched,mission complated sir")

# ---- Doğal dil ayrıştırma ----
def komut_ayristir(komut):
    komut = komut.lower()

    if "google" in komut:
        konu = komut.replace("google", "").replace("araştır", "").strip()
        return "google", konu

    if "wikipedia" in komut:
        konu = komut.replace("wikipedia", "").replace("araştır", "").strip()
        return "wiki", konu

    return None, None

# ---- Jarvis Menüsü ----
def jarvis_menu():
    jarvis_konus("Welcome back,sir!")
    while True:

        komut = input(
            "\n[JARVIS]\n"
            "1 - Uygulama aç\n"
            "2 - Google araştırma\n"
            "3 - Wikipedia araştırma\n"
            "4 - WhatsApp mesaj gönder\n"
            "5 - İnstagram mesaj yolla\n"
            "6 - Hava durumu\n"
            "7 - Ezan Vakitleri\n"
            "8 - Maçkolik İstatistikleri\n"
            "9 - Not Defteri\n"
            "10 - Telefon Bağlantısı\n"
            "11 - Haber paneli\n"
            "12 - Saat Kaç\n"
            "13 - Saniyelik Zamanlayıcı Başlat\n"
            "20 - Nexus'a geri dön\n> "
        ).lower()
        
        

        if komut == "1" or any(x in komut for x in [
            "uygulama aç"
            "jarvis uygulama aç"
            "start app"
            "jarvis start app"
        ]):
            jarvis_konus("Application name sir?")
            app = input("Uygulama adı: ")
            pg.press("win")
            t.sleep(0.8)
            pg.write(app, interval=0.1)
            pg.press("enter")
            jarvis_konus("The application is opened sir!")


        elif komut == "2" or any(x in komut for x in [
                "google da arat",
                "google da araştır",
                "google araştır",
                "google arat",
                "search google",
                "google searching",
                "jarvis open google and search",
                "jarvis open google and start searching"

        ]):
            jarvis_konus("What is the subject sir?")
            konu = input("Ne araştırılsın? ")
            jarvis_konus(f"I'm searching for {konu} sir.")
            google_arastir_insansi(konu)
        

        elif komut == "3" or any(x in komut for x in [
                "wikipedia da araştır",
                "jarvis wikipedia da araştırma yap",
                "wikipedia araştır",
                "search on wikipedia",
                "start searching on wikipedia"
        ]):
            jarvis_konus("What is the subject sir?")
            konu = input("Ne araştırılsın? ")
            sonuc = wiki_arastir(konu)
            print("\n[Wikipedia]")
            print(sonuc)
            jarvis_konus("Sir the answer is your computer,I can't read that because I don't know turkish!")
        
        elif komut == "4" or any(x in komut for x in [
                "wp mesaj",
                "whatsappdan mesaj at",
                "whatsapp mesaj",
                "send the message on whatsapp",
                "send message on whatsapp"
        ]):
            whatsapp_mesaj_at()

        
        elif komut == "5" or any(x in komut for x in [
            "send message on instagram",
            "jarvis send message on instagram"
        ]):
            jarvis_konus("Who should I send the message to sir?")
            kisi = input("Kime? ")

            jarvis_konus("What is the message sir?")
            mesaj = input("Mesaj: ")
            insta_mesaj(kisi, mesaj)
        
        elif komut == "6" or any(x in komut for x in [
            "hava durumunu göster",
            "hava durumunu aç",
            "show weather forecast",
            "jarvis hava durumunu göster",
            "jarvis hava durumunu aç",
            "jarvis show weather forecast"


        ]):
            hava_durumu(komut)
        
        elif komut == "7" or any(x in komut for x in [
            "ezan vakitlerini aç",
            "ezan vakitlerini göster",
            "ezan vakitleri ne zaman",
            "show time of namaz"
        ]):
            ezan_vakti()
        
        elif komut == "8" or any(x in komut for x in [
            "Maçkolik aç",
            "jarvis maçkolik aç",
            "start matchcholik"
        ]):
            spor = input("Basketbol verileri mi futbol verilerini mi istersiniz? ")
            maçkolik(spor)
        
        elif komut == "9" or any(x in komut for x in [
            "not defterine not yaz",
            "not defterini aç",
            "open notbook"
        ]):
            metin = input("Notu Giriniz: ")
            not_alma(metin)

        elif komut == "10" or any(x in komut for x in [
            "arama yap",
            "birini ara",
            "call someone",
            "jarvis birini ara",
            "jarvis call someone"
        ]):
            jarvis_konus("Who would you like me to call, sir?")
            kisi = input("Kimi aramak istiyorsunuz efendim: ")
            telefonu_one_getir()
            telefon_baglantisi(kisi)
            


        elif komut == "11" or any(x in komut for x in [
            "haberleri aç",
            "haberleri göster",
            "jarvis haberleri aç",
            "jarvis open news"
        ]):
            haber_komutu()

        elif komut == "12" or any(x in komut for x in [
            "saat kaç",
            "jarvis saat kaç",
            "jarvis saati söyle",
            "jarvis whats the clock"
        ]):
            saat_kac()


        elif komut == "20" or any(x in komut for x in [
            "nexusa bağlan",
            "jarvis nexusa bağlan"
            "jarvis connect to nexus"
        ]):
            jarvis_konus("Returning to Nexus sir.")
            break

        else:
            tip, konu = komut_ayristir(komut)
            if tip == "google":
                google_arastir_insansi(konu)
            elif tip == "wiki":
                sonuc = wiki_arastir(konu)
                print(sonuc)
                jarvis_konus(sonuc)
            else:
                jarvis_konus("I don't understand you sir.")

# ---- Nexus Menüsü ----
def nexus_menu():
    while True:
        secim = input(
            "\n[NEXUS]\n"
            "1 - Jarvis'e bağlan\n"
            "2 - Çıkış\n>"
        ).lower()
        

        

        if secim == "1" or "jarvis" in secim.lower():
            nexus_konus("Please enter Jarvis password sir.")
            sifre = input("Jarvis's password: ")
            
        
            if sifre == jarvis_sifre:
                nexus_konus("Access granted. Jarvis online.")
                jarvis_menu()
                break
                
                
            else:
                nexus_konus("Wrong password sir.")
                continue
                    

        elif secim == "2" or "çıkış" in secim:
            nexus_konus("Shutting down Nexus. Goodbye sir.")
            break
            

        else:
            nexus_konus("I'm just a security system, I can't answer that.")

# ---- Program Başlangıcı ----
print("Nexus core initializing.")
nexus_konus("Nexus core initializing.")
t.sleep(2)
print("Biometric verification available.")
nexus_konus("Biometric verification available.")
t.sleep(1)
print("Look at your PC's camera")
nexus_konus("Look at your PC's camera")

print("Biometric password scanning", end="", flush=True)
nexus_konus("Biometric password scanning")

for i in range(10):
    t.sleep(0.5)
    print(".", end="", flush=True)

print("\nWelcome back sir!")
nexus_konus("Welcome back sir")
t.sleep(1)



nexus_menu()
