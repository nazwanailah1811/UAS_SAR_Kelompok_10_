from abc import ABC, abstractmethod


class Person(ABC):
    """
    Kelas abstrak Person sebagai dasar untuk semua jenis orang
    dalam sistem SAR.

    Menyimpan data umum seperti:
    - nama
    - umur
    - jenis kelamin
    - tinggi badan
    """

    def __init__(self, name, age):
        """
        Inisialisasi data dasar seseorang.
        :param name: Nama orang
        :param age: Umur orang
        """
        self.__name = name
        self.__age = age

        # atribut tambahan
        self.__gender = None
        self.__height = None

    def get_name(self):
        """Mengembalikan nama orang"""
        return self.__name

    def get_age(self):
        """Mengembalikan umur orang"""
        return self.__age

    def set_gender(self, gender):
        """Mengatur jenis kelamin"""
        self.__gender = gender

    def get_gender(self):
        """Mengambil jenis kelamin"""
        return self.__gender
    
    def set_height(self, height):
        """
        Mengatur tinggi badan.

        :param height: tinggi badan dalam cm
        """
        if height <= 0:
            raise ValueError("Tinggi badan harus lebih dari 0")
        self.__height = height

    def get_height(self):
        """Mengambil tinggi badan"""
        return self.__height
    
    @abstractmethod
    def get_info(self):
        """
        Method abstrak untuk menampilkan informasi lengkap objek.
        Harus diimplementasikan oleh subclass.
        """
        pass
