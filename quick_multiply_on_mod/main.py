def quick_multiply_on_mod(n, degree, mod):
    value = 0
    
    if degree == 0:
        return 1
    else:
        value = quick_multiply_on_mod(n, degree // 2, mod)

    if degree % 2 == 0:
        return value**2 % mod
    else:
        return n*value**2 % mod
        

print("Enter numbers:\t");

while True:
    n, degree, mod = [int(i) for i in input().split()]#int()
    
    if degree >= 0 and mod > 0:
        break
    else:
        print("Enter right numbers:\t")

print("Answer:\t", quick_multiply_on_mod(n, degree, mod))