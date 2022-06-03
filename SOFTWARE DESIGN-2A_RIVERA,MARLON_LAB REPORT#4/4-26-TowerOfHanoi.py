def TowerOfHanoi(n, A, B, C):
    if n == 0:
        return
    TowerOfHanoi(n - 1, A, C, B)
    print("Move disk", n, "from tower", A, "to tower", B)
    TowerOfHanoi(n - 1, C, B, A)

n = int(input("Enter no. of disk: "))
TowerOfHanoi(n, 'A', 'C', 'B')

