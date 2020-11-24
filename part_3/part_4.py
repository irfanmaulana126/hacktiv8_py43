def fakstorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fakstorial(n-1)

print(fakstorial(4))