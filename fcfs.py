
def fcfs_fun (num_list, head):

    next_head = head
    total = 0

    print('Current position --> Next position')

    for num in num_list:
        temp = abs(next_head - num)
        print('{} --> {}'.format(next_head, num))
        next_head = num
        total += temp

    print('Total seek time is : {}'.format(total))
    num_list.insert(0, head)
    return num_list, total


if __name__ == '__main__':

    num_str = input("Enter the sequece of requests : ")

    num_list = list()
    try:
        num_list = [int(num) for num in num_str.split(',')]
    except:
        print("All the sequence number should be integer..")
    head = int(input("Enter Read/Write arm positon : "))

    ls, tot = fcfs_fun(num_list, head)