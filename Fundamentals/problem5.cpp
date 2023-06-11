/*
    Write a function which calculates the average of the numbers in a given list.

    Note: Empty arrays should return 0.
*/

#include <iostream>
#include <vector>

double calcAverage(const std::vector<int>& values){
    if (!values.empty()) {
        int total{0};
        for (auto i{0}; i < values.size(); ++i) {
            total += values[i];
        }
        return static_cast<double> (total) / values.size();
    } else {
        return 0;
    }
}

int main() {
    std::vector<int> ivec = {10, 20, 30, 40, 50};
    double average = calcAverage(ivec);
    std::cout << average << std::endl;
    return 0;
}