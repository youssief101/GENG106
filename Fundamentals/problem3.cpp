/*
    Complete the method that takes a boolean value and return a "Yes" 
    string for true, or a "No" string for false.
*/

#include <iostream>
#include <string>

std::string bool_to_word(bool value) {
    return value ? "Yes" : "No";
}

int main() {
    int value = 20;
    std::string result = bool_to_word(value);
    std::cout << result << std::endl;
    return 0;
}