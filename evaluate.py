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


############################################ open ai #####################
# from datasets import Dataset
# import rag
# from ragas import evaluate
# from ragas.metrics import (
#     faithfulness,
#     answer_similarity,
#     context_recall,
#     context_precision,
#     answer_correctness
# )
# import csv
# import time

# # initialize chatbot
# rag.initialize_chatbot()

# # akses variabel dari namespace rag
# rag_chain = rag.rag_chain
# retriever = rag.retriever

# questions = [
#     "Apa bentuk pemerintahan Singapura?",
#     "Apa kode telepon untuk negara Singapura?",
#     "Apa Zona waktu Singapura? GMT berapa?",
#     "Di mana alamat KBRI di Singapura?",
#     "Berapa lama WNI bisa masuk di Singapura tanpa visa?",
#     "Berapa minimal masa berlaku paspor untuk masuk ke Singapura?",
#     "Apa kewajiban saat masuk atau keluar dari Singapura?",
#     "Disarankan hadir berapa jam sebelum keberangkatan jika ingin tiba di Bandara Changi?",
#     "Jenis soket apa yang digunakan di Singapura?",
#     "Apa nomor darurat untuk menghubungi polisi di Singapura?",
#     "Apa yang harus dilakukan jika kehilangan paspor di Singapura?",
#     "Apa alamat kantor imigrasi Singapura di Jakarta?",
#     "Berapa nomor telepon kantor imigrasi Singapura di Jakarta?",
#     "Apa saja potensi kriminalitas yang harus diwaspadai di Singapura?",
#     "Apa potensi terorisme di Singapura menurut informasi ini?",
#     "Apa musim monsoon di Singapura?",
#     "Apa hukuman untuk tindak pidana narkotika di Singapura?",
#     "Apakah WNI berhak mendapatkan notifikasi penahanan di Singapura?",
#     "Barang apa saja yang dilarang untuk diimpor ke Singapura?",
#     "Jam berapa konsumsi alkohol dilarang di area publik Singapura?",
#     "Apa larangan merokok di Singapura?",
#     "Apa larangan umum terkait perilaku di ruang publik Singapura?",
#     "Apakah permen karet dijual di Singapura?",
#     "Apakah wajib bayar cukai rokok di Singapura?",
#     "Apa larangan menyeberang jalan di Singapura?",
#     "Apa mata uang resmi yang digunakan di Singapura?",
#     "Di mana tempat penukaran uang yang banyak tersedia di Singapura?",
#     "Apa saja operator telekomunikasi di Singapura?",
#     "Apa persyaratan pembelian SIM card di Singapura?",
#     "Apa rekomendasi terkait asuransi untuk wisatawan ke Singapura?",
#     "Siapa yang bertanggung jawab atas biaya pengobatan di Singapura?",
#     "Apa nomor darurat ambulans di Singapura?",
#     "Apa nama masjid yang mendapat rating tertinggi di Singapura?",
#     "Sebutkan salah satu tempat wisata dengan rating bintang lima di Singapura!",
#     "Apa nama restoran cepat saji yang ada di Marina Singapura?",
#     "Apa nama bandara utama di Singapura?",
#     "Berapa lama waktu disarankan untuk hadir sebelum keberangkatan di bandara utama Singapura?",
#     "Apa nama museum yang termasuk dalam daftar tempat wisata di Singapura?",
#     "Sebutkan satu risiko bencana alam di Singapura!",
#     "Apa nomor darurat untuk menghubungi polisi di Singapura?",
#     "Apa alamat KBRI Singapura?",
#     "Apa kontak WhatsApp KBRI Singapura untuk jam kerja?",
#     "Apa larangan terkait pengambilan foto di Singapura?",
#     "Apa larangan terkait mabuk di ruang publik di Singapura?",
#     "Apa yang harus dilakukan untuk pengamanan dokumen penting di Singapura?",
#     "Sebutkan satu restoran dengan rating bintang empat di Singapura!",
#     "Apa larangan terkait merokok di ruang AC di Singapura?",

#     #  "Apa jenis sistem hukum yang berlaku di Singapura?",
#     # "Berapa lama durasi bebas visa bagi WNI di Singapura untuk paspor dinas dan diplomatik?",
#     # "Bagaimana prosedur perpanjangan visa di Singapura?",
#     # "Apa saja dokumen yang harus disiapkan saat masuk ke Singapura?",
#     # "Apakah Singapura menerapkan karantina wajib bagi pengunjung saat pandemi?",
#     # "Bagaimana prosedur pengajuan izin kerja bagi WNA di Singapura?",
#     # "Apa larangan terkait senjata api di Singapura?",
#     # "Apa saja jenis denda yang umum dikenakan di Singapura?",
#     # "Bagaimana aturan penggunaan transportasi umum di Singapura?",
#     # "Apa sanksi bagi pelanggaran aturan lalu lintas di Singapura?",
#     # "Apakah ada batasan usia minimal mengemudi di Singapura?",
#     # "Apa jenis asuransi kesehatan yang disarankan selama di Singapura?",
#     # "Apa kebijakan pengembalian pajak untuk wisatawan di Singapura?",
#     # "Apa larangan terkait narkotika yang harus diketahui di Singapura?",
#     # "Bagaimana prosedur pelaporan kehilangan barang di Singapura?",
#     # "Apa langkah yang harus dilakukan jika terjadi kecelakaan lalu lintas di Singapura?",
#     # "Apakah warga negara asing boleh membawa hewan peliharaan ke Singapura?",
#     # "Bagaimana aturan pengiriman barang dari luar ke Singapura?",
#     # "Apa protokol keamanan saat menghadiri acara publik di Singapura?",
#     # "Bagaimana aturan penggunaan drone di Singapura?",
#     # "Apa kebijakan Singapura terkait penyebaran berita hoax?",
#     # "Apa yang harus dilakukan jika mengalami sakit saat di Singapura?",
#     # "Bagaimana cara menghubungi KBRI Singapura dalam keadaan darurat?",
#     # "Apa larangan terkait pakaian dan penampilan di Singapura?",
#     # "Bagaimana aturan kepemilikan properti bagi WNA di Singapura?",
#     # "Apa jenis pajak yang berlaku di Singapura bagi penduduk dan wisatawan?",
#     # "Apa kebijakan Singapura terhadap limbah elektronik dan daur ulang?",
#     # "Bagaimana aturan parkir kendaraan di Singapura?",
#     # "Apakah Singapura memiliki aturan ketat terhadap kebisingan?",
#     # "Apa jenis dokumen yang diperlukan untuk menyewa tempat tinggal di Singapura?",
#     # "Bagaimana cara membuka rekening bank bagi WNA di Singapura?",
#     # "Apa aturan terkait penggunaan masker di ruang publik Singapura saat pandemi?",
#     # "Bagaimana sistem pendidikan bagi anak WNA yang tinggal di Singapura?",
#     # "Apa larangan terkait penggunaan plastik sekali pakai di Singapura?",
#     # "Bagaimana prosedur pengaduan terhadap layanan publik di Singapura?",
#     # "Apa protokol kesehatan saat menggunakan transportasi umum di Singapura?",
#     # "Apakah ada aturan khusus terkait penggunaan WiFi publik di Singapura?",
#     # "Apa saja tempat wisata ramah keluarga di Singapura?",
#     # "Apa rekomendasi kuliner halal di Singapura?",
#     # "Bagaimana aturan mengenai jam operasional toko dan restoran di Singapura?",
#     # "Apa larangan terkait penggunaan ponsel saat mengemudi di Singapura?",
#     # "Bagaimana sistem pengelolaan sampah di Singapura?",
#     # "Apakah ada aturan khusus untuk wisatawan muslim di Singapura?",
#     # "Apa saja fasilitas kesehatan yang dapat diakses oleh WNA di Singapura?",
#     # "Bagaimana aturan terkait pengoperasian ojek online di Singapura?",
#     # "Apa prosedur bea cukai barang bawaan saat tiba di Singapura?",
#     # "Bagaimana kebijakan Singapura terhadap hak cipta dan paten?",
#     # "Apa tindakan yang diambil oleh pemerintah Singapura terhadap pelanggaran lingkungan?",
#     # "Apa aturan tentang pemakaian alkohol di tempat umum di Singapura?"
# ]

# ground_truths = [
#     "Bentuk pemerintahan Singapura yaitu Republik Parlementer Unikameral",
#     "Kode telepon negara Singapura yaitu +65",
#     "Zona waktu Singapura adalah GMT+8 (1 jam lebih cepat dari Jakarta)",
#     "Kedutaan Besar Republik Indonesia, 7 Chatsworth Road, Singapore 249761",
#     "WNI bisa masuk tanpa Visa selama 30 hari untuk paspor reguler, dinas, dan diplomatik",
#     "Syarat masa berlaku paspor minimal 6 bulan",
#     "Kewajiban saat masuk/keluar Singapura adalah pemindaian sidik jari ",
#     "Disarankan kita hadir 2 jam sebelum keberangkatan di Bandara Changi",
#     "Jenis soket di Singapura adalah soket tipe G",
#     "Nomor darurat untuk menghubungi polisi adalah 999",
#     "Simpan paspor dan dokumen penting, segera lapor ke KBRI jika hilang",
#     "Jl. H.R Rasuna Said Blok X4 Kav. 2, Kuningan, Jakarta 12950",
#     "+62 21 2995 0400",
#     "Waspadai penipuan properti dan hindari transaksi tunai dalam jumlah besar",
#     "Potensi kecil, tetap waspada di hotel, klub malam, bar, pasar, stasiun kereta, dan tempat ibadah",
#     "Musim Monsoon: Desember-Maret dan Juni-September",
#     "Narkotika dapat dihukum mati",
#     "Ya, WNI berhak meminta notifikasi ke KBRI jika ditahan",
#     "Mengimpor barang bajakan dan rokok elektrik dilarang",
#     "Konsumsi alkohol dilarang pukul 22:30 sampai 07:00 di area publik",
#     "Merokok dilarang di ruang publik, AC, dan zona larangan",
#     "Dilarang membuang sampah sembarangan, meludah, graffiti, dan mengambil foto tanpa izin",
#     "Permen karet tidak dijual di Singapura",
#     "Wajib bayar cukai rokok; hindari merokok tanpa cukai",
#     "Dilarang menyeberang jalan sembarangan",
#     "Dollar Singapura (SGD)",
#     "Money changer banyak tersedia di area wisata",
#     "Operator telekomunikasi utama adalah Singtel, M1, StarHub, Circles.Life, dan TPG Telecom",
#     "Pembelian SIM card wajib menunjukkan paspor",
#     "Disarankan mengambil asuransi perjalanan yang mencakup evakuasi medis",
#     "Biaya pengobatan menjadi tanggung jawab pribadi",
#     "995",
#     "Sultan Mosque dan beberapa masjid lain semuanya mendapat rating ⭐⭐⭐⭐⭐½",
#     "Vintage Cameras, Army Museum of Singapore, Chinese Heritage, NUS Museum, dan lainnya dengan rating ⭐⭐⭐⭐⭐½",
#     "McDonald's Marina mendapat rating ⭐⭐⭐⭐⭐½",
#     "Bandara Changi",
#     "Disarankan hadir 2 jam sebelum keberangkatan di Bandara Changi",
#     "NUS Museum termasuk tempat wisata yang disebutkan",
#     "Potensi gempa bumi dan polusi udara umum terjadi",
#     "999",
#     "Kedutaan Besar Republik Indonesia, 7 Chatsworth Road, Singapore 249761",
#     "Kontak WhatsApp KBRI: +65 9648 0017 / +65 6737 7422 (Jam Kerja)",
#     "Mengambil foto tanpa izin dilarang",
#     "Mabuk di pesawat atau di ruang publik dilarang",
#     "Simpan paspor dan dokumen penting dengan baik, segera lapor jika hilang",
#     "Swensen's - ION mendapat rating ⭐⭐⭐⭐½",
#     "Merokok dilarang di ruang AC dan zona larangan",

