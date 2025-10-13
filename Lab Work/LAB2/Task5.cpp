#include <iostream>
using namespace std;

struct DNode {
    int data;
    DNode* next;            //agle node ka address store krne k liye pointer
    DNode* prev;        //pichle node ka address store krne k liye pointer
};

int main(){

    DNode* head = new DNode{10, NULL, NULL};            //head pointer jo first node ka address store krta hai
    DNode* second = new DNode{20, NULL, head};              //second node ka address store krne k liye pointer
    head->next = second;                        //head node ka next pointer second node ko point kr rha hai
    DNode* third = new DNode{30, NULL, second};     //third node ka address store krne k liye pointer
    second->next = third;           //second node ka next pointer third node ko point kr rha hai

    cout << "Forward: ";
    for (DNode* cur = head; cur; cur = cur->next)       //cur pointer ko head se start krke next node pe le jana
        cout << cur->data << " ";
    cout << endl;

    cout << "Backward: ";
    for (DNode* cur = third; cur; cur = cur->prev)      //cur pointer ko third se start krke previous node pe le jana
        cout << cur->data << " ";
    cout << endl;

    return 0;
}