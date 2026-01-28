import os

class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def kapasitas(self):
        os.system("cls")
        try:
            x = int(input("Masukan jumlah kapasitas pada antrian  : "))
            self.size = x
            print("Sebuah antrian dibuat dengan kapasitas :", x)
        except ValueError:
            print("Input harus berupa angka.")
        print("\nTekan [enter] untuk kembali ke halaman menu...")
        input()
        self.menu()

    def is_empty(self):
        return len(self.items) == 0
        
    def is_full(self):
        return len(self.items) >= self.size

    def tambah_antrian(self, x):
        if self.is_full():
            print("Antrian penuh. Tidak bisa menambah antrian baru.")
        else:
            self.items.append(x)  # Tambahkan elemen di belakang
            print("                                                        ")
            print("========================================================")
            print(f"|  Nomor antrian {x} telah ditambahkan ke dalam antrian  |")
            print("========================================================")
        print("\nTekan [enter] untuk kembali ke halaman menu...")
        input()
        self.menu()

    def keluarkan_antrian(self):
        if self.is_empty():
            print("Antrian masih kosong. Silahkan tambah antrian terlebih dahulu pada menu pilihan tambah antrian")
        else:
            removed = self.items.pop(0)  # Keluarkan elemen dari depan
            print(f"Mengeluarkan nomor antrian {removed} dari antrian")
        print("\nTekan [enter] untuk kembali ke halaman menu...")
        input()
        self.menu()

    def status(self):
        print("Kapasitas Antrian            :", self.size)
        print("Banyaknya antrian            :", len(self.items))
        if self.is_empty():
            print("Antrian pada posisi terdepan : Tidak ada")
            print("Antrian pada posisi terakhir : Tidak ada")
        else:
            print("Antrian pada posisi terdepan :", self.items[0])
            print("Antrian pada posisi terakhir :", self.items[-1])
        print("Isi list data                :", self.items)
        print("\nTekan [enter] untuk kembali ke halaman menu...")
        input()
        self.menu()

    def visualisasi_data(self):
        if self.is_empty():
            print("Antrian kosong. Silahkan tambahkan antrian terlebih dahulu pada menu tambah antrian")
        else:
            for i in range(self.size):
                print(f"    [{i+1:2d}]    ", end="")
            print()

            for i in range(self.size):
                print("---------------", end="")
            print()

            for i in range(self.size):
                if i < len(self.items):
                    print(" %10s " % (self.items[i]), end="")
                else:
                    print(" %10s " % (""), end="")

            print(">> [BELAKANG]", end="")
            print()

            for i in range(self.size):
                print("---------------", end="")

        print("\nTekan [enter] untuk kembali ke halaman menu...")
        input()
        self.menu()

    def hitung_antrian_kosong(self):
        jumlah_kosong = self.size - len(self.items)
        print(f"Jumlah antrian kosong : {jumlah_kosong}")
        print("\nTekan [enter] untuk kembali ke halaman menu...")
        input()
        self.menu()

    def menu(self):
        os.system("cls")
        print("=========================================================")
        print("|                 ANTRIAN WAHANA BERMAIN                |")
        print("=========================================================")
        print("| 1. Daftar Antrian                                     |")
        print("| 2. Status Antrian                                     |")
        print("| 3. Tambah Antrian                                     |")
        print("| 4. Keluarkan Antrian Terdepan                         |")
        print("| 5. Menghitung Banyaknya Antrian Kosong                |")
        print("| 6. Keluar dari Program Antrian                        |")
        print("=========================================================")
        pilihan = input("Silahkan masukan menu pilihan anda : ")

        if pilihan == "1":
            os.system("cls")
            print("=====================================================")
            print("|          DAFTAR ANTRIAN WAHANA BERMAIN            |")
            print("=====================================================")
            self.visualisasi_data()
        elif pilihan == "2":
            os.system("cls")
            print("================================================")
            print("|     Anda berada pada menu status antrian     |")
            print("================================================")
            self.status()
        elif pilihan == "3":
            os.system("cls")
            print("========================================================")
            print("|        Anda berada pada menu tambah antrian          |")
            print("========================================================")
            print("                                                        ") 
            x = input("Masukan nomor antrian yang ingin ditambahkan : ")

            while x == "":
                os.system("cls")
                print("Inputan tidak boleh kosong!")
                print("Masukan antrian dengan benar!")
                x = input("\n Masukkan nomor antrian yang ingin ditambahkan : ")
            self.tambah_antrian(x)

        elif pilihan == "4":
            os.system("cls")
            print("================================================")
            print("|    Anda berada pada menu keluarkan antrian   |")
            print("================================================")
            self.keluarkan_antrian()
        elif pilihan == "5":
            os.system("cls")
            print("=================================================")
            print("|  Anda berada pada menu banyak antrian kosong  |")
            print("=================================================")
            self.hitung_antrian_kosong()
        elif pilihan == "6":
            os.system("cls")
            self.keluar()
        else:
            os.system("cls")
            print("Pilihan tidak valid. Silahkan coba lagi.")
            input("Tekan [enter] untuk kembali ke menu...")
            input()
            self.menu()

    def keluar(self):
        print("Anda akan keluar dari program...")
        input()
        quit()

if __name__ == "__main__":
    q = Queue()
    q.kapasitas()

