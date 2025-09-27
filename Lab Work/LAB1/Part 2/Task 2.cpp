#include <iostream>
using namespace std;

int main() {
    int x[10];
    int n = 5;

    for (int i = 0; i < n; i++) {
        x[i] = i + 1;
    }

    x[n] = 99;
    n++;

    cout << "After Insertion: ";
    for (int i = 0; i < n; i++) {
        cout << x[i] << " ";
    }
    cout << endl;
    return 0;
}