def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    
    except IndexError:
        count = 0
        for i in my_list:
            count += 1
        print()
        return count
