def dfs(jumanji_map, row, col, visited):
    if row < 0 or row >= len(jumanji_map) or col < 0 or col >= len(jumanji_map[0]) or jumanji_map[row][col] == '#' or visited[row][col]:
        return 0

    visited[row][col] = True
    collected_diamonds = 0

    if jumanji_map[row][col] == 'D':
        collected_diamonds = 1

    # Explore all four directions (up, down, left, right) from the current cell
    collected_diamonds += dfs(jumanji_map, row + 1, col, visited)
    collected_diamonds += dfs(jumanji_map, row - 1, col, visited)
    collected_diamonds += dfs(jumanji_map, row, col + 1, visited)
    collected_diamonds += dfs(jumanji_map, row, col - 1, visited)

    return collected_diamonds

def max_diamond_find(jumanji_map):
    max_diamonds_collection = 0
    rows, cols = len(jumanji_map), len(jumanji_map[0])

    for i in range(rows):
        for j in range(cols):
            if jumanji_map[i][j] == '.':
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                max_diamonds_collection = max(max_diamonds_collection, dfs(jumanji_map, i, j, visited))

    return max_diamonds_collection

def input_read(input_file):
    with open(input_file, "r") as file:
        R, H = map(int, file.readline().split())
        jumanji_map = [file.readline().strip() for _ in range(R)]
    return jumanji_map

def output_write(output_file, result):
    with open(output_file, "w") as file:
        file.write(str(result))


input_file = "input_6.txt"
output_file = "output_6.txt"

jumanji = input_read(input_file)
result = max_diamond_find(jumanji)
output_write(output_file, result)

print(result)
