from fcfs import fcfs_fun

def look_fun(num_list, head):
    first = num_list[0]
    new_list = []

    num_list.append(head)
    num_list.sort()

    i = num_list.index(head)

    if head < first:
        
        for num in num_list[i+1:]:
            new_list.append(num)

        for num in num_list[i-1: :-1]:
            new_list.append(num)

    else:

        for num in num_list[i-1: : -1]:
            new_list.append(num)

        for num in num_list[i+1:]:
            new_list.append(num)

    _, total = fcfs_fun(new_list, head)
    
    return new_list, total

if __name__ == "__main__":

    print('----- Seqence range is between 0 - 199 -----')

    num_str = input("Enter the sequece of requests : ")

    num_list = list()

    try:
        num_list = [int(num) for num in num_str.split(',')]
    except:
        print("All the sequence number should be integer..")

    head = int(input("Enter Read/Write arm positon : "))

    seq_list,total = look_fun(num_list, head)
    print('Total seek time is : {}'.format(total))
