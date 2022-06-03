def product(m, n):
    if m > n:
        return product(n, m)
     
    elif m and n < 0:
        return product(-m, -n)

    elif m != 0:
        return (m + product(m, n - 1))
     
    else:
        return 0
 
print()
print(product(20, 5))
print()
