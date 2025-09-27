#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

//node ko head pe insert krne k liye function
void insertAtHead(Node*& head, int val){
    Node* n = new Node{val, head};
    head = n;
}

//head node ko delete krne k liye function
void deleteHead(Node*& head){
    if(!head) return;
    Node* temp = head;
    head = head->next;
    delete temp;
}

//linked list ko print krne k liye function
void printList(Node* head){
    cout << "List: ";
    for(Node* cur = head; cur; cur = cur->next){        //cur pointer ko head se start krke next node pe le jana
        cout << cur->data << " ";
    cout << endl;
    }
}

int main(){
    Node* head = NULL;

    insertAtHead(head, 30);             //head pe 30 insert krna
    insertAtHead(head, 20);         //head pe 20 insert krna
    insertAtHead(head, 10);        //head pe 10 insert krna
    printList(head);

    deleteHead(head);        //head node ko delete krna
    printList(head);            //linked list ko print krna

    return 0;
}