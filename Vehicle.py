from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, license_number, entry_time):
        self.license_number = license_number
        self.entry_time = entry_time

    @abstractmethod
    def get_type(self):
        pass