#     # "Sistem hukum yang berlaku di Singapura adalah Common Law berbasis sistem Inggris",
#     # "Bebas visa selama 30 hari sama dengan paspor reguler",
#     # "Perpanjangan visa harus melalui ICA dengan dokumen lengkap dan alasan yang sah",
#     # "Paspor berlaku minimal 6 bulan, tiket pulang, bukti keuangan dan akomodasi",
#     # "Tergantung kebijakan terbaru, biasanya ada protokol karantina selama pandemi",
#     # "Harus mendapatkan Employment Pass atau Work Permit melalui sponsor perusahaan",
#     # "Kepemilikan dan penggunaan senjata api sangat dilarang, termasuk senjata tajam tertentu",
#     # "Denda meliputi pelanggaran lalu lintas, merokok, buang sampah sembarangan, dan lainnya",
#     # "Wajib membeli tiket sebelum naik dan patuhi aturan penumpang yang berlaku",
#     # "Denda dan tilang berat diberlakukan termasuk untuk ngebut dan pelanggaran lampu merah",
#     # "Minimal usia mengemudi 18 tahun untuk mobil dan 16 tahun untuk motor",
#     # "Asuransi kesehatan perjalanan yang mencakup evakuasi medis dan perawatan rumah sakit disarankan",
#     # "Wisatawan dapat mengklaim GST refund dengan bukti pembelian dan paspor",
#     # "Narkotika dapat dikenai hukuman mati atau penjara seumur hidup, termasuk pengedaran",
#     # "Laporkan ke polisi terdekat atau stasiun polisi bandara dengan dokumen lengkap",
#     # "Hubungi polisi dan layanan ambulans, laporkan kepada pihak terkait dengan segera",
#     # "Boleh dengan izin dan karantina sesuai regulasi hewan peliharaan",
#     # "Pengiriman barang wajib melewati proses bea cukai dan pembatasan barang terlarang",
#     # "Pengamanan ketat di area publik, pemeriksaan identitas dan barang bawaan",
#     # "Penggunaan drone harus mendapat izin dan mengikuti aturan penerbangan",
#     # "Penyebaran berita palsu dapat dikenai sanksi pidana berat",
#     # "Segera ke rumah sakit atau klinik terdekat dan hubungi KBRI jika perlu",
#     # "Kontak darurat KBRI Singapura: +65 9648 0017 / +65 6737 7422",
#     # "Larangan berpakaian terbuka dan menampilkan atribut yang menyinggung agama/ras",
#     # "WNA dibatasi dalam kepemilikan properti, khususnya untuk hunian pribadi dan komersial",
#     # "Pajak utama adalah GST (Goods and Services Tax) sebesar 7%",
#     # "Kebijakan daur ulang sangat ketat, limbah elektronik harus diserahkan ke pusat pengumpulan resmi",
#     # "Parkir hanya diperbolehkan di area yang ditentukan dengan membayar tarif parkir",
#     # "Batas kebisingan ketat diterapkan terutama di kawasan perumahan dan komersial",
#     # "Dokumen seperti kontrak sewa dan identitas diri diperlukan saat menyewa tempat tinggal",
#     # "WNA bisa membuka rekening dengan dokumen paspor dan bukti alamat",
#     # "Aturan penggunaan masker tergantung kebijakan terbaru pandemi, biasanya wajib di ruang tertutup",
#     # "Anak WNA bisa bersekolah di sekolah internasional atau pemerintah dengan izin tertentu",
#     # "Penggunaan plastik sekali pakai sangat dibatasi dan didorong menggunakan alternatif ramah lingkungan",
#     # "Pengaduan dapat dilakukan melalui website resmi pemerintah atau kantor layanan publik",
#     # "Protokol meliputi penggunaan masker, jaga jarak, dan sanitasi tangan",
#     # "Tidak ada aturan ketat, namun disarankan untuk tidak menggunakan WiFi publik untuk transaksi sensitif",
#     # "Universal Studios, Singapore Zoo, dan Gardens by the Bay adalah wisata ramah keluarga",
#     # "Restoran halal seperti Zam Zam, Hajah Maimunah, dan restoran Melayu lainnya sangat direkomendasikan",
#     # "Toko biasanya buka dari 10 pagi sampai 10 malam, beberapa restoran buka sampai larut malam",
#     # "Penggunaan ponsel saat mengemudi dilarang dan dapat dikenai denda besar",
#     # "Sistem pengelolaan sampah berbasis 3R (Reduce, Reuse, Recycle) dan pengumpulan terjadwal",
#     # "Tersedia fasilitas khusus, masjid, dan restoran halal bagi wisatawan muslim",
#     # "WNA dapat mengakses rumah sakit swasta maupun publik dengan biaya pribadi atau asuransi",
#     # "Ojek online diatur ketat dan harus mendapat lisensi resmi",
#     # "Barang bawaan harus dilaporkan dan melewati pemeriksaan bea cukai sesuai batas bebas pajak",
#     # "Hak cipta dan paten dilindungi secara ketat, pelanggaran dapat dipidana",
#     # "Pelanggaran lingkungan seperti pembuangan limbah sembarangan dapat dikenai denda berat",
#     # "Minum alkohol di tempat umum dilarang pada jam-jam tertentu (22:30-07:00)"
# ]



# answers = []
# contexts = []

# for query in questions:
#     # print(f"\n🟨 Query: {query}")
#     output = rag_chain.invoke({
#         "question": query,
#         "chat_history": []
#     })

#     # Debug output
#     # print("🔹 Raw output:", output)
#     # print("🔹 Type of output:", type(output))

#     # Ambil jawaban dari output
#     try:
#         if isinstance(output, dict):
#             print("🔹 Keys:", output.keys())
#             ans_text = output.get("answer") or output.get("response") or ""
#         elif hasattr(output, "content"):
#             ans_text = output.content
#         else:
#             ans_text = str(output)
#     except Exception as e:
#         print(f"❌ Error saat parsing output: {e}")
#         ans_text = ""

#     # print(f"✅ Jawaban: {ans_text}")
#     answers.append(ans_text)

#     # Ambil konteks
#     docs = retriever.invoke(query)
#     context_list = [doc.page_content for doc in docs]
#     contexts.append(context_list)

# # Cek apakah jawaban berhasil dikumpulkan
# # print("\n📌 Isi answers sebelum dataset:", answers)

# # Buat dataset untuk evaluasi
# data = {
#     "question": questions,
#     "answer": answers,
#     "contexts": contexts,
#     "reference": ground_truths
# }
# dataset = Dataset.from_dict(data)

# # Evaluasi RAG
# result = evaluate(
#     dataset=dataset,
#     metrics=[
#         context_precision,
#         context_recall,
#         faithfulness,
#         answer_similarity,
#         answer_correctness
#     ],
# )

# # Simpan hasil evaluasi
# df = result.to_pandas()
# df["response"] = answers
# # print("\n✅ DataFrame hasil evaluasi:\n", df.head())
# df['response'] = df['response'].astype(str)

# cleaned_answers = [ans.replace("\n\nNeoIntBot:", "").strip() for ans in answers]
# df["response"] = cleaned_answers
# df.to_csv("evaluation/evaluation_results_gemini.csv", index=False)
# # df.to_csv("evaluation_results_openai.csv", index=False)
# print("📁 Evaluasi selesai, hasil disimpan di evaluation_results.csv")

###################################### gemini ################################
from datasets import Dataset
import rag
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    context_recall,
    context_precision,
    AnswerRelevancy,
    answer_correctness
)
import csv
import time
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.llms import LangchainLLMWrapper
import asyncio

# initialize chatbot
rag.initialize_chatbot()

# akses variabel dari namespace rag
rag_chain = rag.rag_chain
retriever = rag.retriever

