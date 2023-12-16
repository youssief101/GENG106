def main():
    list = [12, 20, 40, 50, 10, 30, 53, 31]
    highest = list[0]
    lowest = list[0]
    for number in list:
        if highest < number:
            highest = number
        if lowest > number:
            lowest = number

    print(f"The highest number is {highest}, and the lowest is {lowest}.")

main()
