def test(n):
    if n > 0:

        return test(n-1)



a = test(4)
print(a)