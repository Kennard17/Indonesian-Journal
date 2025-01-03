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
    text="Pendakian Gunung Terpanjang\n Se-Asia Tenggara",
    font=("Arial", 40, "bold"),  # Menggunakan gaya bold
    text_color='#242322',
)
title_label.pack(pady=(30,15)) 

image_path = r"D:\KENNARD\lomba\build\assets\frame0\limg1.jpg"  # Ganti dengan path gambar Anda
image = Image.open(image_path)
image = image.resize((600, 400))  # Sesuaikan ukuran gambar
photo = ImageTk.PhotoImage(image)

# Menambahkan label untuk gambar
image_label = customtkinter.CTkLabel(my_frame, image=photo, text="")
image_label.pack(pady=20)

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Tentang Gunung Leuser",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(30,15))

# Teks cerita
text_1 = (
    "Gunung Leuser, dengan ketinggian sekitar 3.404 meter di atas permukaan laut, merupakan salah satu puncak tertinggi di Sumatera dan bagian dari Taman Nasional Gunung Leuser yang kaya akan keanekaragaman hayati. Pendakian ke puncak Gunung Leuser menawarkan tantangan yang signifikan, termasuk medan yang berat, cuaca yang tidak menentu, dan durasi pendakian yang panjang, seringkali memakan waktu antara satu hingga dua minggu."
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

image2_path = r"D:\KENNARD\lomba\build\assets\frame0\limg2.jpg"  # Ganti dengan path gambar kedua Anda
image2 = Image.open(image2_path)
image2 = image2.resize((600, 400))  # Sesuaikan ukuran gambar
photo2 = ImageTk.PhotoImage(image2)

# Menambahkan label untuk gambar kedua
image2_label = customtkinter.CTkLabel(my_frame, image=photo2, text="")
image2_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Rangkaian Pendakian",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))

text_2 = (
    "Hari 1-2: Persiapan dan Awal Pendakian\n Pendakian biasanya dimulai dari desa terakhir, seperti Desa Kedah atau Ketambe. Pada hari-hari awal, pendaki akan melewati hutan hujan tropis yang lebat dengan vegetasi yang rapat. Medan yang dilalui berupa tanjakan dan turunan yang licin, terutama setelah hujan. Penggunaan sepatu dan pakaian yang sesuai, serta membawa tongkat trekking, sangat dianjurkan untuk menjaga keseimbangan dan keselamatan.\n\n"
    "Hari 3-5: Memasuki Kawasan Pegunungan\n Setelah melewati hutan lebat, pendaki akan mulai memasuki area perbukitan dengan pemandangan ilalang tinggi. Jalur pendakian di sini terdiri dari tanjakan dan turunan yang cukup menguras tenaga. Penting untuk menjaga ritme pendakian, melakukan istirahat yang cukup, dan memastikan asupan nutrisi terpenuhi untuk menjaga stamina.\n\n"
    "Hari 6-8: Tantangan Menuju Puncak\n Semakin mendekati puncak, medan menjadi lebih terjal dengan jalur yang menurun tajam dan licin. Vegetasi yang bercampur aduk dan adanya pohon besar yang menghalangi jalur menambah tantangan. Pendaki harus ekstra hati-hati dan disarankan untuk menggunakan jasa pemandu lokal yang berpengalaman, mengingat kompleksitas jalur dan risiko tersesat.\n\n"
    "Hari 9-10: Puncak Gunung Leuser\n Setelah perjalanan panjang, pendaki akan mencapai puncak Gunung Leuser. Dari sini, panorama alam Sumatera yang menakjubkan terbentang luas. Rasa lelah terbayar dengan keindahan yang disaksikan. Namun, pendaki harus tetap waspada terhadap kondisi cuaca yang dapat berubah cepat dan suhu yang dingin di ketinggian.\n\n"
    "Hari 11-14: Perjalanan Kembali\n Perjalanan turun seringkali lebih cepat, namun tetap memerlukan kewaspadaan tinggi. Medan yang licin dan kelelahan dapat meningkatkan risiko cedera. Oleh karena itu, penting untuk menjaga konsentrasi dan tidak terburu-buru. Beberapa pendaki melaporkan waktu total pendakian hingga 17 hari, tergantung kondisi fisik dan cuaca.\n\n"
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

image3_path = r"D:\KENNARD\lomba\build\assets\frame0\limg3.jpeg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Tips Penting Pendakian Gunung Leuser",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))



text_2 = (
    "1. Persiapan Fisik dan Mental: Latihan fisik sebelum pendakian sangat penting untuk menghadapi trek panjang dan melelahkan. Selain itu, persiapan mental diperlukan untuk menghadapi tantangan alam liar.\n\n"
    "2. Perlengkapan: Bawa perlengkapan yang memadai, termasuk pakaian hangat, perlengkapan tidur, dan peralatan memasak. Pastikan juga membawa obat-obatan pribadi dan perlengkapan P3K.\n\n"
    "3. Pemandu Lokal: Menggunakan jasa pemandu lokal yang berpengalaman sangat disarankan untuk navigasi yang aman dan mendapatkan informasi berharga tentang medan dan kondisi terkini.\n\n"
    "4. Izin dan Regulasi: Pastikan untuk mengurus semua izin yang diperlukan sebelum pendakian dan patuhi peraturan yang berlaku di kawasan Taman Nasional Gunung Leuser.\n\n"
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
    text="Source: Eiger Adventure, Atap Negeri, Kompas Travel",
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
