def friend_circle(people, connection, file):
    parent = [i for i in range(people + 1)]
    # print('parent:', parent)

    def union(x, y):
        u = find(x)
        v = find(y)
        c = 0

        for i in range(len(parent)):
            if u != v and parent[i] == v:
                parent[i] = u
                c += 1
            elif parent[i] == u:
                c += 1
        # print('count:', c)
        file.write(f'{c}\n')

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    for i, j in connection:
        union(i, j)


def task_information(file):
    vertex, edge = list(map(int, file.readline().split()))
    connection = []

    for i in range(edge):
        start, finish = list(map(int, file.readline().split()))
        connection.append((start, finish))

    # print('connection:', connection)
    return vertex, connection



input_file = open('input_3.txt', 'r')
output_file = open('output_3.txt', 'w')

People, Connection = task_information(input_file)
friend_circle(People, Connection, output_file)

input_file.close()
output_file.close()
