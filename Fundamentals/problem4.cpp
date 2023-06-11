/*
    Very simple, given an integer or a floating-point number, find its opposite.

    Examples:

    1: -1
    14: -14
    -34: 34
*/

#include <iostream>

int opposite(int number) {
    return -number;
}

int main() {
    int i = 10;
    i = opposite(i);
    std::cout << i << std::endl;
    return 0;
}