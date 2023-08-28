input_file = open('input_3.txt', 'r')
output_file = open('output_3.txt', 'w')


def coin_change(coin_list, amount):
    list1 = [amount + 1] * (amount + 1)
    list1[0] = 0
    for val1 in range(1, len(list1)):
        for val2 in coin_list:
            if val1 - val2 >= 0:
                list1[val1] = min(list1[val1], 1 + list1[val1 - val2])
    if list1[amount] != amount + 1:
        return list1[amount]
    else:
        return -1


list2 = input_file.readline().split()
numb, amount1 = int(list2[0]), int(list2[1])
list3 = input_file.readline().split()
list4 = []

for val3 in range(numb):
    list4.append(int(list3[val3]))

result = coin_change(list4, amount1)

print(result, file=output_file)
output_file.close()
