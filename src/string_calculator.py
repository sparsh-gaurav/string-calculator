def add(numbers: str | None) -> int:
    if not numbers:
        return 0
    numbers = numbers.replace("\n", ",")
    number_list = numbers.split(",")
    return sum(int(n) for n in number_list)