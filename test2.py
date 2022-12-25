def prime(a):
    sum =0
    for i in (2,3,5,7):
        if a%i == 0:
            sum = sum + i
    for i in range(8, a):
        if all([i % j != 0 for j in (2,3,5,7)]):
            if a % i == 0:
                sum = sum + i
                
    return sum

print(prime(int(input('enter the number : '))))