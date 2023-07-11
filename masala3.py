def meme_sum(number1: int, number2: int) -> int:
    sum = 0
    max_num = max(number1, number2)
    while max_num:
        sum += (number1 % 10 + number2 % 10) * pow(10, len(str(sum)) if sum != 0 else 0)
        number1 //= 10
        number2 //= 10
        max_num //= 10
    return sum
    

print(meme_sum(169, 73))