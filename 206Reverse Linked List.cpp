// Given the head of a singly linked list, reverse the list, and return the reversed list.

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
    ListNode* reverseList(ListNode* head) {

        if(head==NULL || head->next==NULL)
        return head;
        ListNode * pr, *cr;
        pr=NULL;
        cr=head;

        while(cr!=NULL)
        {
            ListNode*next =cr->next;
            cr->next=pr;
            pr=cr;
            cr=next;

        }
        return pr;     
    }
};