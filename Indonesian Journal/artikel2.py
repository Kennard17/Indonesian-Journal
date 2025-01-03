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
    text="Tradisi Lompat Batu di Pulau Nias",
    font=("Arial", 40, "bold"),  # Menggunakan gaya bold
    text_color='#242322',
)
title_label.pack(pady=(30,15)) 

image_path = r"D:\KENNARD\lomba\build\assets\frame0\nimg1.png"  # Ganti dengan path gambar Anda
image = Image.open(image_path)
image = image.resize((600, 400))  # Sesuaikan ukuran gambar
photo = ImageTk.PhotoImage(image)

# Menambahkan label untuk gambar
image_label = customtkinter.CTkLabel(my_frame, image=photo, text="")
image_label.pack(pady=20)

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Asal Usul dan Sejarah",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(30,15))


# Menambahkan label untuk teks
paragraph_label_1 = customtkinter.CTkLabel(
    my_frame,
    text="Tradisi lompat batu diyakini bermula dari kebiasaan perang antardesa di Nias. Pada masa lalu, desa-desa di Nias dikelilingi oleh benteng batu untuk pertahanan. Pemuda yang mampu melompati benteng tersebut dianggap siap menjadi prajurit dan melindungi desa mereka. Kemampuan melompati batu menjadi tolok ukur keberanian dan kedewasaan seorang pria Nias.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_1.pack(padx=50, pady=(10,50))



title_label = customtkinter.CTkLabel(
    my_frame,
    text="Makna dan Simbolisme",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))


paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Lompat batu melambangkan transisi dari masa remaja ke dewasa serta kesiapan seorang pria untuk menikah. Selain itu, tradisi ini mencerminkan nilai-nilai keberanian, kekuatan, dan keterampilan yang dihormati dalam budaya Nias. Saat ini, lompat batu juga menjadi daya tarik wisata yang memperkenalkan kekayaan budaya Nias kepada dunia.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)


# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))


title_label = customtkinter.CTkLabel(
    my_frame,
    text="Pelaksanaan Tradisi",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))


paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Sebelum melakukan lompat batu, peserta menjalani latihan intensif untuk membangun kekuatan dan keterampilan yang diperlukan. Mereka juga mengikuti serangkaian ritual adat yang melibatkan doa dan pemberian sesajian untuk mendapatkan berkat dan perlindungan dari leluhur. Lompat batu biasanya dilakukan dalam acara-acara adat dan festival budaya, di mana masyarakat berkumpul untuk menyaksikan dan memberikan dukungan kepada peserta.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)


# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))






paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Source: Kumparan, Kompas.com, Liputan6.",
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
