//Name: Fatima Javaid
//Roll no: 2024-csr-010

#include <iostream>
using namespace std;

#define MAX_SIZE 5

class StackArray {
private:
    int data[MAX_SIZE];
    int top;

public:

    StackArray() : top(-1){}

    void push(int val) {
        if (top == MAX_SIZE - 1) {
            cout << "\nERROR: Stack Overflow! Cannot push " << val << "(Array is full)." << endl;
            return;
        }
        data[++top] = val;
        cout << "Pushed: " << val << endl;
    }

    int pop(){
        if (top == -1) {
            cout << "\nERROR: Stack Underflow! (Stack is empty)." << endl;
            return -1;
        }

        return data[top--];
    }

    int peek() const {
        if (top == -1) return -1;
        return data[top];
    }

    void print() const {
        cout << "StackArray (TOP->BOT): [";
        for (int i = top; i >= 0; --i) {
            cout << data[i] << (i == 0 ? "" : ", ");
        }
        cout << "]" << endl;
    }
};

int main() {
    cout << "___ Task 2 Demonstration ___" << endl;
    StackArray stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(40);
    stack.push(50);
    stack.push(60); // trigger overflow
    stack.print();

    

    cout << "Popped value: " << stack.pop() << endl;
    stack.print();
    return 0;
}