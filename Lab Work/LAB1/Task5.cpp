#include <iostream> 
using namespace std;

int main() {
    int n;
    cout << "Enter array size: ";
    cin >> n;

    int* y = new int[n];

    for (int i = 0; i < n; i++) {
        y[i] = 5 * (i + 1);
    }

    cout << "Dynamic Array: ";
    for (int i = 0; i < n; i++) {
        cout << y[i] << " ";
    }
    cout << endl;
    delete[] y;
    return 0;
}