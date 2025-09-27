#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of students: ";
    cin >> n;

    int* marks = new int[n];

    for (int i = 0; i < n; i++) {
        cout << "Enter mark of student " << i + 1 << ": ";
        cin >> marks[i];
    }

    cout << "\nMarks entered: ";
    for (int i = 0; i < n; i++) {
        cout << marks[i] << " ";
    }
    cout << endl;

    int sum = 0, maxMark = marks[0], minMark = marks[0];
    for (int i = 0; i < n; i++) {
        sum += marks[i];
        if (marks[i] > maxMark) maxMark = marks[i];
        if (marks[i] < minMark) minMark = marks[i];
    }

    cout << "Average = " << (sum / (float)n) << endl;
    cout << "Highest = " << maxMark << endl;
    cout << "Lowest = " << minMark << endl;

    delete[] marks;
    return 0;
}

