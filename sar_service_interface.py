from abc import ABC, abstractmethod


class ISARService(ABC):
    """
    Interface layanan SAR
    """

    @abstractmethod
    def add_missing_person(self, person):
        pass

    @abstractmethod
    def get_all_missing(self):
        pass

    @abstractmethod
    def update_status(self, id_person, new_status, new_location=None):
        pass

    @abstractmethod
    def delete_missing_person(self, id_person):
        pass