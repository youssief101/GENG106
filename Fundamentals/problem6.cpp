/*
    Our football team has finished the championship.

    Our team's match results are recorded in a collection of strings. 
    Each match is represented by a string in the format "x:y", 
    where x is our team's score and y is our opponents score.

    For example: ["3:1", "2:2", "0:1", ...]

    Points are awarded for each match as follows:

    if x > y: 3 points (win)
    if x < y: 0 points (loss)
    if x = y: 1 point (tie)
    We need to write a function that takes this collection and returns 
    the number of points our team (x) got in the championship by the rules 
    given above.

    Notes:

    our team always plays 10 matches in the championship
    0 <= x <= 4
    0 <= y <= 4
*/

#include <iostream>
#include <array>
#include <string>

int points(const std::array<std::string, 10>& games) {
    int totalPoints{0};
    // iterate over games array
    for (const std::string& match : games) {
        int x = match[0] - '0'; // extract score of our team
        int y = match[2] - '0'; // extract score of opponent

        if (x > y) {
            totalPoints += 3;
        } else if (x == y) {
            totalPoints += 1;
        }
    }

    return totalPoints;
}

int main() {
    std::array<std::string, 10> arr = {"3:0", "4:1", "1:1", "5:0", "0:3", "4:1", "2:2", "0:4", "0:1", "4:2"};
    int result = points(arr);
    std::cout << result << std::endl;
    return 0;
}