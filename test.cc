#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <numeric>

using namespace std;

int main()
{
    vector<int> grade_vec;

    string gpa_data = "A A B";
    
    // Go through string, only add numbers
    for (int i = 0; gpa_data[i] != '\0'; i++) {
        if (gpa_data[i] == ' ') {
            continue;
        }
        else {
            switch (gpa_data[i]) {
            case 'A':
                grade_vec.push_back(4);
                break;
            case 'B':
                grade_vec.push_back(3);
                break;
            case 'C':
                grade_vec.push_back(2);
                break;
            case 'D':
                grade_vec.push_back(1);
                break;
            case 'F':
                grade_vec.push_back(0);
                break;
            }
        }
    }

    int number_of_grades = grade_vec.size();
    float if_all_perfect = 4 * grade_vec.size();
    float accumulated = accumulate(grade_vec.begin(), grade_vec.end(), 0);
    std::cout <<  accumulated/if_all_perfect << "\n";
    
    
}
