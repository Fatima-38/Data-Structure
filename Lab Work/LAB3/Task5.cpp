//Name: Fatima Javaid
//Roll no: 2024-csr-010

#include <iostream>
using namespace std;

#define MAX_SIZE 5

// ====================================================
//STACK CLASS: Manages a fixed-size integer array.
// ====================================================
class StackArray {
private:
    int data[MAX_SIZE];  // The fixed-size array storage
    int top;             // Index of the top element (serves as the LIFO tracker)

public:
    // Constructor: initializes the stack as empty
    StackArray() : top(-1) {
        cout << "StackArray Initialized (MAX Size: " << MAX_SIZE << ")" << endl;
    }

    // Method 1: Push (Adding an element to the top)
    void push(int val) {
        if (top == MAX_SIZE - 1) {
            cout << "\nERROR: Stack Overflow! Cannot push " << val << " (Array is full)." << endl;
            return;
        }

        // O(1) Push operation: Increment top and add the new value
        data[++top] = val;
        cout << "Pushed: " << val << endl;
    }

    // Method 2: Pop (Removing the top element)
    int pop() {
        if (top == -1) {
            cout << "\nERROR: Stack Underflow! (Stack is empty)." << endl;
            return -1; // Indicate underflow
        }
        // O(1) Pop operation: Return the top value and decrement top
        return data[top--];
    }

    // Method 3: Peek (Viewing the top element without removing it)
    int peek() const {
        if (top == -1) return -1; // Indicate empty stack
        return data[top];
    }

        //Helper to print the stack state
    void print() const {
        cout << "Stack (TOP->BOTTOM): [";
        for (int i = top; i >= 0; --i) {
            cout << data[i] << (i == 0 ? "" : ", ");
        }
        cout << "]" << endl;
    }
};

//=======================================
//MAIN DEMONSTRATION
//=======================================

int main() {
    cout << "--- Task 5: STACK ARRAY DEMO ---" << endl;
    StackArray mystack;

    // Pushing elements up to the capacity (5 elements)
    mystack.push(10);
    mystack.push(20);
    mystack.push(30);
    mystack.push(40);
    mystack.push(50);
    mystack.print();

    //Triggering overflow error
    mystack.push(60);

    //Peek and Pop
    cout << "\nPeek (Top value): " << mystack.peek() << endl; // Should be 50
    cout << "Popped value: " << mystack.pop() << endl; // Should remove 50

    //Emptying the stack
    mystack.pop();
    mystack.pop();
    mystack.pop();
    mystack.pop(); // Stack should be empty now

    //Trigger underflow error
    mystack.pop();
    cout << "\n--- Demo Complete ---" << endl;
    return 0;
}