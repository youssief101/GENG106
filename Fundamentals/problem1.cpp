
/*
    Given a set of numbers, return the additive inverse of each. 
    Each positive becomes negatives, and the negatives become positives.

    invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
    invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
    invert([]) == []
*/

#include <iostream>
#include <vector>

std::vector<int> invert(std::vector<int> values) {
    for (auto &i : values) {
        i = i * -1;
    }
    return values;
}

int main() {
    std::vector<int> ivec = {1, 2, -3, 10, -20, 12, 0};
    ivec = invert(ivec);
    for (auto i : ivec) {
        std::cout << i << std::endl;
    }
    return 0;
}