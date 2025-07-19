# Utility functions for budget tracker
def get_categories(transactions):
    return sorted(set(t.category for t in transactions))

def calculate_category_total(transactions, category):
    return sum(t.amount for t in transactions if t.category == category)