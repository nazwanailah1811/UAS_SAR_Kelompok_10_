from abc import ABC, abstractmethod


class BaseRepository(ABC):
    """
    Interface repository sebagai penerapan
    Dependency Inversion Principle.
    """

    @abstractmethod
    def add(self, data):
        """Menambahkan data"""
        pass

    @abstractmethod
    def get_all(self):
        """Mengambil seluruh data"""
        pass

