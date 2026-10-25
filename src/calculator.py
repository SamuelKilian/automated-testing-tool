def calculate_average(values):
    """Return the average of a non-empty list of numbers."""
    if not values:
        raise ValueError("The list cannot be empty.")

    return sum(values) / len(values)