questions = [
    # "Apa bentuk pemerintahan Singapura?",
    # "Apa kode telepon untuk negara Singapura?",
    # "Apa Zona waktu Singapura? GMT berapa?",
    # "Di mana alamat KBRI di Singapura?",
    # "Berapa lama WNI bisa masuk di Singapura tanpa visa?",
    # "Berapa minimal masa berlaku paspor untuk masuk ke Singapura?",
    # "Apa kewajiban saat masuk atau keluar dari Singapura?",
    # "Disarankan hadir berapa jam sebelum keberangkatan jika ingin tiba di Bandara Changi?",
    # "Jenis soket apa yang digunakan di Singapura?",
    # "Apa nomor darurat untuk menghubungi polisi di Singapura?",
    # "Apa yang harus dilakukan jika kehilangan paspor di Singapura?",
    # "Apa alamat kantor imigrasi Singapura di Jakarta?",
    # "Berapa nomor telepon kantor imigrasi Singapura di Jakarta?",
    # "Apa saja potensi kriminalitas yang harus diwaspadai di Singapura?",
    # "Apa potensi terorisme di Singapura menurut informasi ini?",
    # "Apa musim monsoon di Singapura?",
    # "Apa hukuman untuk tindak pidana narkotika di Singapura?",
    # "Apakah WNI berhak mendapatkan notifikasi penahanan di Singapura?",
    # "Barang apa saja yang dilarang untuk diimpor ke Singapura?",
    # "Jam berapa konsumsi alkohol dilarang di area publik Singapura?",
    # "Apa larangan merokok di Singapura?",
    # "Apa larangan umum terkait perilaku di ruang publik Singapura?",
    # "Apakah permen karet dijual di Singapura?",
    # "Apakah wajib bayar cukai rokok di Singapura?",
    # "Apa larangan menyeberang jalan di Singapura?",
    # "Apa mata uang resmi yang digunakan di Singapura?",
    # "Di mana tempat penukaran uang yang banyak tersedia di Singapura?",
    # "Apa saja operator telekomunikasi di Singapura?",
    # "Apa persyaratan pembelian SIM card di Singapura?",
    # "Apa rekomendasi terkait asuransi untuk wisatawan ke Singapura?",
    # "Siapa yang bertanggung jawab atas biaya pengobatan di Singapura?",
    # "Apa nomor darurat ambulans di Singapura?",
    # "Apa nama masjid yang mendapat rating tertinggi di Singapura?",
    # "Sebutkan salah satu tempat wisata dengan rating bintang lima di Singapura!",
    # "Apa nama restoran cepat saji yang ada di Marina Singapura?",
    # "Apa nama bandara utama di Singapura?",
    # "Berapa lama waktu disarankan untuk hadir sebelum keberangkatan di bandara utama Singapura?",
    # "Apa nama museum yang termasuk dalam daftar tempat wisata di Singapura?",
    # "Sebutkan satu risiko bencana alam di Singapura!",
    # "Apa nomor darurat untuk menghubungi polisi di Singapura?",
    # "Apa alamat KBRI Singapura?",
    # "Apa kontak WhatsApp KBRI Singapura untuk jam kerja?",
    # "Apa larangan terkait pengambilan foto di Singapura?",
    # "Apa larangan terkait mabuk di ruang publik di Singapura?",
    # "Apa yang harus dilakukan untuk pengamanan dokumen penting di Singapura?",
    # "Sebutkan satu restoran dengan rating bintang empat di Singapura!",
    # "Apa larangan terkait merokok di ruang AC di Singapura?",

    #80 question about self report

    # "Apa nama portal yang digunakan WNI untuk lapor diri di luar negeri?",
    # "Siapa yang mengelola portal pelayanan dan pelindungan WNI di luar negeri?",
    # "Apa saja menu utama dalam Portal Pelayanan dan Pelindungan WNI?",
    # "Apa fungsi dari menu Lapor Diri di portal?",
    # "Apa fungsi dari menu Pelindungan di portal?",
    # "Apa saja jenis laporan dalam fitur Lapor Diri?",
    # "Apa saja syarat awal untuk mengakses portal?",
    # "Bagaimana cara login ke dalam portal WNI?",
    # "Apa yang harus dilakukan jika belum punya akun di portal?",
    # "Bagaimana proses konfirmasi email setelah registrasi?",

    # ========================== fix ==========================
    # "Bagaimana sistem memverifikasi nomor KTKLN?",
    # "Kapan halaman input KTKLN akan ditampilkan?",
    #  # 1. Deskripsi singkat aplikasi
    # "Apa deskripsi singkat dari Portal Pelayanan dan Pelindungan WNI di Luar Negeri?",

    # # 2. Deskripsi user
    # "Apa saja hak akses user WNI terhadap aplikasi.",

    # # 3. Langkah awal penggunaan aplikasi
    # "Apa langkah awal untuk menggunakan aplikasi Portal Pelayanan dan Pelindungan WNI di Luar Negeri terutama dari link alamat aplikasi",

    # # 4. Fungsi-fungsi menu (10 soal)
    # "Apa fungsi dari menu Beranda di Portal Pelayanan dan Pelindungan WNI?",
    # "Apa fungsi dari menu Lapor Diri?",
    # "Apa fungsi dari menu Pelindungan?",
    # "Apa fungsi dari menu Pengaduan Layanan?",
    # "Apa fungsi dari menu Pelayanan?",
    # "Apa fungsi dari menu Informasi Pelayanan?",
    # "Apa fungsi dari menu Pengumuman?",
    # "Apa fungsi dari menu Referensi?",
    # "Apa fungsi dari menu FAQ?",
    # "Apa fungsi dari menu Profil WNI?",

    # # 5. Akses fitur-fitur dalam portal
    # "Apa yang harus dilakukan user agar dapat mengakses fitur-fitur dalam Portal Pelayanan dan Pelindungan WNI?",

    # # 6. Jika sudah memiliki akun
    # "Jika user sudah memiliki akun di Portal Pelayanan dan Pelindungan WNI, apa yang harus dilakukan sesuai dengan standar keamanan?",

    # # 7. Jika belum memiliki akun
    # "Apa yang harus dilakukan jika user belum memiliki akun di Portal Pelayanan dan Pelindungan WNI di Luar Negeri?",

    # # 8. Setelah mengisi form pendaftaran
    # "Apa yang harus dilakukan user setelah selesai mengisi semua kolom pada form pendaftaran akun portal?",

    # # 9. UU No. 23 Tahun 2006 (2 soal)
    # "Menurut Undang-undang No.23 Tahun 2006, hal-hal apa saja yang wajib dilaporkan oleh WNI yang berada di luar negeri?",
    # "Apa tujuan sistem menyediakan fitur lapor diri dalam portal sesuai dengan Pasal 4 UU No. 23 Tahun 2006?",

    # # 10. Jenis-jenis lapor diri
    # "Apa saja 4 jenis lapor diri yang tersedia dalam Portal Pelayanan dan Pelindungan WNI di Luar Negeri?",

    # "Jelaskan langkah pertama bagi WNI yang belum pernah melapor diri di perwakilan?",
    # "Apa yang dilakukan jika user tidak memiliki NIK valid?",
    # "Apa halaman yang ditampilkan setelah memasukkan nomor paspor yang valid?",

    # # 2. Kedatangan – Sudah Pernah Lapor Diri
    # "Apa yang user harus lakuakan jika sudah pernah pernah melakukan lapor diri dengan didaftarkan oleh Perwakilan (tidak secara mandiri) menggunakan Portal Pelayanan dan Pelindungan WNI?",
    # "Apa yang harus dilakukan jika nomor registrasi tidak valid saat user yang pernah lapor diri melakukan memasukkan nomor registrasi lapor diri ?",
    # "Apa langkah yang harus dilakukan jika user lupa nomor registrasi lapor diri?",
    # "Apa hasil yang muncul jika data registrasi yang dimasukkan valid dan cocok?",

    # # 3. II.2.2 Perpindahan
    # "Apa syarat agar WNI bisa melakukan lapor diri perpindahan di luar negeri?",
    # "Apa saja data yang harus diisi saat lapor diri perpindahan?",
    # "Jelaskan langkah-langkah yang harus dilakukan jika ingin melakukan lapor diri perpindahan WNI secara langkap",

    # # 4. II.2.3 Kepulangan
    # "Apa fungsi dari fitur Kepulangan pada Portal Pelayanan WNI?",
    # "Jelaskan langkah-langkah menggunakan fitur kepulangan secara lengkap",

    # # 5. II.2.4 Keluarga
    # "Apa fungsi fitur keluarga di menu Lapor Diri pada portal Pelayanan WNI?",
    # "Bagaimana cara menambahkan anggota keluarga dalam fitur lapor diri?",

    # # 6. II.3 Menu Pelindungan
    # "Dalam kondisi apa menu Pelindungan digunakan oleh WNI?",
    # "Apa saja fitur utama yang tersedia di dalam menu Pelindungan?",

    # # 7. II.3.1 Buat Permohonan Pelindungan
    # "Apa langkah awal dalam membuat permohonan pelindungan?",
    # "Apa yang harus diisi dalam form identitas saat membuat permohonan pelindungan?",

    # # 8. II.3.2 Cek Status Permohonan Pelindungan
    # "Untuk apa user dapat melakukan pengecekan status permohonan yang telah dibuat",
    # "Apa kegunaan dari nomor permohonan pelindungan?",
    # "Bagaimana cara user mengecek status permohonan pelindungan yang telah dibuat?",

    # # 9. II.4 Menu Pelayanan
    # "Apa yang ditampilkan dalam menu pelayanan?",
    # "Apa yang terjadi setelah user mengisi form pelayanan dan mengirimkannya?",

    # # 10. Menu Informasi Pelayanan
    # "Apa informasi yang ditampilkan dalam menu Informasi Pelayanan?",
    # "Apa saja yang bisa dilihat user terkait perwakilan dalam menu Informasi Pelayanan?",

    # # 11. II.5.1 Lihat Detail
    # "Apa langkah pertama untuk melihat detail informasi pelayanan suatu negara?",
    # "Apa yang ditampilkan ketika user memilih salah satu perwakilan di negara tersebut?",
    # "Apa saja informasi yang disediakan pada halaman detail perwakilan?",

    # # 12. II.5.2 Pencarian Informasi Pelayanan
    # "Bagaimana cara melakukan pencarian informasi pelayanan berdasarkan negara?",

    # # 13. II.6 Menu Pengumuman
    # "Bagaimana cara mengakases menu Pengumuman?",

    # # 14. II.6.1 Lihat Detail
    # "Bagaimana cara melihat detail dari pengumuman yang tersedia di portal?",

    # 15. II.6.2 Pencarian Data Pengumuman
    "Bagaimana cara user melakukan pencarian pengumuman di Portal Pelayanan WNI?",

    # 16. II.7 Menu Referensi
    "Apa fungsi dari menu Referensi dalam Portal Pelayanan dan Pelindungan WNI?",
    "Bagaimana cara mengakses referensi hukum dalam portal tersebut?",

    # 17. II.8 Profil WNI
    "Apa syarat agar WNI dapat melihat dan mengubah data profilnya di portal WNI?",

    # 18. II.8.1 Lihat Detail
    "Apa saja informasi yang dapat dilihat oleh user pada bagian Lihat Detail dalam Profil WNI?",

    # # 19. II.8.1.1 Identitas
    # "Informasi apa saja yang ditampilkan pada tab Identitas dalam halaman Profil WNI?",

    # # 20. II.8.1.1.1 Ubah Profil
    # "Bagaimana langkah user untuk mengubah data identitas pada halaman Profil?",
    # "Apa dampak perubahan paspor, visa serta Negara, Provinsi dan Kota pada wilayah akreditasi perwakilan yang berbeda ?",

    # # 21. II.8.1.2 Riwayat Lapor Diri
    # "Apa informasi yang ditampilkan dalam fitur Riwayat Lapor Diri di Profil WNI?",

    # # 22. II.8.1.3 Riwayat Pelayanan
    # "Apa isi informasi yang disediakan dalam fitur Riwayat Pelayanan?",

    # # 23. II.8.1.4 Riwayat Pengaduan
    # "Apa saja yang ditampilkan dalam fitur Riwayat Pengaduan pada Profil WNI?",

    # # 24. (tambahan detail) II.8.1.4 Riwayat Pengaduan
    # "Apa kategori data yang tersedia dalam daftar pengaduan pada Riwayat Pengaduan?",

    # # 25. II.8.1.5 Riwayat Dokumen
    # "Apa yang ditampilkan kepada user di laman Riwayat Dokumen?",

    # # 26. II.9.1 Ubah Password
    # "Bagaimana cara user mengubah password melalui menu Profil di Portal Pelayanan WNI?",

    # # 27. II.9.2 Keluar Aplikasi
    # "Bagaimana cara user keluar dari aplikasi Portal Pelayanan dan Pelindungan WNI?",
    
    # "Bagian mana dalam aplikasi yang menampilkan riwayat pengaduan WNI?",
    # "Jika WNI ingin mengubah kata sandi akun mereka di Portal Pelayanan dan Perlindungan WNI, bagaimana caranya?",
    # "Setelah mengisikan kata sandi lama dan mengubah password baru, tombol apa yang harus diklik WNI?",
    # "Bagaimana cara WNI keluar dari aplikasi Portal Pelayanan dan Perlindungan WNI?",
    # "Apa yang terjadi setelah WNI mengklik tombol 'Keluar Aplikasi'?",
    # "Di mana lokasi tombol 'Keluar Aplikasi' atau 'Ubah Password' dapat ditemukan dalam antarmuka pengguna?",
    # "Ketika WNI sudah pernah lapor diri sebelumnya, bagaimana proses pelaporan kedatangan mereka di Portal Pelayanan dan Perlindungan WNI?",
    # "Apa perbedaan utama dalam proses lapor diri antara WNI yang sudah pernah lapor diri dan yang belum pernah?",
    # "Jika WNI ingin melaporkan perpindahan domisili, menu apa yang harus diakses?",
    # "Informasi apa saja yang diperlukan saat WNI melaporkan perpindahan di sistem?",
    # "Bagaimana cara WNI melaporkan kepulangan mereka ke Indonesia melalui Portal Pelayanan dan Perlindungan WNI?",
    # "Apa saja dokumen yang perlu disiapkan saat melaporkan kepulangan?",
    # "Di bagian mana WNI dapat melihat dokumen-dokumen yang telah mereka unggah sebelumnya?",
    # "Apa fungsi dari menu 'Keluarga' dalam aplikasi Portal Pelayanan dan Perlindungan WNI?",
    # "Informasi apa saja yang dapat dikelola dalam menu 'Keluarga'?",
    # "Bagaimana WNI dapat menambahkan anggota keluarga baru ke dalam akun mereka?",
    # "Jika WNI ingin mengajukan permohonan perlindungan, menu apa yang harus mereka pilih?",
    # "Apa saja jenis pengaduan yang dapat diajukan melalui fitur perlindungan?",

    # "Setelah mengajukan pengaduan, bagaimana WNI dapat memeriksa status pengaduan mereka?",
    # "Bagaimana tampilan halaman riwayat pengaduan di Portal Pelayanan dan Perlindungan WNI?",
    # "Informasi apa saja yang termuat dalam riwayat pengaduan?",
    # "Apa yang dimaksud dengan 'Deskripsi Singkat Aplikasi' dalam konteks panduan ini?",
    # "Siapa target pengguna dari aplikasi Portal Pelayanan dan Perlindungan WNI ini?",
    # "Apa langkah awal yang harus dilakukan pengguna sebelum mulai menggunakan aplikasi ini?",
    # "Di mana pengguna dapat menemukan daftar isi panduan?",
    # "Apa saja fungsi menu utama yang tersedia di aplikasi?",
    # "Bagaimana cara mengakses menu Beranda?",
    # "Apa saja informasi yang ditampilkan pada halaman Beranda?",
    # "Jika WNI belum memiliki akun, apa yang harus mereka lakukan untuk memulai proses lapor diri?",
    # "Pada tahap pendaftaran akun, informasi pribadi apa saja yang wajib diisi?",
    # "Bagaimana sistem mengkonfirmasi keberhasilan pendaftaran akun?",
    # "Setelah berhasil mendaftar, apa langkah selanjutnya bagi WNI untuk lapor diri?",
    # "Apakah ada batas waktu untuk melengkapi proses lapor diri setelah pendaftaran?",
    # "Jika WNI lupa kata sandi, apakah ada fitur pemulihan kata sandi?",
    # "Apa yang harus dilakukan jika WNI ingin membatalkan perubahan kata sandi?",
    # "Apakah ada opsi untuk mengelola informasi profil pribadi WNI di aplikasi?",
    # "Bagaimana cara WNI memperbarui data profil mereka?",
    # "Apakah WNI dapat mengunggah lebih dari satu dokumen pada satu waktu?",
    # "Apa jenis file yang diizinkan untuk diunggah sebagai dokumen pendukung?",
    # "Bagaimana proses validasi data setelah WNI mengisi formulir lapor diri?",
    # "Apa yang terjadi jika ada informasi yang tidak valid saat pengisian formulir?",
    # "Apakah ada notifikasi yang diberikan kepada WNI setelah proses lapor diri selesai?",
    # "Bagaimana cara WNI melihat rincian lapor diri yang telah mereka ajukan?",
    # "Jika WNI ingin mengedit informasi lapor diri yang sudah terkirim, apakah itu mungkin?",
    # "Apa yang dimaksud dengan 'status pengaduan' dalam riwayat pengaduan?",
    # "Siapa yang bertanggung jawab untuk memproses pengaduan yang diajukan WNI?",
    # "Apakah aplikasi ini mendukung akses dari perangkat seluler?",
    # "Apa tujuan utama dari Portal Pelayanan dan Perlindungan WNI di luar negeri?",
    # "Bagaimana cara kerja fitur 'preview dokumen'?",
    # "Bisakah WNI mengunduh dokumen yang telah mereka unggah dari sistem?",
    # "Apakah ada batasan ukuran file untuk dokumen yang diunggah?",
    # "Bagaimana sistem memastikan keamanan data pribadi WNI?",
    # "Apa yang dimaksud dengan 'Perwakilan' dalam konteks pengaduan?",
    # "Jika WNI memiliki pertanyaan tentang penggunaan aplikasi, di mana mereka dapat mencari bantuan?",
    # "Apakah aplikasi ini menyediakan fitur bantuan atau FAQ?",
    # "Bagaimana cara mengidentifikasi WNI yang sudah pernah lapor diri di sistem?",
    # "Apa keuntungan menggunakan Portal Pelayanan dan Perlindungan WNI dibandingkan metode lapor diri manual?",
    # "Bagaimana proses verifikasi identitas WNI saat pendaftaran akun?",
    # "Apakah ada persyaratan usia minimum untuk menggunakan aplikasi ini?",
    # "Jika WNI mengalami masalah teknis saat menggunakan aplikasi, siapa yang harus dihubungi?",
    # "Apakah data yang diunggah WNI disimpan secara permanen di sistem?",
    # "Bagaimana aplikasi ini mendukung perlindungan WNI yang berada dalam situasi darurat?",
    # "Apakah ada integrasi dengan layanan darurat lokal di negara tempat WNI berada?",
    # "Bagaimana aplikasi ini memastikan bahwa informasi yang diberikan WNI akurat?",
    # "Apakah WNI akan menerima pemberitahuan mengenai status permohonan atau pengaduan mereka?",
    # "Apa perbedaan antara 'Kedatangan - Belum Pernah Lapor Diri' dan 'Kedatangan - Sudah Pernah Lapor Diri'?",
    # "Bagaimana WNI dapat mengedit data keluarga yang sudah ada di sistem?",
    # "Apakah aplikasi ini menyediakan fitur untuk mencetak bukti lapor diri?",
    # "Bagaimana prosedur pelaporan jika WNI ingin membatalkan pendaftaran lapor diri?",
    # "Apa saja langkah yang perlu diambil untuk melaporkan 'Kepulangan'?",
    # "Dalam konteks 'Riwayat Dokumen', apa yang dapat dilihat oleh pengguna?",
    # "Jika WNI perlu mengubah informasi penting seperti nomor paspor setelah lapor diri, bagaimana prosedurnya?",
    # "Apakah aplikasi ini memungkinkan pengajuan pengaduan anonim?",
    # "Bagaimana sistem membedakan antara 'jenis pengaduan' dan 'kategori kasus'?",
    # "Apakah ada panduan visual atau video tutorial yang tersedia untuk penggunaan aplikasi?",
    # "Berapa jumlah maksimal anggota keluarga yang dapat ditambahkan ke dalam satu akun?",
    # "Bagaimana Portal Pelayanan dan Perlindungan WNI memfasilitasi komunikasi antara WNI dan Perwakilan?",
    # "Apa yang dimaksud dengan 'Halaman Publik' dalam konteks 'Keluar Aplikasi'?",
    # "Apa saja informasi yang harus dipastikan benar oleh WNI sebelum klik 'Simpan' pada formulir?",
    # "Bagaimana WNI dapat memastikan bahwa data yang mereka masukkan aman?",
    # "Apakah ada fitur peringatan atau notifikasi untuk perpanjangan masa lapor diri?"
]

