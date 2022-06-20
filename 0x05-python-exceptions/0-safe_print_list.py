#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed =  0
    nums = []
    for index in range(x):
        try:
            nums.append(str(my_list[index]))
        except:
            pass
        else:
            num_printed += 1
    print(''.join(nums),' ')
    return num_printed
