import tkinter as tk  # Mengimpor pustaka tkinter untuk membuat antarmuka GUI
from tkinter import messagebox  # Mengimpor messagebox dari tkinter untuk menampilkan pesan dialog

# Fungsi untuk memvalidasi input, menghitung rata-rata nilai, dan menampilkan prediksi prodi
def hasil_prediksi():
    try:
        total_nilai = 0  # Variabel untuk menyimpan total nilai dari semua mata pelajaran

        # Mengiterasi setiap entry dalam list entries untuk mendapatkan nilai input
        for entry in entries:
            nilai = int(entry.get())  # Mengonversi nilai input dari string ke integer
            if not (0 <= nilai <= 100):  # Memeriksa apakah nilai berada dalam rentang 0-100
                raise ValueError("Nilai harus antara 0 dan 100.")  # Jika tidak, munculkan error
            total_nilai += nilai  # Menambahkan nilai ke total_nilai

        rata_rata = total_nilai / len(entries)  # Menghitung rata-rata nilai dari semua mata pelajaran
        
        # Menentukan prodi berdasarkan rata-rata nilai yang diperoleh
        if rata_rata >= 80:
            prodi = "Teknologi Informasi"
        elif 60 <= rata_rata < 80:
            prodi = "Pendidikan Bahasa"
        elif 50 <= rata_rata < 60:
            prodi = "Pertanian"
        else:
            prodi = "Tidak ada prodi yang cocok"
        
        # Menampilkan hasil prediksi prodi dan rata-rata nilai di label hasil_label
        hasil_label.config(text=f"Prediksi Prodi: {prodi} (Rata-rata: {rata_rata:.2f})")
        
    except ValueError as ve:
        # Menampilkan pesan error jika ada input yang tidak valid (bukan angka atau tidak dalam rentang 0-100)
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat objek utama window aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Memberikan judul pada window
root.geometry("500x600")  # Mengatur ukuran window aplikasi
root.configure(bg="#f0f0f0")  # Mengatur warna latar belakang window

# Membuat label judul aplikasi dan menampilkannya dengan padding atas dan bawah
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)

# Membuat frame sebagai wadah untuk input nilai mata pelajaran dan menampilkannya dengan padding atas dan bawah
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

entries = []  # List untuk menyimpan kotak input nilai
for i in range(10):  # Loop untuk membuat 10 kotak input nilai mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label di grid
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))  # Membuat kotak input untuk nilai
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan kotak input di grid
    entries.append(entry)  # Menambahkan kotak input ke dalam list entries

# Membuat tombol untuk memicu hasil prediksi dan menampilkannya dengan padding atas dan bawah
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)

# Membuat label untuk menampilkan hasil prediksi dan menampilkannya dengan padding atas dan bawah
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)

# Memulai mainloop tkinter untuk menjalankan aplikasi
root.mainloop()
