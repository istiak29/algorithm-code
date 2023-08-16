def maximum_number_of_tasks(task):
    print('task list:', task)
    task.sort(key=lambda x: x[1])
    # temp_task = []
    # for i in range(len(tasks)):
    #     temp = tasks[i][1]
    #
    # tasks = temp_task.sort()
    print('sorted task list:', task)

    task_completed = []

    finish_time = -1

    for t in task:
        start, finish = t
        if start >= finish_time:
            task_completed.append(t)
            finish_time = finish

    # print('com_task', task_completed)
    return task_completed


def get_task_list(file):
    task_number = int(file.readline())
    task_lsit_of_tuple = []
    for i in range(task_number):
        start, finish = list(map(int, file.readline().split()))
        task_lsit_of_tuple.append((start, finish))

    return task_lsit_of_tuple


def write_max_task(completed_task, file):
    file.write(f"{str(len(completed_task))}\n")
    for i, j in completed_task:
        file.write(f"{i} {j}\n")


input_file = open('input_1.txt', 'r')
output_file = open('output_1.txt', 'w')

Tasks = get_task_list(input_file)
Completed_Task = maximum_number_of_tasks(Tasks)

write_max_task(Completed_Task, output_file)

input_file.close()
output_file.close()
