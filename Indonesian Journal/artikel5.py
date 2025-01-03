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
    text="Trip ke Karimun Jawa",
    font=("Arial", 40, "bold"),  # Menggunakan gaya bold
    text_color='#242322',
)
title_label.pack(pady=(30,15)) 

image_path = r"D:\KENNARD\lomba\build\assets\frame0\kimg1.jpg"  # Ganti dengan path gambar Anda
image = Image.open(image_path)
image = image.resize((600, 400))  # Sesuaikan ukuran gambar
photo = ImageTk.PhotoImage(image)

# Menambahkan label untuk gambar
image_label = customtkinter.CTkLabel(my_frame, image=photo, text="")
image_label.pack(pady=20)

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Asal Mula Nama Karimun Jawa",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(30,15))

# Teks cerita
text_karimunjawa_1 = (
    "Sebelum kita jauh menjelajah keindahan di gugusan pulau Karimunjawa ini, "
    "saya ingin bercerita kembali tentang asal mula nama Karimunjawa.\n\n"
    "Mendengar nama Karimunjawa, sontak pikiran saya melayang kembali ke masa kecil "
    "yang mana pada saat itu setiap malam menjelang tidur kakek sering bercerita tentang kisah keteladanan Wali Songo.\n\n"
    "Wali Songo adalah para penyebar agama Islam di pulau Jawa. Salah satunya adalah Sunan Kudus (Jafar Shodiq). "
    "Seingat saya, nama Karimunjawa sendiri berasal dari kisah keluarga ini yang ceritanya sudah beredar dan diyakini oleh masyarakat hingga kini. "
    "Karena kebetulan saya menghabiskan waktu kecil tidak jauh di daerah Sunan Kudus menyebarkan ajaran Islamnya, jadi kakek tahu benar cerita ini.\n\n"
    "Pada masa itu hampir seluruh wilayah Jawa masih menganut ajaran Hindu dan Buddha. Nah, Sunan Kudus ini memiliki cara "
    "yang dianggapnya jitu untuk meraih hati masyarakat Jawa untuk memeluk Islam, yakni melalui metode dakwah dengan Gamelan (alat musik tradisional Jawa) "
    "dan Gending (lagu-lagu Jawa).\n\n"
    "Cara tersebut ternyata jitu, banyak gending-gending yang diciptakan oleh Jafar Shodiq diterima masyarakat, dan di setiap gending yang beliau ciptakan "
    "kemudian disisipkan ajaran Islam, hingga Islam berkembang di daerah Kudus dan sekitarnya.\n\n"
    "Namun metode seperti ini ditentang sendiri oleh putra Sunan Kudus yaitu Amir Khasan, dan di saat sang ayah sedang menyebarkan ajaran Islam di daerah "
    "yang memakan waktu cukup lama, padepokan dititipkan ke anaknya. Di sinilah Amir Khasan menerapkan ajaran yang secara langsung mengenai Islam, "
    "tidak melalui metode gamelan dan gending Jawa seperti sang ayah, kerap terjadi benturan di sana-sini dengan masyarakat dan bahkan dengan murid-muridnya sendiri di padepokan.\n\n"
    "Setelah sekian lama pulanglah sang Sunan Kudus dari luar daerah. Setelah dia mengetahui bahwa sepeninggal dirinya sang Putra menggunakan metode penyebaran "
    "Islam yang tidak sesuai dengan ajarannya, sang ayah pun murka, diusirnya sang putra dan tidak boleh menginjakkan kaki lagi di Tanah Jawa, dengan maksud agar "
    "sang putra bisa menyebarkan ajaran Islam di daerah yang belum mengenal Islam. Keesokan harinya rakit yang akan membawa Amir Khasan sudah siap dengan beberapa "
    "bekal dari sang ibu, yakni pepes ikan lele kesukaannya, seikat padi, mustaka (Puncak bangunan) Masjid dari bahan tanah liat, serta tongkat kesayangan ayahnya.\n\n"
    "Sang ibu dengan derai air mata mengantarkan sang anak yang sudah menyusuri sungai dengan rakitnya. Berhari-hari sang ibu menyusuri sungai hingga pada suatu hari "
    "tibalah sang rakit di muara sungai dan rakit pun terbawa arus ke tengah laut. Sang ibu dengan bersusah payah menaiki bukit untuk melihat rakit anaknya, hingga "
    "terlihatlah rakit di kejauhan dan terlihat pula dengan samar-samar daratan dengan gunung. Sang Ibu pun memerintahkan muridnya untuk melaporkan kepada Sunan Kudus "
    "bahwa sang putra menuju daratan bergunung itu, namun sang murid dalam memberikan laporan salah ucap bahwa putra Kanjeng Sunan berada jauh di tengah laut menuju "
    "daratan atau gunung yang tampak kremun-kremun (samar-samar), dari situlah sang Sunan mendoakan putranya agar sampai “Karimunjawa” dengan selamat, dan beredarlah "
    "berita bahwa Amir Khasan sedang berdakwah ke Karimunjawa. Dan mulai saat itulah daratan itu dinamai Karimunjawa.\n\n"
)

