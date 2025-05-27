# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# import json


# def scrape_data():
#     # Buka website
#     website = "https://peduliwni.kemlu.go.id/beranda.html"
#     driver_path = r"chromedriver.exe"
#     service = Service(driver_path)
#     driver = webdriver.Chrome(service=service)
#     driver.get(website)

#     # Scraping facilitation
#     facilitations = driver.find_elements(By.CLASS_NAME, "text-fasilitas")
#     data = [facilitate.text for facilitate in facilitations]

#     # Choose informasi pelayanan
#     information_services = driver.find_element(By.XPATH, "//a[text()='Informasi Pelayanan']")
#     information_services.click()
#     time.sleep(5)

#     # Choose Amerika Serikat
#     usa = driver.find_element(By.XPATH, "//a[img[@alt='AMERIKA']]")
#     usa.click()
#     time.sleep(5)

#     # Select KBRI Washington
#     embassy = driver.find_element(By.XPATH, "//a[h4[text()='KBRI Washington D.C.']]")
#     embassy.click()
#     time.sleep(5)

#     # Scraping information
#     services = driver.find_elements(By.TAG_NAME, 'tr')
#     for service in services:
#         data.append(service.text)

#     # Close the driver
#     driver.quit()

#     # Simpan hasil scraping ke file (opsional)
#     with open("data/scraped_data.txt", "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)

#     return data

# if __name__ == "__main__":
#     scraped_data = scrape_data()
#     print("Scraping selesai! Data disimpan.")

############################################### coba ####################
# import requests
# from bs4 import BeautifulSoup

# url = 'https://safetravel.kemlu.go.id/country-info/b5b7212a-4cb2-43df-95d8-6c8c742a41de'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     hasil_akhir = ""

#     # Loop dari swipe-tab-1 hingga swipe-tab-10
#     for i in range(1, 11):
#         tab_id = f'swipe-tab-{i}'
#         div_konten = soup.find('div', id=tab_id)

#         if div_konten:
#             # Tambahkan nomor di setiap h4
#             for h4 in div_konten.find_all('h4'):
#                 h4.string = f"{i}. {h4.get_text(strip=True)}"

#             # Ambil teks dari div
#             teks = div_konten.get_text(separator='\n', strip=True)
#             hasil_akhir += teks + '\n\n'  # Tambah baris kosong antar tab
#         else:
#             hasil_akhir += f"{i}. Tidak ditemukan konten untuk {tab_id}\n\n"

#     # Cetak hasil akhir
#     print(hasil_akhir)

#     # Simpan ke file
#     with open('data/hasil_scraping_safetravel.txt', 'w', encoding='utf-8') as f:
#         f.write(hasil_akhir)
# else:
#     print(f"Gagal mengambil data. Status: {response.status_code}")

# import requests
# from bs4 import BeautifulSoup

# url = 'https://safetravel.kemlu.go.id/country-info/b5b7212a-4cb2-43df-95d8-6c8c742a41de'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     hasil_akhir = ""

#     for i in range(1, 12):
#         tab_id = f'swipe-tab-{i}'
#         div_konten = soup.find('div', id=tab_id)

#         hasil_akhir += f"{i}. Informasi dari {tab_id}\n"

#         if div_konten:
#             for h4 in div_konten.find_all('h4'):
#                 h4.string = f"{i}. {h4.get_text(strip=True)}"
#             teks = div_konten.get_text(separator='\n', strip=True)
#             hasil_akhir += teks + '\n'
#         else:
#             hasil_akhir += f"{i}. Tidak ditemukan konten untuk {tab_id}\n"

#         # Tambahan berdasarkan isi kartu
#         extra_ids = {
#             8: 'safe-travel-show-more-tourist',
#             9: 'safe-travel-show-more-culinary',
#             10: 'safe-travel-show-more-worship',
#             11: 'safe-travel-show-more-hospital',
#         }

#         if i in extra_ids:
#             extra_div = soup.find('div', id=extra_ids[i])
#             if extra_div:
#                 card_titles = extra_div.select('span.card-title')
#                 if card_titles:
#                     hasil_akhir += "\nInformasi Tambahan:\n"
#                     for title in card_titles:
#                         hasil_akhir += f"- {title.get_text(strip=True)}\n"
#                 else:
#                     hasil_akhir += "Tidak ditemukan informasi tambahan di .card-title\n"
#             else:
#                 hasil_akhir += "Tidak ditemukan div tambahan\n"

#         hasil_akhir += '\n'

#     print(hasil_akhir)

#     with open('data/hasil_scraping_safetravel.txt', 'w', encoding='utf-8') as f:
#         f.write(hasil_akhir)
# else:
#     print(f"Gagal mengambil data. Status: {response.status_code}")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === 1. Setup Driver ===
options = Options()
options.add_argument("--start-maximized")  # Buka browser dengan ukuran penuh
# options.add_argument("--headless")       # Uncomment jika ingin headless
driver = webdriver.Chrome(options=options)

# === 2. Buka Halaman ===
url = "https://safetravel.kemlu.go.id/country-info/b5b7212a-4cb2-43df-95d8-6c8c742a41de"  # ganti dengan link yang kamu inspect
driver.get(url)

# Tunggu sampai tab swipe muncul (naikkan timeout)
WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "swipe-tab-8")))

# === 3. Data Tab ===
tabs = {
    "swipe-tab-8": "safe-travel-show-more-tourist",    # Tempat Wisata
    "swipe-tab-9": "safe-travel-show-more-culinary",   # Kuliner
    "swipe-tab-10": "safe-travel-show-more-worship",   # Tempat Ibadah
    "swipe-tab-11": "safe-travel-show-more-hospital",  # Fasilitas Kesehatan
}

# === 4. Loop setiap tab ===
for tab_id, content_id in tabs.items():
    print(f"\n{tab_id}: Mengecek konten dari {content_id}...")

    try:
        # Tunggu tab bisa diklik dengan timeout yang lebih panjang
        tab_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, tab_id))
        )
        tab_element.click()

        # Setelah klik, beri delay agar konten benar-benar render
        time.sleep(5)

        # Tunggu konten benar-benar visible
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, content_id))
        )

        # Ambil isi dari kontennya
        content_div = driver.find_element(By.ID, content_id)
        cards = content_div.find_elements(By.CLASS_NAME, "card")

        if not cards:
            print("❌ Tidak ditemukan konten dalam div.")
        else:
            for i, card in enumerate(cards):
                try:
                    title = card.find_element(By.CLASS_NAME, "card-title").text
                    print(f"{i+1}. {title}")
                except Exception:
                    print(f"{i+1}. (judul tidak ditemukan)")
    except Exception as e:
        print(f"❌ Gagal mengambil data: {e}")

# === 5. Selesai ===
driver.quit()


