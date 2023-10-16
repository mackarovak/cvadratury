def almost_double_factorial(n):
    # YOUR CODE
    if (n!=0):
        for i in range(1, n):
            cvadrat*=i
        return cvadrat
    else:
        print(1)
    return 1# YOUR CODE

n = int(input("Введите число: "))
res=almost_double_factorial(n)
print(res)