from abc import ABC, abstractmethod

class PricingStrategy(ABC):

    @abstractmethod
    def calculate_fee(self, hours):
        pass
