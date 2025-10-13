#include <iostream>
using namespace std;

int main() {
    int x[6];

    for (int j = 0; j < 6; j++) {
        x[j] = 2 * j;
    }

    cout << "Static Array Elements: ";
    for (int j = 0; j < 6; j++) {
        cout << x[j] << " ";
    }

    cout << endl;
    return 0;
}