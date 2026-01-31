from pricing_strategy import PricingStrategy

class PeakPricing(PricingStrategy):

    def calculate_fee(self, hours):
        return hours * 5
