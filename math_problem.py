import math
def main():
    lines = ''
    for degree in range(10, 90, 5):
        sine = math.sin(math.radians(degree))
        formatted_sin = format(sine, '8.5f')
        lines += str(degree) + formatted_sin + '\n'
    print(lines[:8])
    print(lines[-11:-3])
main()
