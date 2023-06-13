/*
    It's pretty straightforward. Your goal is to create a function that removes 
    the first and last characters of a string. 
    You're given one parameter, the original string. 
    You don't have to worry with strings with less than two characters.
*/

#include <iostream>
using std::cout; using std::endl;

#include <string>
using std::string;

string sliceString (string str) {
    str.erase(str.begin());
    str.erase(str.end() - 1);
    return str;
}

int main() {
    string name{"tuna"};
    cout << sliceString(name) << endl;
    return 0;
}