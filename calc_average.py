def main():
    numbers = int(input("How many number you want to calculate the average for? "))
    control = 0
    sum = 0
    while control < numbers:
        number = int(input("Enter the number: "))
        sum += number
        control += 1

    print(f"Average: {sum / numbers}")

main()