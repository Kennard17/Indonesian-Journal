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
    text="Keunikan Tanah Toraja",
    font=("Arial", 40, "bold"),  # Menggunakan gaya bold
    text_color='#242322',
)
title_label.pack(pady=(30,15)) 

image_path = r"D:\KENNARD\lomba\build\assets\frame0\timg1.jpg"  # Ganti dengan path gambar Anda
image = Image.open(image_path)
image = image.resize((600, 400))  # Sesuaikan ukuran gambar
photo = ImageTk.PhotoImage(image)

# Menambahkan label untuk gambar
image_label = customtkinter.CTkLabel(my_frame, image=photo, text="")
image_label.pack(pady=20)

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Asal Usul Suku Toraja",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(30,15))

# Teks cerita
text_1 = (
    "Asal usul Suku Toraja berasal dari Teluk Tonkin yang terletak di antara Vietnam Utara dan Cina Selatan. Awalnya, imigran asal Teluk Tonkin ini tinggal di wilayah pantai yang ada di Sulawesi, namun mereka pindah ke dataran tinggi yang sampai saat ini masih didiami oleh Suku Toraja.\n\n"
    "Disebutkan juga bahwa masyarakat yang mendiami Tana Toraja ini adalah hasil percampuran dari penduduk lokal yang memang tinggal di dataran tinggi Sulawesi Selatan dengan para imigran dari Teluk Tongkin-Yunnan, Cina Selatan. Mereka berlabuh di sekitar hulu sungai, yakni daerah Enrekang, kemudian membangun permukiman.\n\n"
    "Asal usul dari Suku Toraja ini juga memiliki mitos tersendiri yang sangat melegenda. Konon, leluhur dari Suku Toraja merupakan manusia yang berasal dari nirwana. Masyarakat Toraja percaya bahwa nenek moyang mereka turun dari langit dengan tangga yang berfungsi sebagai alat komunikasi dengan Puang Matua (Tuhan).\n\n"
    "Kata Toraja sendiri memiliki asal usul. Orang Bugis menyebut Toraja sebagai to riaja yang berarti orang yang berdiam di negeri atas. Orang Luwu menyebutnya sebagai to riajang yang berarti orang yang berdiam di sebelah barat. Sementara pendapat lain menyebutkan bahwa toraja berasal dari dua kata yakni to yang artinya orang dan maraya yang artinya besar/bangsawan.\n\n"
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

image2_path = r"D:\KENNARD\lomba\build\assets\frame0\timg2.jpg"  # Ganti dengan path gambar kedua Anda
image2 = Image.open(image2_path)
image2 = image2.resize((600, 400))  # Sesuaikan ukuran gambar
photo2 = ImageTk.PhotoImage(image2)

# Menambahkan label untuk gambar kedua
image2_label = customtkinter.CTkLabel(my_frame, image=photo2, text="")
image2_label.pack(pady=(0,50)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Kebudayaan Suku Toraja",
    font=("Arial", 20, "bold"),  # Menggunakan gaya bold
    text_color='grey',
)
title_label.pack(pady=(0,15))


image3_path = r"D:\KENNARD\lomba\build\assets\frame0\timg3.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Rambu Solo",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=220, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Salah satu tradisi khas dari Suku Toraja adalah Rambu Solo' atau dikenal dengan istilah Auk Rampe Matampu. Rambu Solo' adalah tradisi upacara pemakaman yang dilaksanakan masyarakat Toraja untuk menghormati dan mengantarkan arwah menuju kehidupan selanjutnya. Masyarakat Toraja menganggap orang yang sudah meninggal telah benar-benar meninggal jika seluruh kebutuhan prosesi upacara Rambu Solo terpenuhi. Jika upacara ini belum dilakukan, maka keluarga akan memperlakukannya layaknya orang sakit, sehingga harus disediakan makanan, minuman, dan dibaringkan di tempat tidur. Tradisi ini dilakukan melalui serangkaian ritual dan doa yang dilaksanakan dengan pertunjukan seni, penyembelihan babi atau kerbau, dan kemudian mengantarkan jenazah ke tempat peristirahatan terakhirnya.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)


# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))





image3_path = r"D:\KENNARD\lomba\build\assets\frame0\timg4.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Tradisi Ma'nene",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=220, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Tradisi Ma'nene adalah ritual untuk membersihkan dan mengganti pakaian dari mayat yang sudah berusia puluhan bahkan ratusan tahun. Ritual Ma'nene tidak hanya sekedar ritual untuk membersihkan dan memakaikan baju baru pada jasad para leluhur. Ritual ini adalah gambaran dari pentingnya hubungan antar anggota keluarga bahkan yang sudah meninggal, dan diyakini para leluhur juga akan memberikan timbal balik positif bagi keluarga yang masih hidup. Tradisi Ma'nene menjadi salah satu tradisi yang masih dipertahankan dan dipahami sebagai cara menghormati nenek moyang.",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))




image3_path = r"D:\KENNARD\lomba\build\assets\frame0\timg5.jpg"  # Ganti dengan path gambar kedua Anda
image3 = Image.open(image3_path)
image3 = image3.resize((600, 400))  # Sesuaikan ukuran gambar
photo3 = ImageTk.PhotoImage(image3)

# Menambahkan label untuk gambar kedua
image3_label = customtkinter.CTkLabel(my_frame, image=photo3, text="")
image3_label.pack(pady=(0,20)) 

title_label = customtkinter.CTkLabel(
    my_frame,
    text="Sisemba",
    font=("Arial", 18, "bold"),  # Menggunakan gaya bold
    text_color='black',
    anchor="w",  # Mengatur teks menjadi rata kiri
)
title_label.pack(pady=(0, 5), padx=220, fill="x")

paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Sisemba’ adalah permainan adu kaki yang dilakukan sebagai bentuk rasa syukur dari hasil panen. Permainan ini dilaksanakan di lapangan terbuka dan dapat dilakukan oleh anak-anak maupun orang dewasa. Ada tiga cara permainan tradisional Sisemba yaitu Sisemba Simanuk (satu lawan satu), Sisemba Siduanan (dua lawan dua), dan Sisemba Sikambanan (kelompok lawan kelompok).",
    wraplength=900,  # Lebar dengan margin kiri dan kanan
    justify="left",  # Teks rata kiri
    text_color='black',
    font=("Arial", 16)  # Ukuran font lebih besar
)

# Menempatkan label di dalam frame
paragraph_label_2.pack(padx=50, pady=(0,80))




paragraph_label_2 = customtkinter.CTkLabel(
    my_frame,
    text="Source: Kumparan, Kompas.",
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
