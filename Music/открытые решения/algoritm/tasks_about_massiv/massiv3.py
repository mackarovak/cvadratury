def min_queue(stroka):
    count = 0
    queue = 0

    for i in range(len(stroka)):
        if stroka[i] == '0':
            queue += 1
        else:
            if queue == 0:
                count += 1
            else:
                queue -= 1

    return count

input_str = input().split()

print(min_queue(input_str))