ground_truths = [
    
    # "Bentuk pemerintahan Singapura yaitu Republik Parlementer Unikameral",
    # "Kode telepon negara Singapura yaitu +65",
    # "Zona waktu Singapura adalah GMT+8 (1 jam lebih cepat dari Jakarta)",
    # "Kedutaan Besar Republik Indonesia, 7 Chatsworth Road, Singapore 249761",
    # "WNI bisa masuk tanpa Visa selama 30 hari untuk paspor reguler, dinas, dan diplomatik",
    # "Syarat masa berlaku paspor minimal 6 bulan",
    # "Kewajiban saat masuk/keluar Singapura adalah pemindaian sidik jari ",
    # "Disarankan kita hadir 2 jam sebelum keberangkatan di Bandara Changi",
    # "Jenis soket di Singapura adalah soket tipe G",
    # "Nomor darurat untuk menghubungi polisi adalah 999",
    # "Simpan paspor dan dokumen penting, segera lapor ke KBRI jika hilang",
    # "Jl. H.R Rasuna Said Blok X4 Kav. 2, Kuningan, Jakarta 12950",
    # "+62 21 2995 0400",
    # "Waspadai penipuan properti dan hindari transaksi tunai dalam jumlah besar",
    # "Potensi kecil, tetap waspada di hotel, klub malam, bar, pasar, stasiun kereta, dan tempat ibadah",
    # "Musim Monsoon: Desember-Maret dan Juni-September",
    # "Narkotika dapat dihukum mati",
    # "Ya, WNI berhak meminta notifikasi ke KBRI jika ditahan",
    # "Mengimpor barang bajakan dan rokok elektrik dilarang",
    # "Konsumsi alkohol dilarang pukul 22:30 sampai 07:00 di area publik",
    # "Merokok dilarang di ruang publik, AC, dan zona larangan",
    # "Dilarang membuang sampah sembarangan, meludah, graffiti, dan mengambil foto tanpa izin",
    # "Permen karet tidak dijual di Singapura",
    # "Wajib bayar cukai rokok; hindari merokok tanpa cukai",
    # "Dilarang menyeberang jalan sembarangan",
    # "Dollar Singapura (SGD)",
    # "Money changer banyak tersedia di area wisata",
    # "Operator telekomunikasi utama adalah Singtel, M1, StarHub, Circles.Life, dan TPG Telecom",
    # "Pembelian SIM card wajib menunjukkan paspor",
    # "Disarankan mengambil asuransi perjalanan yang mencakup evakuasi medis",
    # "Biaya pengobatan menjadi tanggung jawab pribadi",
    # "995",
    # "Sultan Mosque dan beberapa masjid lain semuanya mendapat rating ⭐⭐⭐⭐⭐½",
    # "Vintage Cameras, Army Museum of Singapore, Chinese Heritage, NUS Museum, dan lainnya dengan rating ⭐⭐⭐⭐⭐½",
    # "McDonald's Marina mendapat rating ⭐⭐⭐⭐⭐½",
    # "Bandara Changi",
    # "Disarankan hadir 2 jam sebelum keberangkatan di Bandara Changi",
    # "NUS Museum termasuk tempat wisata yang disebutkan",
    # "Potensi gempa bumi dan polusi udara umum terjadi",
    # "999",
    # "Kedutaan Besar Republik Indonesia, 7 Chatsworth Road, Singapore 249761",
    # "Kontak WhatsApp KBRI: +65 9648 0017 / +65 6737 7422 (Jam Kerja)",
    # "Mengambil foto tanpa izin dilarang",
    # "Mabuk di pesawat atau di ruang publik dilarang",
    # "Simpan paspor dan dokumen penting dengan baik, segera lapor jika hilang",
    # "Swensen's - ION mendapat rating ⭐⭐⭐⭐½",
    # "Merokok dilarang di ruang AC dan zona larangan",

    # 80 answer
    # "Portal tersebut bernama Portal Pelayanan dan Pelindungan WNI di Luar Negeri.",
    # "Portal ini dikelola oleh Direktorat Jenderal Protokol dan Konsuler, Kementerian Luar Negeri.",
    # "Menu utamanya antara lain: Beranda, Lapor Diri, Pelindungan, Pelayanan, Informasi Pelayanan, Pengumuman, Referensi, FAQ, dan Profil WNI.",
    # "Menu Lapor Diri digunakan untuk melaporkan kedatangan, perpindahan, kepulangan, dan keluarga WNI di luar negeri.",
    # "Menu Pelindungan digunakan untuk permohonan pelindungan dan cek status pelindungan.",
    # "Tiga jenis laporan adalah Kedatangan, Perpindahan, dan Kepulangan. Ditambah laporan keluarga.",
    # "User harus login menggunakan email dan password yang sudah terdaftar.",
    # "User login dengan mengisi email dan password pada halaman login.",
    # "User dapat klik tombol daftar dan mengisi form pendaftaran.",
    # "User akan menerima email konfirmasi dan harus klik link di email tersebut.",

    # ====================== fix ================================
    # "Nomor KTKLN diverifikasi ke sistem SISKOTKLN.",
    # "Halaman input KTKLN muncul hanya jika NIK dan paspor tidak ditemukan.",
    #  # 1
    # "Portal Pelayanan dan Pelindungan WNI di Luar Negeri adalah portal yang mewadahi proses layanan seperti lapor diri, pengaduan kasus, pengaduan layanan, hingga pengajuan layanan yang diperlukan oleh WNI di luar negeri.",

    # # 2
    # "Hak akses user WNI terhadap aplikasi meliputi Beranda, Lapor Diri, Pelindungan, Pengaduan Layanan, Pelayanan, Informasi Pelayanan, Pengumuman, Referensi, FAQ, dan Profil WNI",

    # # 3
    # " Untuk memulai aplikasi ini, pertama kali kita bisa menggunakan salah satu browser, kemudian mengisikan alamat URL aplikasi pada address bar, yaitu http://peduliwni.kemlu.go.id/. Setelah user menjalankan URL tersebut, maka akan terlihat tampilan berikut ini.",

    # # 4 - Fungsi menu
    # "Menu ini menampilkan halaman awal ketika user mengakses Portal Pelayanan dan Pelindungan WNI di Luar Negeri. ",
    # "Menu ini digunakan untuk melaporkan diri terkait kedatangan, perpindahan, kepulangan WNI di luar negeri, dan kedatangan anggota keluarga. ",
    # "Menu Pelindungan digunakan untuk membuat permohonan pelindungan dan mengecek statusnya.",
    # "Menu ini digunakan untuk melakukan pengaduan terhadap pelayanan yang dilakukan Perwakilan RI. ",
    # "Menu Pelayanan digunakan untuk mengajukan layanan administrasi penting tanpa harus kembali ke Indonesia.",
    # "Menu Informasi Pelayanan menampilkan informasi pelayanan di setiap perwakilan RI.",
    # "Menu ini menampilkan pengumuman penting bagi WNI di luar negeri, yang terdiri dari pengumuman pusat dan pengumuman lokal (sesuai negara).",
    # "Menu ini menampilkan referensi hukum terkait keberadaan dan perlindungan WNI di luar negeri.",
    # "Menu FAQ menampilkan pertanyaan umum yang sering diajukan oleh WNI.",
    # "Menu ini digunakan untuk melihat profil WNI serta melakukan ubahan password akun WNI ",

    # # 5
    # "Untuk mengakses fitur-fitur portal, user harus melakukan login terlebih dahulu dengan cara klik Masuk kemudian sistem akan menampilkan form login. Apabila belum memiliki akun, user dapat klik daftar dan mengisi form pendaftaran yang disediakan",

    # # 6
    # "Jika sudah memiliki akun, user harus login terlebih dahulu untuk mengakses fitur portal, sesuai standar keamanan website.",

    # # 7
    # "Jika belum memiliki akun, user harus mendaftar terlebih dahulu melalui form pendaftaran yang tersedia di portal.",
    # " Apabila user belum mempunyai akun pada Portal Pelayanan dan Pelindungan WNI di luar negeri, maka user dapat klik Daftar, kemudian sistem akan menampilkan form pendaftaran. Setelah berhasil, user akan mendapatkan email konfirmasi pendaftaran"

    # # 8
    # "Setelah selesai mengisi semua kolom pada form pendaftaran, user harus klik tombol daftar untuk mendaftarkan akun.",

    # # 9
    # "WNI wajib melaporkan keberadaan, kepindahan, perubahan alamat, status izin tinggal, serta kejadian penting seperti kelahiran, perkawinan, perceraian, dan kematian.",
    # "Sistem menyediakan fitur lapor diri untuk mempermudah WNI memenuhi kewajiban pelaporan kepada pemerintah setempat atau perwakilan RI.",

    # # 10
    # "Jenis-jenis lapor diri dalam portal meliputi: Kedatangan WNI, Perpindahan, Kepulangan, dan Keluarga.",

    # "User harus klik  lalu klik 'Lapor Sekarang' pada halaman 'Lapor Diri' dan setelah itu akan diminta mengisi nomor NIK untuk memulai.",
    # "Jika tidak memiliki NIK yang valid, user dapat klik Lupa/Tidak Punya NIK,  maka sistem secara otomatis akan mengarahkan pada halaman input nomor paspor, Jika user tidak mempunyai Nomor Paspor yang valid / paspor hilang, maka user diarahkan pada halaman input nomor KTKLN ",
    # "Setelah memasukkan nomor paspor yang valid, sistem menampilkan halaman untuk pengisian data di luar negeri.",

    # # 2. Kedatangan – Sudah Pernah Lapor Diri
    # "User tidak perlu melakukan proses lapor diri mulai dari awal lagi, namun dapat memappingkan data lapor dirinya yang terdahulu dengan akunnya, dengan klik nama di pojok kanan atas lalu pilih 'Sudah Pernah Lapor di Perwakilan' dan masukkan nomor registrasi.",
    
    # "User dapat memilih ‘Kembali’	, dan melakukan input ulang nomor registrasi lapor diri. Apabila user lupa dengan nomor registrasi lapor diri yang pernah dilakukan, maka user dapat memilih ‘Lupa nomor registrasi’, kemudian sistem akan menampilkan form seperti berikut.  Kemudian user dapat memilih ‘Lanjutkan’ untuk memproses data yang dimasukkan. Jika data yang dimasukkan memang sudah valid dan pernah melakukan lapor diri,",
    
    # "User dapat memilih ‘Lupa nomor registrasi’, kemudian sistem akan menampilkan form. Selesai mengisikan data, user dapat memilih ‘Lanjutkan’ untuk memproses data yang dimasukkan. Jika data yang dimasukkan memang sudah valid dan pernah melakukan lapor diri, maka sistem akan menampilkan pop up akun terhubung",
    # "Jika data yang dimasukkan valid dan cocok, sistem akan menampilkan pop up bahwa data tersebut berhasil terhubung dengan akun.",

    # # 3. Perpindahan
    # "Syarat agar WNI bisa melakukan lapor diri perpindahan di luar negeri adalah user harus sudah pernah melakukan lapor diri kedatangan sebelumnya.",
    # "User harus mengisi data perpindahan, tujuan menetap, dan kontak darurat.",
    # "Untuk melakukan lapor diri perpindahan, user terlebih dahulu harus sudah melakukan lapor diri kedatangan, maka pada saat user klik menu ‘Lapor Diri’. Kemudian user dapat klik ‘Lapor Sekarang’ di Lapor Diri Perpindahan. Selanjutnya user dapat memilih ‘Lanjutkan’ untuk melanjutkan pengisian data selanjutnya yaitu tujuan menetap. Selesai mengisikan data tujuan menetap, user dapat memilih ‘Lanjutkan’ , kemudian sistem akan mengarahkan pada pengisian data kontak darurat. Selesai mengisikan data lapor diri perpindahan, user dapat memilih ‘Lanjutkan’ kemudian sistem akan menampilkan resume data lapor diri perpindahan",

    # # 4. Kepulangan
    # "Fitur Kepulangan digunakan oleh WNI untuk melaporkan kembalinya mereka ke Indonesia.",
    # "User dapat klik 'Lapor Diri', maka sistem akan menampilkan halaman seperti berikut. Untuk melakukan lapor diri kepulangan, maka user dapat klik 'Lapor Sekarang' di Lapor Diri Kepulangan. Setelah selesai mengisikan keseluruhan data, user dapat memilih Lanjutkan. Lapor diri perpindahan sudah masuk ke sistem dan menunggu verifikasi dari perwakilan.",

    # # 5. Keluarga
    # "Fitur ini berfungsi untuk melakukan lapor diri bagi WNI yang membawa keluarga/pengikut.",
    # "Untuk menambahkan anggota keluarga/pengikut, klik tombol 'Buat Lapor Diri' , maka akan tampil form lapor diri keluarga ",

    # # 6. Menu Pelindungan
    # "Menu ini digunakan ketika WNI mengalami kasus di Luar Negeri dan memerlukan bantuan dari pihak perwakilan.",
    # "Fitur utama di dalam menu Pelindungan adalah form permohonan pelindungan dan cek status permohonan pelindungan.",

    # # 7. Buat Permohonan Pelindungan
    # "Untuk membuat permohonan pelindungan, user dapat klik tombol ‘Buat Permohonan’ pada bagian “Permohonan Pelindungan”. Kemudian akan tampil form permohonan pelindungan",
    # "Pada form identias, isikan informasi dengan lengkap agar memudahkan pihak perwakilan mengambil tindatakn terhadap kasus yang ada. Kemudian klik ‘Lanjutkan’ untuk melanjutkan ke form kasus",

    # # 8. Cek Status Permohonan
    # "User dapat melakukan pengecekan status permohonan yang telah dibuat agar memudahkan user untuk melihat update tahapan kasus yang diajukan",
    # "Nomor permohonan digunakan untuk melakukan pengecekan status pelindungan di sistem.",
    # "Untuk menggunakan cek status, isi form cek kasus pada halaman menu pelindungan, kemudian. Kemudian akan tampil halaman cek status permohonan pelindungan klik ‘Cari status’ sebagai berikut. ",

    # # 9. Menu Pelayanan
    # "Menu Pelayanan  menampilkan akses ke halaman pelayanan yang berisi beberapa pelayanan yang dapat diakses oleh user berdasarkan perwakilan yang terdaftar. Menu ini digunakan ketika WNI membutuhkan pelayanan terkait administrasi",
    # "Setelah form dikirim, data masuk ke sistem dan menunggu verifikasi dari perwakilan.",

    # # 10. Informasi Pelayanan
    # "Menu ini menampilkan informasi mengenai pelayanan yang disediakan oleh masing- masing perwakilan di seluruh negara. Pada menu ini, user juga dapat melihat alamat perwakilan , serta dapat melihat pelayanan apa saja yang disediakan di perwakilan tersebut",
    # "User bisa melihat alamat dan daftar pelayanan,  serta jam kerja dari perwakilan yang tersedia.",

    # # 11. Lihat Detail
    # "User memilih salah satu negara untuk melihat daftar perwakilan di negara tersebut.",
    # "Sistem akan menampilkan informasi detail dari perwakilan yang dipilih.",
    # "Di halaman detail perwakilan, informasi yang ditampilkan meliputi alamat, jenis pelayanan, dan jam kerja perwakilan.",

    # # 12. Pencarian Informasi Pelayanan
    # "User melakukan pencarian informasi pelayanan berdasarkan negara, User juga dapat melakukan pencarian informasi pelayanan berdasarkan negara pada ‘Search Bar’, maka sistem langsung menampilkan data negara yang sesuai dengan pencarian yang dilakukan user",

    # # 13. Menu Pengumuman
    # "Untuk dapat mengakses menu tersebut, user dapat memilih ‘Penguman’, kemudian sistem akan menampilkan halaman pengumuman",

    # # 14. Lihat Detail
    # "Pertama, user dapat memilih menu ‘Penguman’, kemudian sistem akan menampilkan halaman pengumuman lalu klik judul pengumuman untuk melihat detail informasi pengumuman tersebut.",

    # 15
    "Pada menu pengumuman, user juga dapat melakukan pencarian pengumuman dengan mengetikkan kata kunci pada ‘Search Bar’, maka sistem langsung menampilkan data pengumuman yang sesuai dengan pencarian yang dilakukan user.",

    # 16
    "Menu Referensi menampilkan referensi hukum terkait perlindungan WNI di luar negeri.",
    "Untuk dapat mengakses menu tersebut, user dapat memilih ‘Referensi’ ,kemudian sistem akan menampilkan halaman referensi yang telah dikelompokan berdasarkan kategori",

    # 17
    "User dapat melihat dan mengubah data pada menu Profil jika status lapor dirinya  sudah valid dengan klik dropdown yang terdapat dibagian kanan atas pada menu profil ",

    # 18
    "User dapat melihat detail identitas, riwayat lapor diri, pelayanan, pengaduan, serta dokumen yang pernah diajukan atau diunggah.",

    # # 19
    # "Laman Identitas menampilkan informasi terkait identitas, data di luar negeri, tujuan menetap dan kontak darurat yang sebelumnya sudah diisikan WNI pada saat melakukan lapor diri",

    # # 20
    # "Untuk mengubah data identitas pada halaman Profil, User dapat klik 'Ubah Profil' di laman Profil WNI, maka field pada halaman profil akan dapat diedit. Setelah melakukan perubahan pada profil WNI user dapat klik ‘Simpan’. Maka data profil akan tersimpan. ",
    # "Jika user mengubah paspor, visa serta Negara, Provinsi dan Kota pada wilayah akreditasi perwakilan yang berbeda membutuhkan validasi dari perwakilan terkait, oleh karena itu sistem akan otomatis meng-create data lapor diri baru",

    # # 21
    # "Fitur Riwayat Lapor Diri menampilkan tanggal, nomor registrasi, jenis laporan (kedatangan, perpindahan, kepulangan), alamat, dan informasi perwakilan.",

    # # 22
    # "Fitur ini menampilkan tanggal pengajuan, perwakilan tempat pengajuan layanan, nomor layanan, Jenis layanan serta status dari layanan yang sudah diajukan",

    # # 23
    # "Riwayat Pengaduan menampilkan informasi tanggal pengaduan, informasi perwakilan, nomor pengaduan, jenis pengaduan dan kategori kasus, serta status dari pengaduan ",

    # # 24
    # "Kategori data pengaduan meliputi informasi tanggal pengaduan, informasi perwakilan, nomor pengaduan, jenis pengaduan dan kategori kasus, serta status dari pengaduan",

    # # 25
    # "Laman Riwayat Dokumen menampilkan preview dari dokumen-dokumen yang sebelumnya telah diunggah oleh user di portal.",

    # # 26
    # "Untuk mengubah password melalui menu Profil di Portal Pelayanan WNI, user dapat klik nama di pojok kanan atas ‘Menu Profil’. Lalu user dapat klik ‘Ubah Password’. User dapat mengisikan kata sandi lama, mengisikan kata sandi baru, dan mengisikan ulang kata sandi baru. Setelah itu user dapat klik ‘Ubah’, maka sistem akan mengubah password lama. Jika user ingin membatalkan pengubahan password, maka user dapat klik ‘Tutup’ ",

    # # 27
    # "Untuk keluar dari aplikasi, user dapat keluar dari aplikasi dengan klik nama di pojok kanan atas  ‘Menu Profil’, kemudian user dapat klik ‘Keluar’ publik."

    # "Riwayat pengaduan WNI dapat ditemukan dengan mengklik pada menu profil lalu klik Riwayat Pengaduan.",
    # "WNI dapat mengubah kata sandi dengan mengklik nama mereka di pojok kanan atas layar, lalu memilih 'Ubah Password' dan mengisi kata sandi lama, kata sandi baru, dan konfirmasi kata sandi baru.",
    # "Setelah mengisi kata sandi lama dan baru untuk mengubah password, WNI harus mengklik tombol 'Simpan'.",
    # "WNI dapat keluar dari aplikasi dengan mengklik nama di pojok kanan atas, kemudian akan muncul menu yang salah satunya adalah 'Keluar Aplikasi'.",
    # "Setelah WNI mengklik tombol 'Keluar Aplikasi', sistem akan mengembalikan halaman ke halaman publik.",
    # "Tombol 'Keluar Aplikasi' dan 'Ubah Password' dapat ditemukan setelah WNI mengklik nama mereka di pojok kanan atas layar aplikasi.",
    # "WNI yang sudah pernah lapor diri dapat melaporkan kedatangan mereka dengan masuk ke akun yang sudah ada, lalu memilih menu 'Lapor Diri' dan 'Kedatangan', kemudian mengisi formulir yang relevan dengan data terbaru.",
    # "Perbedaan utamanya adalah WNI yang belum pernah lapor diri harus membuat akun baru dan mengisi data awal, sedangkan WNI yang sudah pernah lapor diri hanya perlu masuk ke akun yang sudah ada dan memperbarui informasi kedatangan mereka.",
    # "Jika WNI ingin melaporkan perpindahan domisili, mereka harus mengakses menu 'Lapor Diri' dan kemudian memilih opsi 'Perpindahan'.",
    # "Informasi yang diperlukan saat WNI melaporkan perpindahan di sistem mencakup data pribadi, alamat lama, alamat baru, dan tanggal perpindahan.",
    # "WNI dapat melaporkan kepulangan mereka ke Indonesia melalui Portal Pelayanan dan Perlindungan WNI dengan memilih menu 'Lapor Diri' dan kemudian opsi 'Kepulangan', lalu mengisi informasi yang diperlukan.",
    # "Dokumen yang perlu disiapkan saat melaporkan kepulangan antara lain salinan paspor, visa (jika ada), dan tiket kepulangan.",
    # "WNI dapat melihat dokumen-dokumen yang telah mereka unggah sebelumnya dengan mengklik pada 'Riwayat Dokumen' yang akan menampilkan preview dokumen.",
    # "Fungsi dari menu 'Keluarga' adalah untuk mengelola dan mendaftarkan informasi anggota keluarga WNI yang tinggal di luar negeri.",
    # "Informasi yang dapat dikelola dalam menu 'Keluarga' meliputi nama anggota keluarga, hubungan, tanggal lahir, nomor paspor, dan data identitas lainnya.",
    # "WNI dapat menambahkan anggota keluarga baru ke dalam akun mereka dengan mengakses menu 'Keluarga' dan memilih opsi untuk menambah data anggota keluarga baru, lalu mengisi formulir yang tersedia.",
    # "Jika WNI ingin mengajukan permohonan perlindungan, mereka harus memilih menu 'Perlindungan' di dalam aplikasi.",
    # "Jenis pengaduan yang dapat diajukan melalui fitur perlindungan mencakup berbagai kasus seperti masalah keimigrasian, ketenagakerjaan, kesehatan, dan kasus darurat lainnya.",

    # "Setelah mengajukan pengaduan, WNI dapat memeriksa status pengaduan mereka dengan mengakses halaman 'Riwayat Pengaduan' di dalam profil mereka.",
    # "Halaman riwayat pengaduan menampilkan informasi tanggal pengaduan, informasi perwakilan, nomor pengaduan, jenis pengaduan, kategori kasus, serta status dari pengaduan tersebut.",
    # "Informasi yang termuat dalam riwayat pengaduan meliputi tanggal pengaduan, perwakilan yang menangani, nomor pengaduan, jenis pengaduan, kategori kasus, dan status pengaduan (misalnya, dalam proses, selesai, ditolak).",
    # "Deskripsi Singkat Aplikasi dalam konteks panduan ini adalah gambaran umum mengenai fungsi dan tujuan dari Portal Pelayanan dan Perlindungan WNI di Luar Negeri.",
    # "Target pengguna dari aplikasi Portal Pelayanan dan Perlindungan WNI ini adalah Warga Negara Indonesia (WNI) yang berada di luar negeri.",
    # "Langkah awal yang harus dilakukan pengguna sebelum mulai menggunakan aplikasi ini adalah melakukan registrasi akun baru jika belum memiliki akun, atau masuk (login) jika sudah memiliki akun.",
    # "Pengguna dapat menemukan daftar isi panduan pada halaman kedua (ii) dari dokumen panduan.",
    # "Fungsi menu utama yang tersedia di aplikasi mencakup Beranda, Lapor Diri (Kedatangan, Perpindahan, Kepulangan, Keluarga), Pelindungan, dan Riwayat (Pengaduan, Dokumen).",
    # "Menu Beranda dapat diakses setelah pengguna berhasil masuk ke dalam aplikasi atau merupakan halaman awal setelah login.",
    # "Informasi yang ditampilkan pada halaman Beranda mencakup informasi umum, notifikasi, dan ringkasan status lapor diri atau pengaduan.",
    # "Jika WNI belum memiliki akun, mereka harus melakukan registrasi akun baru dengan mengklik tombol 'Daftar' di halaman utama aplikasi.",
    # "Pada tahap pendaftaran akun, informasi pribadi yang wajib diisi meliputi email, kata sandi, nama lengkap, dan Nomor Induk Kependudukan (NIK).",
    # "Sistem akan mengkonfirmasi keberhasilan pendaftaran akun dengan menampilkan pesan pop-up atau notifikasi bahwa akun telah berhasil dibuat dan mengarahkan pengguna untuk melakukan aktivasi via email.",
    # "Setelah berhasil mendaftar, langkah selanjutnya bagi WNI untuk lapor diri adalah melakukan aktivasi akun melalui tautan yang dikirimkan ke email terdaftar, kemudian login dan memilih menu Lapor Diri.",
    # "Panduan tidak menyebutkan batas waktu spesifik untuk melengkapi proses lapor diri setelah pendaftaran, namun disarankan untuk segera melengkapi data.",
    # "Panduan tidak secara eksplisit menyebutkan fitur pemulihan kata sandi jika WNI lupa, namun umumnya sistem semacam ini memiliki opsi 'Lupa Kata Sandi'.",
    # "Jika WNI ingin membatalkan perubahan kata sandi, mereka dapat mengklik tombol 'Batal' pada pop-up perubahan kata sandi.",
    # "Ya, ada opsi untuk mengelola informasi profil pribadi WNI di aplikasi yang dapat diakses dengan mengklik nama pengguna di pojok kanan atas.",
    # "WNI dapat memperbarui data profil mereka dengan mengklik nama di pojok kanan atas, lalu memilih 'Informasi Akun' dan mengedit data yang diperlukan, kemudian menyimpan perubahan.",
    # "Panduan tidak secara spesifik menyebutkan kemampuan mengunggah lebih dari satu dokumen pada satu waktu, tetapi biasanya diunggah satu per satu atau dalam kelompok jika ada fitur drag-and-drop.",
    # "Jenis file yang diizinkan untuk diunggah sebagai dokumen pendukung biasanya adalah PDF atau format gambar umum (JPG, PNG).",
    # "Proses validasi data setelah WNI mengisi formulir lapor diri dilakukan secara otomatis oleh sistem untuk memastikan kelengkapan dan format data yang benar.",
    # "Jika ada informasi yang tidak valid saat pengisian formulir, sistem akan menampilkan pesan kesalahan atau menandai kolom yang perlu diperbaiki.",
    # "Ya, panduan menyiratkan adanya notifikasi setelah proses lapor diri selesai, biasanya melalui status di riwayat lapor diri.",
    # "WNI dapat melihat rincian lapor diri yang telah mereka ajukan melalui menu 'Riwayat' atau 'Lapor Diri' yang akan menampilkan detail dari laporan yang sudah terkirim.",
    # "Panduan tidak secara eksplisit menyatakan apakah WNI dapat mengedit informasi lapor diri yang sudah terkirim, namun untuk beberapa perubahan penting mungkin diperlukan pengajuan ulang atau menghubungi Perwakilan.",
    # "Status pengaduan dalam riwayat pengaduan menunjukkan tahapan proses pengaduan, seperti 'menunggu verifikasi', 'dalam proses', 'selesai', atau 'ditolak'.",
    # "Pihak yang bertanggung jawab untuk memproses pengaduan yang diajukan WNI adalah Perwakilan Republik Indonesia di luar negeri (Kedutaan Besar atau Konsulat Jenderal).",
    # "Panduan ini dirancang untuk tampilan web, namun tidak secara spesifik menyebutkan dukungan penuh untuk aplikasi seluler, meskipun antarmuka umumnya responsif.",
    # "Tujuan utama dari Portal Pelayanan dan Perlindungan WNI di luar negeri adalah untuk mempermudah WNI dalam melakukan lapor diri dan mengajukan permohonan perlindungan serta memantau statusnya.",
    # "Fitur 'preview dokumen' memungkinkan pengguna untuk melihat pratinjau dokumen yang sudah diunggah tanpa harus mengunduhnya terlebih dahulu.",
    # "Panduan tidak secara eksplisit menyebutkan kemampuan WNI untuk mengunduh dokumen yang telah mereka unggah dari sistem, namun fitur 'preview' biasanya menyertai opsi unduh.",
    # "Panduan tidak menyebutkan batasan ukuran file secara spesifik, namun biasanya ada batasan untuk menghindari beban server yang berlebihan.",
    # "Sistem memastikan keamanan data pribadi WNI melalui penggunaan enkripsi data dan akses terbatas berdasarkan hak pengguna serta standar keamanan informasi yang berlaku.",
    # "'Perwakilan' dalam konteks pengaduan mengacu pada Kedutaan Besar Republik Indonesia (KBRI) atau Konsulat Jenderal Republik Indonesia (KJRI) di negara tempat WNI berada, yang akan menangani pengaduan tersebut.",
    # "Jika WNI memiliki pertanyaan tentang penggunaan aplikasi, mereka dapat mencari bantuan melalui Perwakilan RI atau bagian dukungan yang mungkin disediakan oleh Kementerian Luar Negeri.",
    # "Panduan tidak secara eksplisit menyebutkan adanya fitur bantuan atau FAQ di dalam aplikasi, namun biasanya disediakan dalam bentuk buku panduan atau kontak dukungan.",
    # "WNI yang sudah pernah lapor diri diidentifikasi oleh sistem melalui nomor identifikasi unik mereka (misalnya NIK atau nomor paspor) yang terkait dengan akun yang sudah ada.",
    # "Keuntungan menggunakan Portal Pelayanan dan Perlindungan WNI dibandingkan metode lapor diri manual adalah efisiensi, aksesibilitas 24/7, dan kemudahan dalam memantau status permohonan secara online.",
    # "Proses verifikasi identitas WNI saat pendaftaran akun dilakukan melalui pengisian NIK dan validasi data dasar, serta kemungkinan verifikasi email.",
    # "Panduan tidak menyebutkan persyaratan usia minimum untuk menggunakan aplikasi ini, tetapi secara implisit ditujukan untuk WNI dewasa yang dapat mengurus dokumen pribadi.",
    # "Jika WNI mengalami masalah teknis saat menggunakan aplikasi, mereka harus menghubungi Perwakilan Republik Indonesia atau tim dukungan teknis yang tertera jika ada.",
    # "Data yang diunggah WNI kemungkinan besar disimpan secara permanen di sistem sebagai bagian dari catatan lapor diri dan riwayat perlindungan, sesuai dengan kebijakan penyimpanan data pemerintah.",
    # "Aplikasi ini mendukung perlindungan WNI dalam situasi darurat dengan menyediakan fitur pengajuan pengaduan yang memungkinkan WNI melaporkan kasus-kasar darurat untuk ditindaklanjuti oleh Perwakilan.",
    # "Panduan tidak menyebutkan adanya integrasi langsung dengan layanan darurat lokal di negara tempat WNI berada, namun Perwakilan RI yang menerima pengaduan dapat berkoordinasi dengan pihak terkait.",
    # "Aplikasi ini memastikan informasi yang diberikan WNI akurat melalui validasi form input, meminta dokumen pendukung, dan proses verifikasi oleh Perwakilan.",
    # "Ya, WNI akan menerima pemberitahuan mengenai status permohonan atau pengaduan mereka, yang dapat dilihat di halaman riwayat pengaduan atau melalui notifikasi sistem.",
    # "Perbedaan utamanya adalah 'Kedatangan - Belum Pernah Lapor Diri' untuk WNI yang baru pertama kali mendaftar dan lapor diri, sedangkan 'Kedatangan - Sudah Pernah Lapor Diri' adalah untuk WNI yang sudah memiliki akun dan sedang memperbarui informasi kedatangan mereka.",
    # "WNI dapat mengedit data keluarga yang sudah ada di sistem dengan mengakses menu 'Keluarga', memilih anggota keluarga yang ingin diedit, dan memperbarui informasi yang diperlukan.",
    # "Panduan tidak secara eksplisit menyebutkan fitur untuk mencetak bukti lapor diri, namun WNI mungkin dapat mencetak halaman detail laporan dari browser mereka.",
    # "Prosedur pelaporan jika WNI ingin membatalkan pendaftaran lapor diri tidak dijelaskan secara langsung dalam panduan, kemungkinan memerlukan komunikasi langsung dengan Perwakilan RI.",
    # "Langkah-langkah untuk melaporkan 'Kepulangan' meliputi memilih menu 'Lapor Diri' kemudian 'Kepulangan', mengisi data kepulangan seperti tanggal dan tujuan, serta mengunggah dokumen pendukung jika diminta.",
    # "Dalam konteks 'Riwayat Dokumen', pengguna dapat melihat pratinjau dokumen-dokumen yang sebelumnya sudah diunggah pada portal.",
    # "Jika WNI perlu mengubah informasi penting seperti nomor paspor setelah lapor diri, mereka kemungkinan perlu mengajukan perubahan data melalui Perwakilan RI atau mencari opsi 'Ubah Profil' jika tersedia untuk data tersebut.",
    # "Panduan tidak menyebutkan fitur pengajuan pengaduan anonim; semua pengaduan memerlukan identitas WNI yang jelas.",
    # "Sistem membedakan antara 'jenis pengaduan' (misalnya, masalah paspor, masalah ketenagakerjaan) dan 'kategori kasus' (misalnya, visa overstay, gaji tidak dibayar) sebagai sub-klasifikasi dari masalah yang dilaporkan.",
    # "Panduan ini sendiri adalah panduan visual, namun tidak disebutkan adanya video tutorial terpisah dalam dokumen.",
    # "Panduan tidak secara spesifik menyebutkan jumlah maksimal anggota keluarga yang dapat ditambahkan ke dalam satu akun.",
    # "Portal Pelayanan dan Perlindungan WNI memfasilitasi komunikasi antara WNI dan Perwakilan melalui sistem pengaduan, di mana WNI dapat mengirimkan laporan dan Perwakilan dapat merespon atau menindaklanjuti.",
    # "'Halaman Publik' dalam konteks 'Keluar Aplikasi' adalah halaman beranda atau login yang tidak memerlukan autentikasi, tempat pengguna dapat mengakses informasi umum atau memulai proses login/registrasi.",
    # "WNI harus memastikan bahwa semua informasi yang relevan seperti data pribadi, informasi kontak, tanggal, dan detail lapor diri lainnya sudah benar sebelum mengklik 'Simpan' pada formulir.",
    # "WNI dapat memastikan bahwa data yang mereka masukkan aman dengan memastikan mereka mengakses situs web resmi, menggunakan koneksi internet yang aman, dan menjaga kerahasiaan kata sandi mereka.",
    # "Panduan tidak secara eksplisit menyebutkan fitur peringatan atau notifikasi untuk perpanjangan masa lapor diri."
]



