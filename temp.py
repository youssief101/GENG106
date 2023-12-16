import math

def main():
    try:
        file = open('file.txt', 'r')
        content = file.readlines()
        file.close()  # Close the file after reading its content
        for line in content:
            number = int(line.strip())
            square_root = math.sqrt(number)
            print(square_root)
    except FileNotFoundError:
        print(f"File isn't here!")

main()
