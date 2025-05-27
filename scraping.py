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
import requests
from bs4 import BeautifulSoup

url = 'https://safetravel.kemlu.go.id/country-info/b5b7212a-4cb2-43df-95d8-6c8c742a41de'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    hasil_akhir = ""

    # Loop dari swipe-tab-1 hingga swipe-tab-10
    for i in range(1, 11):
        tab_id = f'swipe-tab-{i}'
        div_konten = soup.find('div', id=tab_id)

        if div_konten:
            # Tambahkan nomor di setiap h4
            for h4 in div_konten.find_all('h4'):
                h4.string = f"{i}. {h4.get_text(strip=True)}"

            # Ambil teks dari div
            teks = div_konten.get_text(separator='\n', strip=True)
            hasil_akhir += teks + '\n\n'  # Tambah baris kosong antar tab
        else:
            hasil_akhir += f"{i}. Tidak ditemukan konten untuk {tab_id}\n\n"

    # Cetak hasil akhir
    print(hasil_akhir)

    # Simpan ke file
    with open('data/hasil_scraping_safetravel.txt', 'w', encoding='utf-8') as f:
        f.write(hasil_akhir)
else:
    print(f"Gagal mengambil data. Status: {response.status_code}")
