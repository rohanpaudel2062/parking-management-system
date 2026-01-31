class ParkingLot:

    def __init__(self):
        self.total_spaces = 300
        self.available_spaces = 300

    def record_entry(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1

    def record_exit(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1

    def get_available_spaces(self):
        return self.available_spaces
