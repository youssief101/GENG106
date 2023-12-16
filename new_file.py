print("Table of squares")
limit = int(input("How high to go? "))
print("\nNunmber\tSquare")
number = 1
while number <= limit:
    print(f"{number:2d}\t{number * number:3d}")
    number = number + 1