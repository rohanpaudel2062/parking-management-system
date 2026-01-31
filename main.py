from car import Car
from peak_pricing import PeakPricing
from parking_lot import ParkingLot

car = Car("ABC123", "10:00")
pricing = PeakPricing()
lot = ParkingLot()

lot.record_entry()
fee = pricing.calculate_fee(2)

print(car.get_type())
print("Fee:", fee)
print("Available spaces:", lot.get_available_spaces())
