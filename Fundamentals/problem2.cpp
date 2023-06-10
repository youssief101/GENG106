/*
    Build a function that returns an array of integers from n to 1 where n>0.
    Example : n=5 --> [5,4,3,2,1]
*/

#include <iostream>
#include <vector>

std::vector<int> reverseSeq(int n) {
    std::vector<int> ivec;
    for (int i{n}; i != 0; --i) {
        ivec.push_back(i);
    }

    return ivec;
}

int main() {
    int n = 20;
    for (auto i : reverseSeq(n)) {
        std::cout << i << " ";
    }
    return 0;
}