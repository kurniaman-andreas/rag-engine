# from datasets import Dataset
# import rag
# from ragas import evaluate
# from ragas.metrics import (
#     faithfulness,
#     answer_relevancy,
#     context_recall,
#     context_precision,
# )
# # initialize chatbot
# rag.initialize_chatbot()

# # Pastikan kamu mengakses variabel dari namespace `rag`
# rag_chain = rag.rag_chain
# retriever = rag.retriever

# questions = [
#     "Berapa kode telepon internasional Singapura?",
#     "Apakah WNI perlu visa untuk masuk ke Singapura?",
#     "Apa bentuk pemerintahan Singapura?",
#     "Apa yang harus saya lakukan jika paspor saya hilang di Singapura?",
#     "Apa larangan hukum yang harus saya perhatikan di Singapura?",
#     "Apakah saya bisa membeli SIM card di Singapura?",
#     "Di mana saya bisa menemukan masjid di Singapura?",
#     "Apakah boleh membawa rokok ke Singapura?",
#     "Apa musim yang perlu diwaspadai di Singapura?",
#     "Apa restoran Indonesia yang direkomendasikan di Singapura?"
# ]

# ground_truths = [
#     "Kode telepon internasional Singapura adalah +65.",
#     "Tidak perlu. WNI pemegang paspor reguler, dinas, atau diplomatik bebas visa selama 30 hari.",
#     "Singapura memiliki bentuk pemerintahan Republik Parlementer Unikameral.",
#     "Segera laporkan kehilangan ke pihak berwenang setempat dan hubungi KBRI Singapura di WhatsApp +65 9648 0017 atau telepon +65 6737 7422.",
#     "Larangan mencakup membawa narkoba, merokok di ruang publik, membuang sampah sembarangan, konsumsi alkohol di area publik setelah pukul 22:30, dan membawa permen karet.",
#     "Bisa, namun pembelian SIM card di Singapura wajib menunjukkan paspor.",
#     "Beberapa masjid di Singapura antara lain Sultan Mosque, Masjid Assyafaah, Masjid An-Nur, Masjid Al-Iman, dan Masjid Ar-Raudhah.",
#     "Boleh, namun wajib membayar cukai. Hindari merokok tanpa cukai karena itu ilegal.",
#     "Musim monsun berlangsung pada bulan Desember–Maret dan Juni–September.",
#     "Restoran Indobox adalah salah satu tempat yang menyajikan makanan Indonesia di Singapura."
# ]

# answers = []
# contexts = []

# # Inference
# for query in questions:
#   answers.append(
#     rag_chain.invoke({
#         "question": query,
#         "chat_history": []
#     })  
# )
#   contexts.append([docs.page_content for docs in retriever.get_relevant_documents(query)])
# #   contexts.append([doc.page_content for doc in retriever.invoke(query)])


# # To dict
# data = {
#     "question": questions,
#     "answer": answers,
#     "contexts": contexts,
#     "reference": ground_truths
# }

# # Convert dict to dataset
# dataset = Dataset.from_dict(data)



# result = evaluate(
#     dataset = dataset, 
#     metrics=[
#         context_precision,
#         context_recall,
#         faithfulness,
#         answer_relevancy,
#     ],
# )

# df = result.to_pandas()
# df.to_csv("evaluation_results.csv", index=False)

from datasets import Dataset
import rag
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_similarity,
    context_recall,
    context_precision,
    answer_correctness
)
import csv

# initialize chatbot
rag.initialize_chatbot()

# akses variabel dari namespace rag
rag_chain = rag.rag_chain
retriever = rag.retriever

