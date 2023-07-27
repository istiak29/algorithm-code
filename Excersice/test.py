n = [5, 4, 12, 11, 9]

c = 0  # just for check
inl = 0  # just for check

flag = False

for j in range(len(n) - 1):
    for i in range(len(n) - 1):
        if n[i] < n[i + 1]:
            t = n[i]
            n[i] = n[i + 1]
            n[i + 1] = t
            inl += 1  # just for check
            flag = True

    if not flag:
        break
    c += 1  # just for check
print(n)
print("Outer Iteration Number:", c)  # just for check
print("inner Iteration Number:", inl)  # just for check

print("Length of Array:", len(n))  # just for check
