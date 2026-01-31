from pricing_strategy import PricingStrategy

class WeekendPricing(PricingStrategy):

    def calculate_fee(self, hours):
        return hours * 4
