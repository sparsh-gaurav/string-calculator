def add(numbers: str | None) -> int:
    if not numbers:
        return 0
    number_list = numbers.split(",")
    return sum(int(n) for n in number_list)