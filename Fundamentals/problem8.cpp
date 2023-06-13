/*
    Write a program that finds the summation of every number from 1 to num. 
    The number will always be a positive integer greater than 0.

    For example (Input -> Output):

    2 -> 3 (1 + 2)
    8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
*/

#include <iostream>
using std::cout; using std::cin; using std::endl;

int summation(int num){
    int result{0};
    for (int i{1}; i <= num; ++i) {
        result += i;
    }
    return result;
}

int main() {
    int num{0};
    cin >> num;
    cout << summation(num) << endl;
    return 0;
}