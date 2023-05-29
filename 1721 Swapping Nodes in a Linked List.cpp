// You are given the head of a linked list, and an integer k.
// Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed)0.

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        
    ListNode* h1=NULL , *h2=NULL;
    h1=h2=head;
    int cnt=0;
    while(h1!=NULL){
        h1=h1->next;
        cnt++;

    }
    h1=head;
    int i=k;
    while(i>1){
        h1=h1->next;
        i--;
    }
    int j=cnt-k;
    while(j>0){
        h2=h2->next;
        j--;
    }
    swap(h1->val,h2->val);
    return head;


    }
};