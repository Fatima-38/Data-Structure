#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

int main(){
    int N=10, M=3;

    Node* head = new Node{1, NULL};                 //head pointer jo first node ka address store krta hai
    Node* curr = head;                      //current pointer jo node ka address store krta hai
    for(int i=2; i<=N; i++){                    
        curr->next = new Node{i, NULL};         //current node ka next pointer new node ko point kr rha hai
        curr = curr->next;                  //current pointer ko next node pe le jana
    }
    curr->next = head;                  //last node ka next pointer head ko point kr rha hai

    Node* prev = curr;              //previous pointer jo node ka address store krta hai
    curr = head;

    while(curr->next != curr){          //jab tak current node ka next pointer khud ko na point kre
        for(int i=1; i<M; i++){         
            prev = curr;                //previous pointer ko current pointer pe le jana    
            curr = curr->next;
        }
        cout << "Removing: " << curr->data << endl;
        prev->next = curr->next;                //previous node ka next pointer current node ke next node ko point kr rha hai
        delete curr;
        curr = prev->next;
    }
    cout << "Leader is: " << curr->data << endl;
    return 0;
}