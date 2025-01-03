from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import os


def open_main_window():
    # Destroy the current window to avoid overlapping windows
    root.destroy()

    # Run main.py to open the next window (assuming main.py is a separate file)
    os.system("python main.py")



# Konfigurasi mode dan tema
customtkinter.set_appearance_mode('light')  # Mode penampilan
customtkinter.set_default_color_theme('dark-blue')  # Tema warna

# Membuat jendela utama
root = customtkinter.CTk()
root.geometry('1200x800')  # Ukuran jendela


navbar = customtkinter.CTkFrame(root, fg_color="black", height=50)
navbar.pack(fill="x", side="top")

navbar_label = customtkinter.CTkLabel(
    navbar,
    text="Indonesian Journal",
    font=("Arial", 20, "bold"),
    text_color="white",
)
navbar_label.pack(pady=15)

# Membuat frame scrollable
my_frame = customtkinter.CTkScrollableFrame(root, fg_color='white')
my_frame.pack(fill="both", expand=True)

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Merbabu 3145 MDPL",
    font=("Arial", 40, "bold"),  # Menggunakan gaya bold
    text_color='#242322',
)
title_label.pack(pady=(30,15)) 

image_path = r"D:\KENNARD\lomba\build\assets\frame0\mimg1.jpg"  # Ganti dengan path gambar Anda
image = Image.open(image_path)
image = image.resize((600, 400))  # Sesuaikan ukuran gambar
photo = ImageTk.PhotoImage(image)

# Menambahkan label untuk gambar
image_label = customtkinter.CTkLabel(my_frame, image=photo, text="")
image_label.pack(pady=20)

title_label = customtkinter.CTkLabel(
    my_frame,
    text="",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(30,15))

# Teks cerita
text_1 = (
    "Salah satu hal terberat saat mendaki gunung adalah bangun tengah malam untuk berangkat ke puncak. Tantangannya tidak hanya kantuk, tetapi juga suhu dingin yang biasanya mencapai titik terendah sebelum fajar. Apalagi jika jarak dari tempat camp ke puncak masih cukup jauh, sehingga harus kuat membuka mata lebih awal.\n\n"
    "Kondisi tersebut umum dilakukan di gunung mana pun dengan program pendakian 2 hari 1 malam. Termasuk pendakian Gunung Merbabu via Suwanting. Terlepas kebijakan pembatasan durasi pendakian dari taman nasional, durasi tersebut sudah sangat cukup untuk mengunjungi gunung yang bertetangga dengan Merapi itu.\n\n"
    "Untungnya kami hanya tinggal menempuh 1,5 kilometer lagi menuju dua puncak tertinggi yang terletak berdekatan, yaitu Triangulasi dan Kenteng Songo. Naik sekitar 400 meter vertikal untuk mencapai ketinggian hampir 3.145 mdpl. Secara teori, butuh waktu paling cepat 1-1,5 jam perjalanan.\n\n"
    "“Kadang-kadang bisa lebih dari 2 jam, karena keasyikan foto-foto di sabana,” kelakar Pak Ambon saat briefing kemarin. '\n\n"
    "Pak Ambon mungkin benar. Pemandangan sabana khas jalur Suwanting bisa jadi jauh lebih memikat ketimbang puncaknya. Seperti halnya Ranu Kumbolo di Gunung Semeru, atau danau Segara Anak di Gunung Rinjani. \n\n"
    "Saya sendiri yakin kami pun tidak akan lama berselebrasi di titik tertinggi—kalau memang sampai puncak. Kedua puncak tersebut merupakan pertemuan semua jalur resmi Merbabu, yakni Suwanting, Selo, Tekhelan atau Wekas (dua jalur ini bertemu di pos Helipad). Akhir pekan jelas menjadi masa berkerumun manusia, yang kebanyakan memiliki tujuan sama: foto dengan plang, plakat, atau tugu penanda puncak. Suasana yang tidak ingin kami nikmati berlama-lama."
)

