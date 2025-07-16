def calculate_tax(amount: float, country: str):
    tax_rates = {"US": 0.07, "IN": 0.18, "EU": 0.20}
    return amount * tax_rates.get(country.upper(), 0.10)