questions = [
    "Apa bentuk pemerintahan Singapura?",
    "Apa kode telepon untuk negara Singapura?",
    "Apa Zona waktu Singapura? GMT berapa?",
    "Di mana alamat KBRI di Singapura?",
    "Berapa lama WNI bisa masuk di Singapura tanpa visa?",
    "Berapa minimal masa berlaku paspor untuk masuk ke Singapura?",
    "Apa kewajiban saat masuk atau keluar dari Singapura?",
    "Disarankan hadir berapa jam sebelum keberangkatan jika ingin tiba di Bandara Changi?",
    "Jenis soket apa yang digunakan di Singapura?",
    "Apa nomor darurat untuk menghubungi polisi di Singapura?",
    "Apa yang harus dilakukan jika kehilangan paspor di Singapura?",
    "Apa alamat kantor imigrasi Singapura di Jakarta?",
    "Berapa nomor telepon kantor imigrasi Singapura di Jakarta?",
    "Apa saja potensi kriminalitas yang harus diwaspadai di Singapura?",
    "Apa potensi terorisme di Singapura menurut informasi ini?",
    "Apa musim monsoon di Singapura?",
    "Apa hukuman untuk tindak pidana narkotika di Singapura?",
    "Apakah WNI berhak mendapatkan notifikasi penahanan di Singapura?",
    "Barang apa saja yang dilarang untuk diimpor ke Singapura?",
    "Jam berapa konsumsi alkohol dilarang di area publik Singapura?",
    "Apa larangan merokok di Singapura?",
    "Apa larangan umum terkait perilaku di ruang publik Singapura?",
    "Apakah permen karet dijual di Singapura?",
    "Apakah wajib bayar cukai rokok di Singapura?",
    "Apa larangan menyeberang jalan di Singapura?",
    "Apa mata uang resmi yang digunakan di Singapura?",
    "Di mana tempat penukaran uang yang banyak tersedia di Singapura?",
    "Apa saja operator telekomunikasi di Singapura?",
    "Apa persyaratan pembelian SIM card di Singapura?",
    "Apa rekomendasi terkait asuransi untuk wisatawan ke Singapura?",
    "Siapa yang bertanggung jawab atas biaya pengobatan di Singapura?",
    "Apa nomor darurat ambulans di Singapura?",
    "Apa nama masjid yang mendapat rating tertinggi di Singapura?",
    "Sebutkan salah satu tempat wisata dengan rating bintang lima di Singapura!",
    "Apa nama restoran cepat saji yang ada di Marina Singapura?",
    "Apa nama bandara utama di Singapura?",
    "Berapa lama waktu disarankan untuk hadir sebelum keberangkatan di bandara utama Singapura?",
    "Apa nama museum yang termasuk dalam daftar tempat wisata di Singapura?",
    "Sebutkan satu risiko bencana alam di Singapura!",
    "Apa nomor darurat untuk menghubungi polisi di Singapura?",
    "Apa alamat KBRI Singapura?",
    "Apa kontak WhatsApp KBRI Singapura untuk jam kerja?",
    "Apa larangan terkait pengambilan foto di Singapura?",
    "Apa larangan terkait mabuk di ruang publik di Singapura?",
    "Apa yang harus dilakukan untuk pengamanan dokumen penting di Singapura?",
    "Sebutkan satu restoran dengan rating bintang empat di Singapura!",
    "Apa larangan terkait merokok di ruang AC di Singapura?",

    #  "Apa jenis sistem hukum yang berlaku di Singapura?",
    # "Berapa lama durasi bebas visa bagi WNI di Singapura untuk paspor dinas dan diplomatik?",
    # "Bagaimana prosedur perpanjangan visa di Singapura?",
    # "Apa saja dokumen yang harus disiapkan saat masuk ke Singapura?",
    # "Apakah Singapura menerapkan karantina wajib bagi pengunjung saat pandemi?",
    # "Bagaimana prosedur pengajuan izin kerja bagi WNA di Singapura?",
    # "Apa larangan terkait senjata api di Singapura?",
    # "Apa saja jenis denda yang umum dikenakan di Singapura?",
    # "Bagaimana aturan penggunaan transportasi umum di Singapura?",
    # "Apa sanksi bagi pelanggaran aturan lalu lintas di Singapura?",
    # "Apakah ada batasan usia minimal mengemudi di Singapura?",
    # "Apa jenis asuransi kesehatan yang disarankan selama di Singapura?",
    # "Apa kebijakan pengembalian pajak untuk wisatawan di Singapura?",
    # "Apa larangan terkait narkotika yang harus diketahui di Singapura?",
    # "Bagaimana prosedur pelaporan kehilangan barang di Singapura?",
    # "Apa langkah yang harus dilakukan jika terjadi kecelakaan lalu lintas di Singapura?",
    # "Apakah warga negara asing boleh membawa hewan peliharaan ke Singapura?",
    # "Bagaimana aturan pengiriman barang dari luar ke Singapura?",
    # "Apa protokol keamanan saat menghadiri acara publik di Singapura?",
    # "Bagaimana aturan penggunaan drone di Singapura?",
    # "Apa kebijakan Singapura terkait penyebaran berita hoax?",
    # "Apa yang harus dilakukan jika mengalami sakit saat di Singapura?",
    # "Bagaimana cara menghubungi KBRI Singapura dalam keadaan darurat?",
    # "Apa larangan terkait pakaian dan penampilan di Singapura?",
    # "Bagaimana aturan kepemilikan properti bagi WNA di Singapura?",
    # "Apa jenis pajak yang berlaku di Singapura bagi penduduk dan wisatawan?",
    # "Apa kebijakan Singapura terhadap limbah elektronik dan daur ulang?",
    # "Bagaimana aturan parkir kendaraan di Singapura?",
    # "Apakah Singapura memiliki aturan ketat terhadap kebisingan?",
    # "Apa jenis dokumen yang diperlukan untuk menyewa tempat tinggal di Singapura?",
    # "Bagaimana cara membuka rekening bank bagi WNA di Singapura?",
    # "Apa aturan terkait penggunaan masker di ruang publik Singapura saat pandemi?",
    # "Bagaimana sistem pendidikan bagi anak WNA yang tinggal di Singapura?",
    # "Apa larangan terkait penggunaan plastik sekali pakai di Singapura?",
    # "Bagaimana prosedur pengaduan terhadap layanan publik di Singapura?",
    # "Apa protokol kesehatan saat menggunakan transportasi umum di Singapura?",
    # "Apakah ada aturan khusus terkait penggunaan WiFi publik di Singapura?",
    # "Apa saja tempat wisata ramah keluarga di Singapura?",
    # "Apa rekomendasi kuliner halal di Singapura?",
    # "Bagaimana aturan mengenai jam operasional toko dan restoran di Singapura?",
    # "Apa larangan terkait penggunaan ponsel saat mengemudi di Singapura?",
    # "Bagaimana sistem pengelolaan sampah di Singapura?",
    # "Apakah ada aturan khusus untuk wisatawan muslim di Singapura?",
    # "Apa saja fasilitas kesehatan yang dapat diakses oleh WNA di Singapura?",
    # "Bagaimana aturan terkait pengoperasian ojek online di Singapura?",
    # "Apa prosedur bea cukai barang bawaan saat tiba di Singapura?",
    # "Bagaimana kebijakan Singapura terhadap hak cipta dan paten?",
    # "Apa tindakan yang diambil oleh pemerintah Singapura terhadap pelanggaran lingkungan?",
    # "Apa aturan tentang pemakaian alkohol di tempat umum di Singapura?"
]

