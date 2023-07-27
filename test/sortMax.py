def Min(a):
    m = 0
    c = 0
    for i in range(len(a)):
        if m < a[i]:
            m = a[i]

    return m


a = [10, 4, 3, 9, 8, 19, 23, 29]
print(f"Max: {Min(a)}")

def sortMin(arr):
    array = []
    if len(arr) >= 1:
        array.append(Min())
    else:

