from pricing_strategy import PricingStrategy

class OffPeakPricing(PricingStrategy):

    def calculate_fee(self, hours):
        return hours * 3