ground_truths = [
    "Bentuk pemerintahan Singapura yaitu Republik Parlementer Unikameral",
    "Kode telepon negara Singapura yaitu +65",
    "Zona waktu Singapura adalah GMT+8 (1 jam lebih cepat dari Jakarta)",
    "Kedutaan Besar Republik Indonesia, 7 Chatsworth Road, Singapore 249761",
    "WNI bisa masuk tanpa Visa selama 30 hari untuk paspor reguler, dinas, dan diplomatik",
    "Syarat masa berlaku paspor minimal 6 bulan",
    "Kewajiban saat masuk/keluar Singapura adalah pemindaian sidik jari ",
    "Disarankan kita hadir 2 jam sebelum keberangkatan di Bandara Changi",
    "Jenis soket di Singapura adalah soket tipe G",
    "Nomor darurat untuk menghubungi polisi adalah 999",
    "Simpan paspor dan dokumen penting, segera lapor ke KBRI jika hilang",
    "Jl. H.R Rasuna Said Blok X4 Kav. 2, Kuningan, Jakarta 12950",
    "+62 21 2995 0400",
    "Waspadai penipuan properti dan hindari transaksi tunai dalam jumlah besar",
    "Potensi kecil, tetap waspada di hotel, klub malam, bar, pasar, stasiun kereta, dan tempat ibadah",
    "Musim Monsoon: Desember-Maret dan Juni-September",
    "Narkotika dapat dihukum mati",
    "Ya, WNI berhak meminta notifikasi ke KBRI jika ditahan",
    "Mengimpor barang bajakan dan rokok elektrik dilarang",
    "Konsumsi alkohol dilarang pukul 22:30 sampai 07:00 di area publik",
    "Merokok dilarang di ruang publik, AC, dan zona larangan",
    "Dilarang membuang sampah sembarangan, meludah, graffiti, dan mengambil foto tanpa izin",
    "Permen karet tidak dijual di Singapura",
    "Wajib bayar cukai rokok; hindari merokok tanpa cukai",
    "Dilarang menyeberang jalan sembarangan",
    "Dollar Singapura (SGD)",
    "Money changer banyak tersedia di area wisata",
    "Operator telekomunikasi utama adalah Singtel, M1, StarHub, Circles.Life, dan TPG Telecom",
    "Pembelian SIM card wajib menunjukkan paspor",
    "Disarankan mengambil asuransi perjalanan yang mencakup evakuasi medis",
    "Biaya pengobatan menjadi tanggung jawab pribadi",
    "995",
    "Sultan Mosque dan beberapa masjid lain semuanya mendapat rating ⭐⭐⭐⭐⭐½",
    "Vintage Cameras, Army Museum of Singapore, Chinese Heritage, NUS Museum, dan lainnya dengan rating ⭐⭐⭐⭐⭐½",
    "McDonald's Marina mendapat rating ⭐⭐⭐⭐⭐½",
    "Bandara Changi",
    "Disarankan hadir 2 jam sebelum keberangkatan di Bandara Changi",
    "NUS Museum termasuk tempat wisata yang disebutkan",
    "Potensi gempa bumi dan polusi udara umum terjadi",
    "999",
    "Kedutaan Besar Republik Indonesia, 7 Chatsworth Road, Singapore 249761",
    "Kontak WhatsApp KBRI: +65 9648 0017 / +65 6737 7422 (Jam Kerja)",
    "Mengambil foto tanpa izin dilarang",
    "Mabuk di pesawat atau di ruang publik dilarang",
    "Simpan paspor dan dokumen penting dengan baik, segera lapor jika hilang",
    "Swensen's - ION mendapat rating ⭐⭐⭐⭐½",
    "Merokok dilarang di ruang AC dan zona larangan",

    # "Sistem hukum yang berlaku di Singapura adalah Common Law berbasis sistem Inggris",
    # "Bebas visa selama 30 hari sama dengan paspor reguler",
    # "Perpanjangan visa harus melalui ICA dengan dokumen lengkap dan alasan yang sah",
    # "Paspor berlaku minimal 6 bulan, tiket pulang, bukti keuangan dan akomodasi",
    # "Tergantung kebijakan terbaru, biasanya ada protokol karantina selama pandemi",
    # "Harus mendapatkan Employment Pass atau Work Permit melalui sponsor perusahaan",
    # "Kepemilikan dan penggunaan senjata api sangat dilarang, termasuk senjata tajam tertentu",
    # "Denda meliputi pelanggaran lalu lintas, merokok, buang sampah sembarangan, dan lainnya",
    # "Wajib membeli tiket sebelum naik dan patuhi aturan penumpang yang berlaku",
    # "Denda dan tilang berat diberlakukan termasuk untuk ngebut dan pelanggaran lampu merah",
    # "Minimal usia mengemudi 18 tahun untuk mobil dan 16 tahun untuk motor",
    # "Asuransi kesehatan perjalanan yang mencakup evakuasi medis dan perawatan rumah sakit disarankan",
    # "Wisatawan dapat mengklaim GST refund dengan bukti pembelian dan paspor",
    # "Narkotika dapat dikenai hukuman mati atau penjara seumur hidup, termasuk pengedaran",
    # "Laporkan ke polisi terdekat atau stasiun polisi bandara dengan dokumen lengkap",
    # "Hubungi polisi dan layanan ambulans, laporkan kepada pihak terkait dengan segera",
    # "Boleh dengan izin dan karantina sesuai regulasi hewan peliharaan",
    # "Pengiriman barang wajib melewati proses bea cukai dan pembatasan barang terlarang",
    # "Pengamanan ketat di area publik, pemeriksaan identitas dan barang bawaan",
    # "Penggunaan drone harus mendapat izin dan mengikuti aturan penerbangan",
    # "Penyebaran berita palsu dapat dikenai sanksi pidana berat",
    # "Segera ke rumah sakit atau klinik terdekat dan hubungi KBRI jika perlu",
    # "Kontak darurat KBRI Singapura: +65 9648 0017 / +65 6737 7422",
    # "Larangan berpakaian terbuka dan menampilkan atribut yang menyinggung agama/ras",
    # "WNA dibatasi dalam kepemilikan properti, khususnya untuk hunian pribadi dan komersial",
    # "Pajak utama adalah GST (Goods and Services Tax) sebesar 7%",
    # "Kebijakan daur ulang sangat ketat, limbah elektronik harus diserahkan ke pusat pengumpulan resmi",
    # "Parkir hanya diperbolehkan di area yang ditentukan dengan membayar tarif parkir",
    # "Batas kebisingan ketat diterapkan terutama di kawasan perumahan dan komersial",
    # "Dokumen seperti kontrak sewa dan identitas diri diperlukan saat menyewa tempat tinggal",
    # "WNA bisa membuka rekening dengan dokumen paspor dan bukti alamat",
    # "Aturan penggunaan masker tergantung kebijakan terbaru pandemi, biasanya wajib di ruang tertutup",
    # "Anak WNA bisa bersekolah di sekolah internasional atau pemerintah dengan izin tertentu",
    # "Penggunaan plastik sekali pakai sangat dibatasi dan didorong menggunakan alternatif ramah lingkungan",
    # "Pengaduan dapat dilakukan melalui website resmi pemerintah atau kantor layanan publik",
    # "Protokol meliputi penggunaan masker, jaga jarak, dan sanitasi tangan",
    # "Tidak ada aturan ketat, namun disarankan untuk tidak menggunakan WiFi publik untuk transaksi sensitif",
    # "Universal Studios, Singapore Zoo, dan Gardens by the Bay adalah wisata ramah keluarga",
    # "Restoran halal seperti Zam Zam, Hajah Maimunah, dan restoran Melayu lainnya sangat direkomendasikan",
    # "Toko biasanya buka dari 10 pagi sampai 10 malam, beberapa restoran buka sampai larut malam",
    # "Penggunaan ponsel saat mengemudi dilarang dan dapat dikenai denda besar",
    # "Sistem pengelolaan sampah berbasis 3R (Reduce, Reuse, Recycle) dan pengumpulan terjadwal",
    # "Tersedia fasilitas khusus, masjid, dan restoran halal bagi wisatawan muslim",
    # "WNA dapat mengakses rumah sakit swasta maupun publik dengan biaya pribadi atau asuransi",
    # "Ojek online diatur ketat dan harus mendapat lisensi resmi",
    # "Barang bawaan harus dilaporkan dan melewati pemeriksaan bea cukai sesuai batas bebas pajak",
    # "Hak cipta dan paten dilindungi secara ketat, pelanggaran dapat dipidana",
    # "Pelanggaran lingkungan seperti pembuangan limbah sembarangan dapat dikenai denda berat",
    # "Minum alkohol di tempat umum dilarang pada jam-jam tertentu (22:30-07:00)"
]



