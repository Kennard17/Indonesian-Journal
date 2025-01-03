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
    text="Panduan Pendakian Gunung Rinjani",
    font=("Arial", 40, "bold"),  # Menggunakan gaya bold
    text_color='#242322',
)
title_label.pack(pady=(30,15)) 

image_path = r"D:\KENNARD\lomba\build\assets\frame0\rimg1.jpg"  # Ganti dengan path gambar Anda
image = Image.open(image_path)
image = image.resize((600, 400))  # Sesuaikan ukuran gambar
photo = ImageTk.PhotoImage(image)

# Menambahkan label untuk gambar
image_label = customtkinter.CTkLabel(my_frame, image=photo, text="")
image_label.pack(pady=20)

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Pos Yang Akan Dilewati",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(30,15))

# Teks cerita
text_1 = (
    "Pos 1 (1.300 m): Pos ini menawarkan pemandangan sabana yang luas dan sering dijadikan tempat istirahat pertama. Medannya relatif landai dan cocok untuk pemanasan. \n\n"
    "Pos 2 (1.500 m): Di pos ini, kamu akan mulai merasakan medan yang lebih menanjak. Pemandangan sekitar masih didominasi oleh sabana dengan beberapa pohon besar.\n\n"
    "Pos 3 (1.800 m): Pos ini memiliki medan yang semakin menanjak dan lebih berat dibandingkan pos sebelumnya. Pemandangan sabana mulai berganti dengan hutan tropis.\n\n"
    "Pelawangan Sembalun (2.639 m): Pelawangan Sembalun adalah tempat perkemahan sebelum melakukan summit attack ke puncak Rinjani. Di sini, kamu bisa menikmati pemandangan spektakuler Danau Segara Anak dan puncak Rinjani.\n\n"
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
paragraph_label_1.pack(padx=50, pady=20)

image2_path = r"D:\KENNARD\lomba\build\assets\frame0\rimg2.jpg"  # Ganti dengan path gambar kedua Anda
image2 = Image.open(image2_path)
image2 = image2.resize((600, 400))  # Sesuaikan ukuran gambar
photo2 = ImageTk.PhotoImage(image2)

# Menambahkan label untuk gambar kedua
image2_label = customtkinter.CTkLabel(my_frame, image=photo2, text="")
image2_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Biaya Pendakian Gunung Rinjani",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))

text_2 = (
    "1. Izin Pendakian (Simaksi): Tarif simaksi untuk pendaki domestik sebesar Rp5.000 per hari untuk weekdays, dan tarif Rp7.500 per hari untuk hari libur. Sedangkan untuk pendaki asing dikenakan tarif sekitar Rp150.000/hari (weekday) dan hari libur sebesar Rp250.000/hari per orang. Tarif ini tergantung pada kebijakan yang berlaku.\n\n"
    "2. Surat Keterangan Sehat: Pendaki wajib menyerahkan surat keterangan sehat dengan biaya sekitar Rp20.000.\n\n"
    "3. Transportasi menuju basecamp: Biaya transportasi umum (bus, kapal, kereta, pesawat, dll) menuju Lombok tergantung dari tempat keberangkatan masing-masing. Biaya transportasi dari bandara atau kota terdekat ke Sembalun menggunakan rental mobil berkisar antara Rp300.000 – Rp500.000.\n\n"
    "4. Guide dan Porter: Untuk keselamatan dan kenyamanan selama pendakian, disarankan untuk menyewa guide dan porter. Biaya guide sekitar Rp250.000 – Rp350.000 per hari, sedangkan porter sekitar Rp150.000 – Rp250.000 per hari. DI luar itu, kamu bisa memberikan tip tambahan sebagai ucapan terima kasih terhadap jasa mereka.\n\n"
    "5. Perlengkapan Pendakian: Jika tidak membawa perlengkapan sendiri, kamu bisa menyewanya di area basecamp dengan biaya sekitar Rp500.000 – Rp1.000.000. \n\n"
    "6. Makanan dan Minuman: Siapkan budget sekitar Rp200.000 – Rp300.000 untuk persediaan makanan dan minuman selama beberapa hari pendakian.\n\n"
    "7. Biaya Lain-Lain: Persiapkan juga biaya lain-lain selama pendakian, meliputi biaya obat-obatan, dana darurat, oleh-oleh, dan lainnya.\n\n"
    "Secara keseluruhan, estimasi biaya mendaki Rinjani via Sembalun bisa mencapai Rp2.000.000 – Rp3.000.000 per orang. Biaya ini bisa bervariasi tergantung pada kebutuhan dan preferensi masing-masing."
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

image3_path = r"D:\KENNARD\lomba\build\assets\frame0\rimg3.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Tips Pendakian Gunung Rinjani",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))



text_2 = (
    "1. Manfaatkan Sabana untuk Pemanasan: Jalur Sembalun dimulai dengan medan sabana yang landai. Manfaatkan medan pendakian ini untuk pemanasan dan menyesuaikan ritme pendakianmu.\n\n"
    "2. Istirahat di Pelawangan Sembalun: Pelawangan Sembalun adalah tempat yang ideal untuk camping sebelum melakukan summit attack Rinjani. Nikmati camping sembari berhadapan langsung dengan pemandangan indah Danau Segara Anak dan persiapkan dirimu kembali untuk pendakian ke puncak.\n\n"
    "3. Persiapkan Diri untuk Summit Attack: Trek dari Pelawangan Sembalun ke puncak sangat menantang dengan medan curam dan berpasir. Pastikan kamu membawa headlamp, pakaian hangat, dan memulai pendakian dini hari untuk menghindari cuaca ekstrem.\n\n"
    "4. Jaga Kebersihan dan Kelestarian Alam: Jalur Sembalun terkenal dengan keindahan alamnya. Pastikan kamu tidak membuang sampah sembarangan di gunung, bawa turun kembali sampahmu, dan selalu menjaga kebersihan lingkungan.\n\n"
    "5. Sesuaikan Kecepatan dan Ritme: Setiap pendaki memiliki stamina dan kecepatan yang berbeda. Jangan ragu untuk beristirahat jika merasa lelah dan selalu utamakan keselamatan.\n\n"
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
    text="Source: Eiger Adventure",
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
