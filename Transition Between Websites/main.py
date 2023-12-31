# Kodu yazmaya başlamadan önce
# "pip install selenium" ve
# "pip install webdriver-manager" komutlarını çalıştırın.

# Selenium modülünden gerekli kütüphaneleri içe aktarın.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriver'ı başlatın ve gerekli hizmeti ve sürücüyü kullanın.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Sekmeler arasında geçiş yapmak için kullanılacak işlevi tanımlayın. Belirtilen başlığa göre belirtilen web sitesine geçiş yapar.
def sekme_degistir(baslik):
    # Tüm açık sekmeleri gezin.
    for sayfa in driver.window_handles:
        driver.switch_to.window(sayfa)
        # Belirtilen başlık sekmelerden birinde bulunursa, ekrana yazdırın ve döngüden çıkın.
        if baslik in driver.title.lower():
            print(f"{baslik} başlıklı web sitesine geçildi.")
            break

# Kullanıcının hangi web sitesini ziyaret etmek istediğine karar vermesini sağlayan işlevi tanımlayın.
def baslik_al():
    while True:
        baslik = input("Hangi web sitesini ziyaret etmek istersiniz?\n"
                       "Youtube?\n"
                       "Twitch?\n"
                       "ChatGPT?\n"
                       "Google?\n"
                       "Seçiminizi girin: ")
        baslik = baslik.lower()
        return baslik

# Kullanıcının devam etmeye karar vermesini sağlayan işlevi tanımlayın.
def devam_karari():
    karar = input("Programa devam etmek istiyor musunuz?\n"
                  "Evet\n"
                  "Hayır\n"
                  "Seçiminizi girin: ")
    karar = karar.lower()
    return karar

# Programın başlangıcında bilgi mesajını görüntüleyin.
print("Bu program size birkaç web sitesi arasında geçiş yapma imkanı tanır.")

# Web sitelerini birer birer ziyaret edin ve her biri için yeni bir sekme açın.
time.sleep(2)
driver.get("https://www.youtube.com/")
time.sleep(1)
driver.switch_to.new_window("tab")
driver.get("https://www.twitch.tv/")
time.sleep(1)
driver.switch_to.new_window("tab")
driver.get("https://chat.openai.com/")
time.sleep(1)
driver.switch_to.new_window("tab")
driver.get("https://www.google.com.tr/?hl=tr")
time.sleep(3)

# Sonsuz bir döngü başlatın.
while True:

    baslik = baslik_al()

    while True:

        if baslik in ["youtube", "twitch", "chatgpt", "google"]:
            sekme_degistir(baslik)
            break

        else:
            print("Program tarafından tanınmayan bir metin girildi. Lütfen tekrar girin: ")
            baslik = baslik_al()

    karar = devam_karari()

    # Kullanıcı "hayır" derse, programdan çıkın; aksi takdirde devam edin.
    if karar == "hayır":
        print("Programdan çıkıldı.")
        break

    else:
        print("Programa devam ediliyor.")

# Sonsuz bir döngü oluşturduğumuzdan, programın sonlanmasını önlemek için programı bekletiyoruz.
time.sleep(100000000000000000)