# answers = []
# contexts = []             

# for query in questions:
#     # print(f"\n🟨 Query: {query}")
#     output = rag_chain.invoke({
#         "question": query,
#         "chat_history": []
#     })

#     # Debug output
#     # print("🔹 Raw output:", output)
#     # print("🔹 Type of output:", type(output))

#     # Ambil jawaban dari output
#     try:
#         if isinstance(output, dict):
#             print("🔹 Keys:", output.keys())
#             ans_text = output.get("answer") or output.get("response") or ""
#         elif hasattr(output, "content"):
#             ans_text = output.content
#         else:
#             ans_text = str(output)
#     except Exception as e:
#         print(f"❌ Error saat parsing output: {e}")
#         ans_text = ""

#     # print(f"✅ Jawaban: {ans_text}")
#     answers.append(ans_text)

#     # Ambil konteks
#     docs = retriever.invoke(query)
#     context_list = [doc.page_content for doc in docs]
#     contexts.append(context_list)

#     time.sleep(5)



# # Cek apakah jawaban berhasil dikumpulkan
# # print("\n📌 Isi answers sebelum dataset:", answers)

# # Buat dataset untuk evaluasi
# data = {
#     "question": questions,
#     "answer": answers,
#     "contexts": contexts,
#     "reference": ground_truths
# }
# dataset = Dataset.from_dict(data)

