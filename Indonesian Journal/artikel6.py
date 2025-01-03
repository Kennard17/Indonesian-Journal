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
    text="Peninggalan Kolonial di\nPulau Nusakambangan",
    font=("Arial", 40, "bold"),  # Menggunakan gaya bold
    text_color='#242322',
)
title_label.pack(pady=(30,15)) 

image_path = r"D:\KENNARD\lomba\build\assets\frame0\pimg1.jpg"  # Ganti dengan path gambar Anda
image = Image.open(image_path)
image = image.resize((600, 400))  # Sesuaikan ukuran gambar
photo = ImageTk.PhotoImage(image)

# Menambahkan label untuk gambar
image_label = customtkinter.CTkLabel(my_frame, image=photo, text="")
image_label.pack(pady=20)

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Tentang Pulau Nusakambangan",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(30,15))


# Menambahkan label untuk teks
paragraph_label_1 = customtkinter.CTkLabel(
    my_frame,
    text="Pulau Nusakambangan adalah sebuah pulau di provinsi Jawa Tengah, Indonesia, yang terletak di sebelah selatan Kota Cilacap. Pulau ini sering dikenal sebagai 'Pulau Penjara' karena terdapat beberapa lembaga pemasyarakatan (lapas) dengan tingkat keamanan tinggi di sana. Nusakambangan memiliki reputasi sebagai tempat tahanan bagi narapidana yang menjalani hukuman berat, termasuk hukuman mati.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_1.pack(padx=50, pady=(10,50))


title_label = customtkinter.CTkLabel(
    my_frame,
    text="Peninggalan Kolonial",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))


image3_path = r"D:\KENNARD\lomba\build\assets\frame0\pimg2.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Benteng Karangbolong",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=145, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Terletak di ujung timur Pulau Nusakambangan, benteng ini dibangun oleh Belanda sebagai pertahanan pantai. Meskipun usianya sudah tua, struktur benteng ini masih berdiri kokoh dan menjadi saksi bisu sejarah kolonial di Indonesia.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)


# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))





image3_path = r"D:\KENNARD\lomba\build\assets\frame0\pimg3.jpeg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Benteng Pendem Cilacap",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=155, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Meskipun secara geografis berada di daratan Cilacap, benteng ini memiliki keterkaitan dengan Pulau Nusakambangan. Dibangun oleh Tentara Kerajaan Belanda antara tahun 1861–1879, benteng ini berfungsi sebagai markas pertahanan pantai selatan Pulau Jawa. Struktur benteng mencakup parit, barak, klinik, gudang amunisi, dan terowongan yang digunakan untuk strategi pertahanan",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))




image3_path = r"D:\KENNARD\lomba\build\assets\frame0\pimg4.jpeg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Gua-gua Belanda dan Pos Intai Kapal",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=150, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Di Pulau Nusakambangan terdapat gua-gua yang digunakan oleh Belanda sebagai tempat penyimpanan amunisi dan pos pengintaian kapal. Gua-gua ini menunjukkan strategi pertahanan Belanda dalam mengawasi perairan sekitar pulau.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))


image3_path = r"D:\KENNARD\lomba\build\assets\frame0\pimg5.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Benteng Klingker (Fort Banjoenjapa)",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=150, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Benteng ini merupakan bangunan megah peninggalan Belanda yang tersembunyi di tengah semak Pulau Nusakambangan. Dibangun pada abad ke-19, benteng ini menjadi bagian dari jaringan pertahanan Belanda di wilayah tersebut.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))



paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Source: Tribun Banyumas",
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
