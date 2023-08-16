

# Read input from file
with open("input_max_task.txt", "r") as input_file:
    N = int(input_file.readline())
    tasks = []
    for _ in range(N):
        start, end = map(int, input_file.readline().split())
        tasks.append((start, end))


# Find maximum number of tasks
completed_tasks = max_tasks(tasks)
num_completed_tasks = len(completed_tasks)

# Write output to file
with open("output_max_task.txt", "w") as output_file:
    output_file.write(str(num_completed_tasks) + "\n")
    for task in completed_tasks:
        output_file.write(str(task[0]) + " " + str(task[1]) + "\n")