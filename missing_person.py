from models.person import Person
from utils.time_utils import current_time


class MissingPerson(Person):
    """
    Representasi orang hilang dalam sistem SAR.
    Turunan dari class Person.
    """

    def __init__(self, id_person, name, age, gender, last_location):
        """
        Inisialisasi data orang hilang.

        :param id_person: ID unik orang
        :param name: nama
        :param age: umur
        :param gender: jenis kelamin
        :param last_location: lokasi terakhir terlihat
        """
        super().__init__(name, age)

        self.__id_person = id_person
        self.set_gender(gender)

        self.__last_location = last_location
        self.__status = "Hilang"

        # tambahan informasi
        self.__special_mark = None
        self.__reported_time = current_time()

    def get_id(self):
        """Mengembalikan ID orang"""
        return self.__id_person

    def get_status(self):
        """Mengambil status pencarian"""
        return self.__status

    def set_status(self, status):
        """
        Mengubah status orang hilang.

        Status yang diperbolehkan:
        - Hilang
        - Ditemukan
        - Meninggal
        """
        if status not in ["Hilang", "Ditemukan", "Meninggal"]:
            raise ValueError("Status tidak valid")
        self.__status = status

    def update_location(self, location):
        """Memperbarui lokasi terakhir"""
        self.__last_location = location

    def set_special_mark(self, mark):
        """Menyimpan ciri khusus orang"""
        self.__special_mark = mark

    def get_special_mark(self):
        """Mengambil ciri khusus"""
        return self.__special_mark

    def get_reported_time(self):
        """Mengambil waktu pelaporan"""
        return self.__reported_time

    def get_info(self):
        """
        Implementasi polymorphism:
        Mengembalikan informasi lengkap orang hilang.
        """
        return (
            f"ID: {self.__id_person}\n"
            f"Nama: {self.get_name()}\n"
            f"Umur: {self.get_age()}\n"
            f"JK: {self.get_gender()}\n"
            f"Tinggi: {self.get_height()} cm\n"
            f"Lokasi Terakhir: {self.__last_location}\n"
            f"Ciri Khusus: {self.__special_mark}\n"
            f"Status: {self.__status}\n"
            f"Waktu Lapor: {self.__reported_time}\n"
        )
