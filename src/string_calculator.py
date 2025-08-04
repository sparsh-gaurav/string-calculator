class NegativeNumberException(Exception):
    """Custom exception for negative numbers in the string calculator."""
    pass

def add(numbers: str | None) -> int:
    if not numbers:
        return 0
    delimiter = ","
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = header[2:]

    numbers = numbers.replace('\n', delimiter)
    number_list = numbers.split(delimiter)
    negative_numbers = [n for n in number_list if int(n) < 0]
    if negative_numbers:
        raise NegativeNumberException(f"negative numbers not allowed {','.join(negative_numbers)}")
    return sum(int(n) for n in number_list)