# Menambahkan label untuk teks
paragraph_label_1 = customtkinter.CTkLabel(
    my_frame,
    text=text_1,
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_1.pack(padx=50, pady=(10,50))

image2_path = r"D:\KENNARD\lomba\build\assets\frame0\mimg2.jpg"  # Ganti dengan path gambar kedua Anda
image2 = Image.open(image2_path)
image2 = image2.resize((600, 400))  # Sesuaikan ukuran gambar
photo2 = ImageTk.PhotoImage(image2)

# Menambahkan label untuk gambar kedua
image2_label = customtkinter.CTkLabel(my_frame, image=photo2, text="")
image2_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Menunda Lelah",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))

text_2 = (
    "Adanya potensi hujan seperti hari pertama membuat kami membulatkan tekad untuk berangkat ke puncak sesegera mungkin. Kaus kaki dan sepatu jelas belum kering. Alas kaki yang masih basah sebenarnya membuat berjalan kurang nyaman. Namun, kami tak ambil pusing. Toh, kemarin juga basah-basahan saat mendaki sampai bagian dalam sepatu kebanjiran.\n\n"
    "Secangkir teh hangat, dua biji kurma, dan sepotong roti tawar saya lahap untuk menghangatkan tubuh. Teman satu tenda, Evelyne dan Rivai, melakukan hal serupa. Hanya beda di jenis minumannya saja. \n\n"
    "“Mas Bagus, aman? Jadi ke puncak?” tanya saya setengah teriak ke tenda sebelah, tempat kawan asal Jepara itu tidur sendirian semalam.\n\n"
    "“Aman!” sahutnya.\n\n"
    "Saya melongok ke langit melalui pintu tenda. Masih terlihat jejak bulan dan bintang-bintang berjarak yang bersanding awan kelabu tipis. Namun, cahayanya kalah terang dengan lampu-lampu artifisial buatan operator wisata di “kampung” tenda sebelah. Meriah sekali, seperti bumi perkemahan Sabtu-Minggu. \n\n"
    "Pertanda baik, pikir saya, karena semalam sempat hujan sebentar saat kami tidur. Walaupun begitu tidur saya dan teman-teman tidak terlalu nyenyak, karena sampai jelang tengah malam pun masih banyak pendaki yang baru tiba di Pos 3. Jelang subuh seperti ini, atau setidaknya menunggu agak terang, mereka juga pergi ke puncak. Saya tidak bisa membayangkan akan selelah apa yang mereka rasakan. Istirahatnya hanya sebentar.\n\n"
    "Sementara kami saja masih terasa pegal di sekujur tubuh. Saya berharap dengan mencoba terus berjalan rasa capek tidak akan begitu terasa. Atau setidaknya tertunda sejenak. Kondisi seperti ini mungkin dialami juga oleh pendaki-pendaki lain saat itu, yang bersama-sama mencoba berjuang menggapai puncak tertinggi. "
)

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text=text_2,
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,40))

image3_path = r"D:\KENNARD\lomba\build\assets\frame0\mimg3.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Yang Kami Lihat di Sabana",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))



text_2 = (
    "Cahaya lampu senter maupun alat penerang lainnya menyemut di jalan setapak yang membelah sabana Merbabu. Dari kejauhan seperti kunang-kunang yang terbang vertikal secara perlahan. Setiap pendaki silih berganti saling mendahului dan bertegur sapa. Memberi semangat satu sama lain. Bahu-membahu mendorong yang kepayahan, menarik yang lelah. Seperti inilah sisi positif dari pendakian di gunung, yang saya harapkan juga berlaku tatkala sedang mengalami kesulitan di hutan.\n\n"
    "Sebelum puncak, terdapat tiga kawasan sabana yang harus kami lewati. Setelah berjalan hampir setengah jam sampai ke Sabana 1 (2.828 mdpl), saya merasa treknya ternyata tidak terjal-terjal amat. Mungkin karena saya tidak membawa beban berat seperti pendakian lintas jalur Suwanting-Selo lima tahun lalu. Selain itu matahari belum muncul, sehingga tidak terasa terik.\n\n"
    "Sepanjang jalur, tidak banyak aktivitas yang kami lakukan selain terus berjalan. Foto-foto pun seperlunya. Saya bukan orang yang mudah kalap dalam membuat konten, ketika melihat pemandangan bagus. \n\n"
    "Namun, saya akui lukisan fajar pagi itu membuat saya tertegun. Terutama setelah melewati Sabana 2 (2.915 mdpl) dan berhenti agak lama di Sabana 3 (2.984 mdpl). Kurang lebih satu jam perjalanan dari tenda kami. \n\n"
)

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text=text_2,
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,40))



image3_path = r"D:\KENNARD\lomba\build\assets\frame0\mimg4.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,50)) 



