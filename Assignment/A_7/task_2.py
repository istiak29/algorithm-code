def maximum_number_of_tasks(task, people):
    task.sort(key=lambda x: x[1])
    max_activities = 0
    time = -1

    for t in task:
        if time < t[0]:
            max_activities += 1
            time = t[1]  # Update current time

            if max_activities == people:
                break

    return max_activities


def task_information(file):
    number_of_activities, number_of_people = map(int, file.readline().split())
    task = []
    for i in range(number_of_activities):
        start, finish = map(int, file.readline().split())
        task.append((start, finish))

    return task, number_of_people


input_file = open('input_2.txt', 'r')
output_file = open('output_2.txt', 'w')

Task, People = task_information(input_file)

max_num_activities = maximum_number_of_tasks(Task, People)
print('max task:', max_num_activities)

output_file.write(str(max_num_activities))

input_file.close()
output_file.close()