# Menambahkan label untuk teks
paragraph_label_1 = customtkinter.CTkLabel(
    my_frame,
    text=text_karimunjawa_1,
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_1.pack(padx=50, pady=20)

image2_path = r"D:\KENNARD\lomba\build\assets\frame0\kimg2.jpg"  # Ganti dengan path gambar kedua Anda
image2 = Image.open(image2_path)
image2 = image2.resize((600, 400))  # Sesuaikan ukuran gambar
photo2 = ImageTk.PhotoImage(image2)

# Menambahkan label untuk gambar kedua
image2_label = customtkinter.CTkLabel(my_frame, image=photo2, text="")
image2_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Perjalanan Menuju Karimun Jawa",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))

text_karimunjawa_2 = (
    "Raungan deru mesin KMP Muria memecah keheningan di dermaga yang terletak di kawasan objek wisata"
    "pantai Kartini itu seolah menyiratkan lelah dan bosan yang teramat sangat dari kMP Muria yang sudah"
    "tampak tua. Setiap hari yang dilihat adalah laut, dermaga Karimunjawa dan dermaga pantai Kartini. Kedua dermaga tempat dia akan berlabuh untuk menaik-turunkan para penumpang.\n\n"
    "Cuaca pagi itu cukup cerah, begitu pula dengan para penumpang yang berada di kapal. Jumlahnya kala itu tidak terlalu banyak, mungkin kurang dari kapasitas maksimal kapal yang berjumlah sekitar 200 an penumpang sekali angkut.\n\n"
    "Awalnya, semua masih terlihat gembira bahkan ada serombongan remaja dengan gaya-gaya kocak dan sedikit noraknya sedang asik berfoto-foto. Namun begitu waktu menginjak pada jam-jam ketiga para penumpang di atas kapal semua sudah mulai terlihat bosan dan jenuh.\n\n"
    "Setelah 4 jam membunuh bosan di kapal KMP Muria, di kejauhan daratan dengan bukit-bukit yang hijau mulai terlihat Kremun-kremun alias samar-samar. Ya, itulah Pulau Karimunjawa.\n\n"
    "Sebuah gugusan pulau-pulau berjumlah 27 pulau. Di antara pulau-pulau tersebut, sebanyak 5 pulau berpenghuni, yaitu: Pulau Karimunjawa, Pulau Genting, Pulau Kemujan, Pulau Nyamuk dan Pulau Parang.\n\n"
    "Tak berselang lama, kapal KMP Muria yang saya tumpangi mulai merapat. Air laut di sekitar dermaga ini jernih sekali, hingga saya bisa melihat ganggang yang tumbuh di dasar laut. Bukit-bukit hijau nan memuka dengan latar belakang langit biru dan awan putih seolah berarak menyambut kedatangan kami kala itu.\n\n"
    "Lelah, bosan dan penah yang terakumulasi selama 6 jam di kapal rasanya langsung hilang. Justru semangat yang kian membara untuk segera menyeburkan diri di beningnya air laut itu. Tepat pukul 15.30, saya pun menginjakkan kaki di Karimun Jawa."
)

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text=text_karimunjawa_2,
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,40))

image3_path = r"D:\KENNARD\lomba\build\assets\frame0\kimg3.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Rekomendasi Tempat Wisata di Karimun Jawa",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))

image3_path = r"D:\KENNARD\lomba\build\assets\frame0\kimg4.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Pantai Tanjung Gelam",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=220, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Pantai ini terkenal dengan pasir putihnya yang lembut dan air laut yang jernih. Pemandangan matahari terbenam di sini sangat memukau, menjadikannya spot favorit bagi wisatawan untuk menikmati sunset.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)


# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))





image3_path = r"D:\KENNARD\lomba\build\assets\frame0\kimg5.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Pulau Menjangan Kecil",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=220, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Pulau ini menawarkan pengalaman snorkeling yang luar biasa dengan keanekaragaman terumbu karang dan biota laut yang indah. Airnya yang jernih memungkinkan wisatawan melihat keindahan bawah laut dengan jelas.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))




image3_path = r"D:\KENNARD\lomba\build\assets\frame0\kimg6.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Bukit Love",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=220, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Dari bukit ini, Anda dapat menikmati panorama Karimunjawa dari ketinggian. Terdapat monumen bertuliskan 'Love' yang menjadi spot foto populer bagi pengunjung.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))



paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Source: lostpacker.com, Kompas Travel",
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