text_2 = (
    "Saya mengedarkan pandangan hampir 360 derajat. Selain sisa tanjakan ke arah puncak Suwanting (3.105 mdpl) dan dua dataran tertinggi Merbabu, sajian alam memberikan pengalaman tak terlupakan. Tiba-tiba, ingatan soal pendakian bersusah payah menerjang hujan kemarin untuk sesaat sirna. Seketika pula saya mampu melupakan rasa lelah. \n\n"
    "“Itu kelihatan Sindoro dan Sumbing juga, Mbak,” ucap saya kepada Mbak Evelyne sambil menunjuk ke arah barat. Gunung Sumbing punya memori yang lekat dengan kami, karena sempat mendaki via jalur Banaran akhir tahun lalu bersama adik ipar saya dan temannya.\n\n"
    "Kabut tipis menutup bagian tubuh gunung ke bawah. Gunung-gunung kecil seperti Andong dan Telomoyo seperti melayang. Adapun atraksi utama yang tetap banyak dipotret adalah si tetangga, Gunung Merapi. Sejenak saya berpikir, makin kita berada di ketinggian, sudut pandang menjadi lebih luas dan menarik. \n\n"
    "Sepertinya memang benar jika kita bisa melihat bumi dari kacamata burung. Terbang ke mana pun sesuka hati. Pagi itu, tak banyak burung yang kami lihat. Hanya purwarupanya saja, yaitu sekawanan drone yang diterbangkan pemiliknya."
)

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text=text_2,
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,40))



image3_path = r"D:\KENNARD\lomba\build\assets\frame0\mimg4.jpeg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Puncak Seperlunya, Pulang Secepatnya",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))



text_2 = (
    "Dua jam perjalanan adalah waktu yang kami catat untuk tiba di puncak Triangulasi dan Kenteng Songo. Masing-masing hanya berjarak 100 meter dengan kontur relatif landai. Seperti yang saya duga, tugu jumbo bertuliskan nama dan ketinggian puncak itu seperti benda keramat yang wajib masuk dalam memori kamera. Adapun kami hanya tertarik untuk mengabadikan diri secara bersama-sama dalam satu atau dua bingkai foto.\n\n"
    "Kami berempat sepakat untuk tidak berlama-lama di puncak. Selain ingin lebih menikmati sabana, kami juga mengejar waktu agar tidak terlalu sore tiba di basecamp. Kami berencana meninggalkan Pos 3 Dampo Awang sekitar pukul 10.00 WIB.\n\n"
    "Saya teringat pagi sebelum berangkat naik ojek ke pintu hutan kemarin. Waktu itu cuaca hampir secerah hari ini, tetapi siang sampai sore terjadi dua kali hujan deras. Jika hujan jatuh lagi di tengah perjalanan, jalur akan semakin sulit dilewati dan memakan waktu lebih lama untuk turun."
)

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text=text_2,
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,40))



image3_path = r"D:\KENNARD\lomba\build\assets\frame0\mimg5.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,50)) 


text_2 = (
    "Meskipun manusia hanya berencana, saya tak kapok menitipkan harapan agar alam bermurah hati hari ini. Sepanjang perjalanan kembali ke tenda, kemudian berkemas dan  lanjut turun ke dusun, tidak terhitung berapa kali saya harus menengadah ke langit. Merapalkan doa seperti semalam, agar Tuhan “memasukkan” hujan ke jadwal cuti.\n\n"
    "Harapan itu semakin kencang saya genggam dalam pikiran, tatkala mendung dan kabut sempat menyelimuti lembah-lembah di sepanjang punggungan jalur Suwanting. Kepasrahan semakin lekat ketika perut mulai keroncongan dan langkah kian gontai selepas Pos 2 Bendera. \n\n"
    "Namun, sampai kami bertemu pintu hutan dan tiba di rumah Pak Ambon pukul 15.30, tak ada setetes pun air langit yang membasahi tanah. Hujan baru benar-benar turun teramat deras ketika saya sudah jauh dari kawasan gunung, tepatnya dalam perjalanan pulang ke rumah.\n\n"
    "Entah, mungkin doa saya semalam terkabul. Atau, harapan-harapan baik dari pendaki lain selepas hujan kemarin."
)

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text=text_2,
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,40))



paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Source: Telusuri.id/Rifqy Faiza Rahman",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='grey',
    font=("Arial", 13)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))


back_button = customtkinter.CTkButton(
    my_frame,
    text='Kembali',
    fg_color='black',
    text_color='white',
    command=open_main_window,
)

back_button.pack(pady=(0,50))


# Menjalankan loop utama
root.mainloop()
