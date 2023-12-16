my_list = [32, 45, 20, 6, 8, 12, 51, 12] # global variable

def do_sum(a_list):
    sum2 = 0
    for element in a_list:
        sum2 += element ** 2
    return sum2

print(do_sum(my_list[2:5]))