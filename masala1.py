def prime_factors(number):
    tub = list()
    for i in range(2, number // 2 + 1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
            
        if count == 0:
            tub.append(i)
    
    factors = list()
    l = 0
    while l < len(tub):
        if number % tub[l] == 0:
            number /= tub[l]
            factors.append(tub[l])
        else:
            l += 1
    return factors

print(prime_factors(int(input("Enter the number:\n>>>"))))