from fcfs import fcfs_fun

def sstf_fun (num_list, head):
    next_head = head

    num_list.append(head)

    num_list.sort()

    new_list = []

    while len(num_list) > 1:

        i = num_list.index(next_head)

        if i == 0:
            next_head = num_list[i+1]
            num_list.pop(i)
        elif i == len(num_list) - 1 :
            next_head = num_list[i]
            num_list.pop(i)
        else:
            diff1 = abs(num_list[i] - num_list[i-1])
            diff2 = abs(num_list[i+1] - num_list[i])
            next_head = [num_list[i-1] if diff1 < diff2 else num_list[i+1]][0]
            num_list.pop(i)

        new_list.append(next_head)

    _, total = fcfs_fun(new_list, head)

    return new_list, total

if __name__ == "__main__":

    num_str = input("Enter the sequece of requests : ")

    num_list = list()
    try:
        num_list = [int(num) for num in num_str.split(',')]
    except:
        print("All the sequence number should be integer..")
    head = int(input("Enter Read/Write arm positon : "))

    seq_list, total = sstf_fun(num_list, head)
    print('Total seek time is : {}'.format(seq_list))
