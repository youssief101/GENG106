def calc_summation(start_num, end_num):
    sum = 0
    while start_num <= end_num:
        sum += start_num
        start_num += 1
    
    return sum

def main():
    num1 = int(input("start number: "))
    num2 = int(input("end number: "))
    summation = calc_summation(num1, num2)
    print(summation)
main()