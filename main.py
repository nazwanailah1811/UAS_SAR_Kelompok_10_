import logging
from models.missing_person import MissingPerson
from models.rescuer import LandRescuer, WaterRescuer, AirRescuer
from repositories.missing_person_repository import MissingPersonRepository
from services.sar_service import SARService

logging.basicConfig(level=logging.INFO)

repo = MissingPersonRepository()
service = SARService(repo)


def menu():
    """Menampilkan menu utama aplikasi"""
    print("\n=== SISTEM PUSAT DATA ORANG HILANG & SAR ===")
    print("1. Tambah Orang Hilang")
    print("2. Lihat Data Orang Hilang")
    print("3. Operasi SAR")
    print("4. Update Status Korban (ditemukan/Lokasi)")
    print("5. Hapus Data Korban")
    print("0. Keluar")


while True:
    menu()
    pilih = input("Pilih menu: ")

    if pilih == "1":
        orang = MissingPerson(
            input("ID: "),
            input("Nama: "),
            int(input("Umur: ")),
            input("Jenis Kelamin: "),
            input("Lokasi Terakhir: ")
        )

        orang.set_height(int(input("Tinggi Badan (cm): ")))
        orang.set_special_mark(input("Ciri khusus: "))

        service.add_missing_person(orang)

    elif pilih == "2":
        for o in service.get_all_missing():
            print(o.get_info())

    elif pilih == "3":
        data = service.get_all_missing()
        if not data:
            print("Belum ada data orang hilang.")
        else:
            # 1. Pilih target (orang yang dicari)
            target = data[0] 
            
            # 2. Tambahkan sub-menu untuk memilih jenis tim
            print("\nPilih Jenis Tim SAR:")
            print("1. Tim Darat")
            print("2. Tim Air")
            print("3. Tim Udara")
            pilihan_tim = input("Pilih (1-3): ")

            # 3. Logika penentuan tim berdasarkan input
            if pilihan_tim == "1":
                tim = LandRescuer("T01", "Macan")
            elif pilihan_tim == "2":
                tim = WaterRescuer("T02", "Hiu")
            elif pilihan_tim == "3":
                tim = AirRescuer("T03", "Elang")
            else:
                print("Pilihan tim tidak valid!")
                continue # Kembali ke menu utama

            # 4. Jalankan pencarian
            print("\n--- Memulai Operasi ---")
            print(tim.search(target))
            
            target.set_status("Ditemukan")
            logging.info(f"Operasi SAR untuk {target.get_name()} selesai")

    elif pilih == "4":
        id_cari = input("Masukkan ID Korban yang ingin diupdate: ")
        print("Pilih Status Baru:")
        print("1. Ditemukan")
        print("2. Meninggal")
        print("3. Masih Hilang")
        
        status_map = {"1": "Ditemukan", "2": "Meninggal", "3": "Hilang"}
        pilihan_status = input("Pilih (1-3): ")
        
        if pilihan_status in status_map:
            status_baru = status_map[pilihan_status]
            lokasi_baru = input("Update lokasi saat ini (kosongkan jika tidak ada): ")
            berhasil = service.update_status(id_cari, status_baru, lokasi_baru if lokasi_baru else None)
            
            if berhasil:
                print("Data berhasil diperbarui!")
            else:
                print("Gagal: ID tidak terdaftar.")
        else:
            print("Pilihan status tidak valid.")
    
    elif pilih == "5":
        id_hapus = input("Masukkan ID Korban yang ingin dihapus: ")
        print(f"PERINGATAN: Data dengan ID {id_hapus} akan dihapus permanen.")
        konfirmasi = input("Apakah Anda yakin? (y/n): ")
        
        if konfirmasi.lower() == 'y':
            berhasil = service.delete_missing_person(id_hapus)
            if berhasil:
                print("Data berhasil dihapus dari pusat data.")
            else:
                print("Gagal: Data tidak ditemukan.")
        else:
            print("Penghapusan dibatalkan.")

    elif pilih == "0":
        print("Program selesai.")
        break