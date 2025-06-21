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

############################################## coba ####################
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
#     for i in range(1, 8):
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

# ################################# SELENIUM ###########################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import re
# import string  # Untuk huruf a, b, c, ...

# # === 1. Setup Driver ===
# options = Options()
# options.add_argument("--start-maximized")
# # options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)

# try:
#     # === 2. Buka Halaman ===
#     url = "https://safetravel.kemlu.go.id/country-info/b5b7212a-4cb2-43df-95d8-6c8c742a41de"
#     driver.get(url)

#     # === 3. Mapping tab dan container_id ===
#     tab_mapping = {
#         "tab8": "safe-travel-show-more-tourist",
#         "tab9": "safe-travel-show-more-culinary",
#         "tab10": "safe-travel-show-more-worship",
#         "tab11": "safe-travel-show-more-hospital"
#     }

#     for tab_label, container_id in tab_mapping.items():
#         WebDriverWait(driver, 60).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, f"label[for='{tab_label}']"))
#         ).click()

#         tab_number = re.search(r'\d+', tab_label).group()
#         swipe_tab_id = f"swipe-tab-{tab_number}"

#         WebDriverWait(driver, 30).until(
#             EC.visibility_of_element_located((By.ID, swipe_tab_id))
#         )

#         time.sleep(2)

#         try:
#             tab_section = driver.find_element(By.ID, swipe_tab_id)
#             h4_title = tab_section.find_element(By.TAG_NAME, "h4").text.strip()
#         except:
#             h4_title = "Judul Tidak Ditemukan"

#         print(f"\n{tab_number}. {h4_title}\n")

#         WebDriverWait(driver, 30).until(
#             EC.visibility_of_element_located((By.ID, container_id))
#         )

#         container = driver.find_element(By.ID, container_id)
#         cards = container.find_elements(By.CLASS_NAME, "card")

#         if not cards:
#             print(f"❌ Tidak ada konten ditemukan pada tab {tab_label}.")
#         else:
#             for i, card in enumerate(cards):
#                 try:
#                     title_span = card.find_element(By.CLASS_NAME, "card-title")
#                     # Menggunakan huruf a, b, c, ...
#                     if i < 26:
#                         letter = string.ascii_lowercase[i]
#                     else:
#                         letter = f"{string.ascii_lowercase[i // 26 - 1]}{string.ascii_lowercase[i % 26]}"  # aa, ab, ...
#                     print(f"{letter}. {title_span.text}")
#                 except:
#                     print(f"{letter}. (judul tidak ditemukan)")

# except Exception as e:
#     print("Terjadi kesalahan:", e)

# finally:
#     driver.quit()

############################### GABUNGAN ####################################
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import string
import os

# === Hasil akhir gabungan ===
hasil_akhir = ""

# === PART 1: Requests untuk tab 1 - 7 ===
url = 'https://safetravel.kemlu.go.id/country-info/b5b7212a-4cb2-43df-95d8-6c8c742a41de'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for i in range(1, 8):
        tab_id = f'swipe-tab-{i}'
        div_konten = soup.find('div', id=tab_id)

        if div_konten:
            h4 = div_konten.find('h4')
            judul = h4.get_text(strip=True) if h4 else f"Tab {i}"
            hasil_akhir += f"{i}. {judul}\n"

            isi = div_konten.get_text(separator='\n', strip=True)
            hasil_akhir += isi + "\n\n"
        else:
            hasil_akhir += f"{i}. Tidak ditemukan konten untuk {tab_id}\n\n"
else:
    hasil_akhir += f"Gagal mengambil data tab 1-7. Status: {response.status_code}\n\n"

# === PART 2: Selenium untuk tab 8 - 11 ===
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
    driver.get(url)

    tab_mapping = {
        "tab8": "safe-travel-show-more-tourist",
        "tab9": "safe-travel-show-more-culinary",
        "tab10": "safe-travel-show-more-worship",
        "tab11": "safe-travel-show-more-hospital"
    }

    for tab_label, container_id in tab_mapping.items():
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"label[for='{tab_label}']"))
        ).click()

        tab_number = re.search(r'\d+', tab_label).group()
        swipe_tab_id = f"swipe-tab-{tab_number}"

        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, swipe_tab_id))
        )

        time.sleep(2)

        try:
            tab_section = driver.find_element(By.ID, swipe_tab_id)
            h4_title = tab_section.find_element(By.TAG_NAME, "h4").text.strip()
        except:
            h4_title = "Judul Tidak Ditemukan"

        hasil_akhir += f"{tab_number}. {h4_title}\n"

        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, container_id))
        )

        container = driver.find_element(By.ID, container_id)
        cards = container.find_elements(By.CLASS_NAME, "card")

        if not cards:
            hasil_akhir += f"❌ Tidak ada konten ditemukan pada tab {tab_label}.\n\n"
        else:
            for i, card in enumerate(cards):
                try:
                    title_span = card.find_element(By.CLASS_NAME, "card-title")
                    if i < 26:
                        letter = string.ascii_lowercase[i]
                    else:
                        letter = f"{string.ascii_lowercase[i // 26 - 1]}{string.ascii_lowercase[i % 26]}"
                    hasil_akhir += f"{letter}. {title_span.text}\n"
                except:
                    hasil_akhir += f"{letter}. (judul tidak ditemukan)\n"
            hasil_akhir += "\n"

except Exception as e:
    hasil_akhir += f"Terjadi kesalahan: {e}\n"

finally:
    driver.quit()

# === Simpan ke file ===
os.makedirs('data', exist_ok=True)
with open('data/hasil_scraping_safetravel.txt', 'w', encoding='utf-8') as f:
    f.write(hasil_akhir)

print("✅ Scraping selesai. Data disimpan di 'data/hasil_scraping_safetravel.txt'")
