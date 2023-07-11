def countDigits(number: int, digit: int) -> int:
    if digit >= 10:
        return None
    count = 0
    for i in range(number + 1):
        count += str(i ** 2).count(str(digit))
    return count

print(countDigits(10, 1))