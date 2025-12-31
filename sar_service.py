import logging
from services.sar_service_interface import ISARService


class SARService(ISARService):
    """
    Implementasi service SAR.
    Menghubungkan repository dan aplikasi utama.
    """

    def __init__(self, repository):
        self.repository = repository

    def add_missing_person(self, person):
        """Menambahkan data orang hilang ke repository"""
        self.repository.add(person)
        logging.info(f"Data orang hilang ditambahkan: {person.get_name()}")

    def get_all_missing(self):
        """Mengambil seluruh data orang hilang"""
        return self.repository.get_all()

    def update_status(self, id_person, new_status, new_location=None):
        """Logika untuk mengupdate status dan lokasi person"""
        person = self.repository.get_by_id(id_person)
        if person:
            person.set_status(new_status)
            if new_location:
                person.update_location(new_location)
            logging.info(f"Update berhasil: {person.get_name()} status sekarang {new_status}")
            return True
        logging.warning(f"Update gagal: ID {id_person} tidak ditemukan")
        return False
    
    def delete_missing_person(self, id_person):
        """Logika untuk menghapus data melalui repository"""
        # Kita ambil datanya dulu untuk mendapatkan nama sebelum dihapus dari list
        person = self.repository.get_by_id(id_person)
        
        if person:
            nama_terdaftar = person.get_name() # Mengambil nama asli dari object
            success = self.repository.delete(id_person)
            
            if success:
                # Menampilkan nama yang diambil tadi ke dalam log
                logging.info(f"Data {nama_terdaftar} telah dihapus dari sistem.")
                return True
                
        logging.warning(f"Gagal menghapus: ID {id_person} tidak ditemukan.")
        return False