from repositories.base_repository import BaseRepository


class MissingPersonRepository(BaseRepository):
    """
    Repository penyimpanan data orang hilang.
    """

    def __init__(self):
        self.__data = []

    def add(self, data):
        """Menambahkan data orang hilang"""
        self.__data.append(data)

    def get_all(self):
        """Mengembalikan semua data orang hilang"""
        return self.__data

    def get_by_id(self, id_person):
        """Mencari satu data berdasarkan ID"""
        for person in self.__data:
            if person.get_id() == id_person:
                return person
        return None
    
    def delete(self, id_person):
        """Menghapus data berdasarkan ID"""
        person = self.get_by_id(id_person) 
        if person:
            self.__data.remove(person)
            return True
        return False