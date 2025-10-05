//Name: Fatima Javaid
//Roll no: 2024-csr-010

#include <iostream>
using namespace std;

class ArrayWrapper {
private:
    int* data;
    int size;

public:

    ArrayWrapper(int n) : size(n) {
        data = new int[size];
        cout << "Dynamic ArrayWrapper created successfully with size" << size << "." << endl;

        for (int i = 0; i < size; ++i){
            data[i] = i * 10 + 5;
        }
    }

    ~ArrayWrapper() {
        delete[] data;
        data = nullptr;
        cout << "ArrayWrapper memory freed safetly. (Destructor called)" << endl;
    }

    int getElement(int index) const {
        if (index >= 0 && index < size) {
            return data[index];
        }
        return -1;
    }

    void print() const {
        cout << "Wrapper Array: [";
        for (int i = 0; i < size; ++i) {
            cout << data[i] << (i == size - 1 ? "" : ", ");
        }
        cout << "]" << endl;
    }
};

int main() {
    cout << "___ Task 1 Demonstration ___" << endl;
    ArrayWrapper wrapper(4);
    wrapper.print();
    cout << "Element at index 2: " << wrapper.getElement(2) << endl;
    return 0;
}