#include <iostream>
using namespace std;

struct CNode {
    int data;
    CNode* next;
};  

int main(){
    int n = 5;
    CNode* head = new CNode{1, NULL};           //head pointer jo first node ka address store krta hai
    CNode* curr = head;                     //current pointer jo node ka address store krta hai

    for(int i = 2; i <= n; i++){                //2 se n tak nodes create krna
        curr->next = new CNode{i, NULL};            //current node ka next pointer new node ko point kr rha hai
        curr = curr->next;                          //current pointer ko next node pe le jana
    }
    curr->next = head;

    cout << "Circular List: ";
    curr = head;
    for(int i = 0; i < n; i++){         //n nodes ko print krna 
        cout << curr->data << " ";
        curr = curr->next;
    }
    cout << endl;
    return 0;
}