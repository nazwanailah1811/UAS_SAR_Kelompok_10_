from abc import ABC, abstractmethod


class Rescuer(ABC):
    """
    Kelas abstrak untuk tim penyelamat (SAR).
    """

    def __init__(self, id_team, team_name):
        self._id_team = id_team
        self._team_name = team_name

    @abstractmethod
    def search(self, person):
        """
        Method pencarian yang harus diimplementasikan
        oleh setiap jenis tim SAR.
        """
        pass


class LandRescuer(Rescuer):
    """Tim SAR darat"""

    def search(self, person):
        return f"Tim Darat mencari {person.get_name()} di wilayah darat"


class WaterRescuer(Rescuer):
    """Tim SAR air"""

    def search(self, person):
        return f"Tim Air menyisir sungai/laut untuk {person.get_name()}"


class AirRescuer(Rescuer):
    """Tim SAR udara"""

    def search(self, person):
        return f"Tim Udara memantau area udara untuk {person.get_name()}"


