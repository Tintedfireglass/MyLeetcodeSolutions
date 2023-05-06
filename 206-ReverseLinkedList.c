/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){

    struct ListNode* cursor = head;
    struct ListNode* prev = NULL;
    struct ListNode* next = head;
    while(next != NULL){
        next=cursor->next;
        cursor->next=prev;
        prev=cursor;
        cursor=next;
    }
    return prev;
}
