def is_even(n):
    return n % 2 == 0

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def max_in_list(numbers):
    if not numbers:
        return None
    return max(numbers)

def min_in_list(numbers):
    if not numbers:
        return None