answers = []
contexts = []

for query in questions:
    # print(f"\n🟨 Query: {query}")
    output = rag_chain.invoke({
        "question": query,
        "chat_history": []
    })

    # Debug output
    # print("🔹 Raw output:", output)
    # print("🔹 Type of output:", type(output))

    # Ambil jawaban dari output
    try:
        if isinstance(output, dict):
            print("🔹 Keys:", output.keys())
            ans_text = output.get("answer") or output.get("response") or ""
        elif hasattr(output, "content"):
            ans_text = output.content
        else:
            ans_text = str(output)
    except Exception as e:
        print(f"❌ Error saat parsing output: {e}")
        ans_text = ""

    # print(f"✅ Jawaban: {ans_text}")
    answers.append(ans_text)

    # Ambil konteks
    docs = retriever.invoke(query)
    context_list = [doc.page_content for doc in docs]
    contexts.append(context_list)

# Cek apakah jawaban berhasil dikumpulkan
# print("\n📌 Isi answers sebelum dataset:", answers)

# Buat dataset untuk evaluasi
data = {
    "question": questions,
    "answer": answers,
    "contexts": contexts,
    "reference": ground_truths
}
dataset = Dataset.from_dict(data)

# Evaluasi RAG
result = evaluate(
    dataset=dataset,
    metrics=[
        context_precision,
        context_recall,
        faithfulness,
        answer_similarity,
        answer_correctness
    ],
)

# Simpan hasil evaluasi
df = result.to_pandas()
df["response"] = answers
# print("\n✅ DataFrame hasil evaluasi:\n", df.head())
df['response'] = df['response'].astype(str)

cleaned_answers = [ans.replace("\n\nNeoIntBot:", "").strip() for ans in answers]
df["response"] = cleaned_answers
df.to_csv("evaluation_results_1.csv", index=False)
print("📁 Evaluasi selesai, hasil disimpan di evaluation_results.csv")


