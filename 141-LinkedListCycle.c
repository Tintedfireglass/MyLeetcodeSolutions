/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {

     if (head==NULL || head->next==NULL)
        return false;
    
    struct ListNode *cursor = head;
    struct ListNode *rotate = head->next;
    int ct=0;
    while(rotate!=cursor){

        if (rotate->next==NULL){
        return false;}

        rotate=rotate->next;

        if (rotate->next==NULL){
        return false;}
         
        rotate=rotate->next;
         
         if (cursor->next==NULL){
        return false;}
        
        cursor=cursor->next;
        

    }return true;
}
