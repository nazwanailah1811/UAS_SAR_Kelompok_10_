## Anggota Kelompok 10
1. Tri Wahyu Widyastuti (2411102441172)
2. Nazwa Nailah (2411102441169)
3. Hilwa Amalia Rosalba Salik (2411102441034)
4. Putri Molida (2411102441141)
5. Gabrilla Aszahra Samad(2411102441174)
6. Nabiilah (2411102441202)
7. Raisyi Salsabila (2411102441210)

# Pusat Data Orang Hilang & SAR (SAR Data Center)

Proyek ini adalah sistem manajemen data orang hilang dan koordinasi tim SAR (Search and Rescue) yang dibangun dengan prinsip pemrograman berorientasi objek (OOP). Sistem ini dirancang untuk mempermudah pendataan, pemantauan status korban, serta simulasi penugasan tim penyelamat.

## Fitur Utama
- **Manajemen Data (CRUD):** Tambah, lihat, perbarui status, dan hapus data orang hilang secara terorganisir.
- **Update Status Real-time:** Memungkinkan pembaruan lokasi terakhir dan status korban (Hilang/Ditemukan/Meninggal).
- **Simulasi Operasi SAR:** Fitur penugasan tim SAR (Darat, Air, Udara) menggunakan konsep Polymorphism.
- **Logging System:** Pencatatan otomatis setiap aktivitas penting (tambah data, update, delete) ke dalam sistem log.

## Arsitektur & Prinsip Desain
Proyek ini menerapkan standar pengembangan perangkat lunak modern:
- SOLID Principles: - Single Responsibility: Tiap kelas memiliki tanggung jawab spesifik (Model, Repository, Service).
                    - Dependency Inversion: Bergantung pada abstraksi (Interface), bukan implementasi konkret.
- Repository Pattern:Memisahkan logika penyimpanan data dari logika bisnis.
- Service Layer: Sebagai jembatan antara antarmuka pengguna (CLI) dan penyimpanan data.
- Encapsulation: Penggunaan atribut privat (__private) untuk menjaga integritas data.
- Abstraction & Polymorphism: Penggunaan Abstract Base Class (ABC) untuk blueprint manusia dan tim penyelamat.

## Cara Menjalakankan
1. Pastikan Anda memiliki Python 3.x terinstal.
2. Clone repository ini.
3. Jalankan aplikasi melalui terminal:
**python main.py**

## Struktur Folder
```text
.
├── models/
│   ├── person.py           # Abstract class untuk data person
│   ├── missing_person.py   # Implementasi data orang hilang
│   └── rescuer.py          # Abstract class & jenis tim SAR
├── repositories/
│   ├── base_repository.py  # Interface repository
│   └── missing_person_repository.py # Implementasi penyimpanan
├── services/
│   ├── sar_service_interface.py # Interface layanan SAR
│   └── sar_service.py      # Logika bisnis utama
├── utils/
│   ├── logger.py           # Konfigurasi logging
│   └── time_utils.py       # Helper untuk format waktu
└── main.py                 # Entry point aplikasi (CLI)

