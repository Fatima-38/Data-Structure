#include <iostream>
using namespace std;

int main() {
    int x[6] = {10, 20, 30, 40, 50, 60};
    int n = 6;

    int pos = 2;

    for (int i = pos; i < n - 1; i++) {
        x[i] = x[i + 1];
    }
    n--;

    cout << "After Deletion: ";
    for (int i = 0; i < n; i++) {
        cout << x[i] << " ";
    }
    cout << endl;
    return 0;
}