def factiorial(n):

    for i in range(1, n):
        n = n * i
    return n


fact = factiorial(6)
print(fact)
