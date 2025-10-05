//Name: Fatima Javaid
//Roll no: 2024-csr-010

#include <iostream>
using namespace std;

class SNode {
public:
    int data;
    SNode* next;

    SNode(int val) : data(val), next(nullptr) {}
};

class StackList {
private:
    SNode* head;

public:
    StackList() : head(nullptr) {}

    ~StackList() {
        SNode* current = head;

        while (current != nullptr) {
            SNode* next_node = current->next;
            delete current;
            current = next_node;
        }
    }

    void push(int val) {
        SNode* newNode = new SNode(val);
        newNode->next = head;
        head = newNode;
        cout << "Pushed: " << val << endl;
    }

    int pop(){
        if (head == nullptr) {
            cout << "\nERROR: Stack Underflow! (Stack is empty)." << endl;
            return -1;
        }

        SNode* temp = head;
        int val = head->data;
        head = head->next;
        delete temp;

        return val;
    }

    void print() const {
        SNode* current = head;
        cout << "StackList (TOP->BOT): [";
        while (current != nullptr) {
            cout << current->data << (current->next == nullptr ? "" : ", ");
            current = current->next;
        }
        cout << "]" << endl;
    }
};

int main() {
    cout << "___ Task 3 Demonstration ___" << endl;
    StackList stack;

    stack.push(100);
    stack.push(200);
    stack.push(300);
    stack.print();

    cout << "Popped value: " << stack.pop() << endl;
    stack.push(400);
    stack.print();

    return 0;
}