# # Evaluasi RAG
# result = evaluate(
#     dataset=dataset,
#     metrics=[
#         context_precision,
#         context_recall,
#         faithfulness,
#         answer_correctness
#     ],
# )


answers = []
contexts = []

# === STEP 3: Inisialisasi LLM GPT-3.5 dan Embedding ===
llm = ChatOpenAI(model="gpt-3.5-turbo")
llm_wrapper = LangchainLLMWrapper(llm)
embeddings = OpenAIEmbeddings()

# === STEP 4: Adaptasi Metrik yang Perlu Bahasa Indonesia ===

# 1. Answer relevancy
answer_relevance = AnswerRelevancy(
    name="answer_relevancy",
    strictness=3,
    embeddings=embeddings
)

# Adapt prompt AnswerRelevancy
async def adapt_answer_relevancy():
    adapted_prompts = await answer_relevance.adapt_prompts(
        language="indonesian",
        llm=llm_wrapper
    )
    answer_relevance.set_prompts(**adapted_prompts)

# Jalankan adaptasi answer_relevancy (karena manual)
asyncio.run(adapt_answer_relevancy())

# === STEP 5: Loop ke Chatbot ===
for query in questions:
    output = rag_chain.invoke({
        "question": query,
        "chat_history": []
    })

    try:
        if isinstance(output, dict):
            ans_text = output.get("answer") or output.get("response") or ""
        elif hasattr(output, "content"):
            ans_text = output.content
        else:
            ans_text = str(output)
    except Exception as e:
        print(f"❌ Error saat parsing output: {e}")
        ans_text = ""

    answers.append(ans_text)

    docs = retriever.invoke(query)
    context_list = [doc.page_content for doc in docs]
    contexts.append(context_list)

    time.sleep(3)

# === STEP 6: Buat Dataset untuk Evaluasi ===
# data = Dataset.from_list([
#     {
#         "question": q,
#         "answer": a,
#         "contexts": c,
#         "reference": g
#     }
#     for q, a, c, g in zip(questions, answers, contexts, ground_truths)
# ])
data = {
    "question": questions,
    "answer": answers,
    "contexts": contexts,
    "reference": ground_truths
}
dataset = Dataset.from_dict(data)

# === STEP 7: Evaluasi dengan Semua Metrik ===
result = evaluate(
    dataset=dataset,
    metrics=[
        context_precision,
        context_recall,
        faithfulness, 
        answer_relevance,
        answer_correctness
    ],
    llm=llm,
    embeddings=embeddings
)


# Simpan hasil evaluasi
df = result.to_pandas()

df.to_csv("evaluation/evaluation_results_test.csv", index=False)
# df.to_csv("evaluation/evaluation_results_openai.csv", index=False)
print("📁 Evaluasi selesai, hasil disimpan di evaluation_results.csv")