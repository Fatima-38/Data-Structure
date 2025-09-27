#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;         //agle node ka address store krne k liye pointer
};
int main(){

    Node* head = new Node{10, NULL};        //head pointer jo first node ka address store krta hai
    Node* second = new Node{20, NULL};      //second node ka address store krne k liye pointer
    Node* third = new Node{30, NULL};       //third node ka address store krne k liye pointer

    head->next = second;            //head node ka next pointer second node ko point kr rha hai
    second->next = third;           //second node ka next pointer third node ko point kr rha hai

    cout << "Linked List: ";
    Node* temp = head;       //temp pointer 
    while(temp != NULL){                //jab tak temp NULL na ho jaye
        cout << temp->data << " ";      //temp pointer ka data print krna
        temp = temp->next;      //temp pointer ko next node pe le jana
    }
    return 0;
}