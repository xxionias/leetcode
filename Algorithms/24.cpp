/*
#---->@---->@---->@---->@---->@---->@
            ^     ^
            pre   cur
1. pre -> next = cur -> next
             ---------
            /         \
#---->@---->@     @---->@---->@---->@
            ^     ^
            pre   cur
2. pre = pre -> next
             ---------
            /         \
#---->@---->@     @---->@---->@---->@
                  ^     ^
                  cur   pre
3. cur -> next = pre -> next
             ----------
            /          \
#---->@---->@     @     @---->@---->@
                  \          /
                   ----------
                  ^     ^
                  cur   pre
4. pre -> next = cur
             ----------
            /          \
#---->@---->@     @<----@     @---->@
                  \          /
                   ----------
                  ^     ^
                  cur   pre
5. pre = cur; cur = cur -> next
             ---------
            /         \
#---->@---->@     @<----@     @---->@
                  \          /
                   ----------
                  ^           ^
                  pre        cur
*/
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
  ListNode* swapPairs(ListNode* head) {
    if(!head) return NULL;
    ListNode tmp(0);
    tmp.next = head;
    ListNode *pre = &tmp, *cur = head;
    while(cur && cur -> next) {
      pre -> next = cur -> next;
      pre = pre -> next;
      cur -> next = pre -> next;
      pre -> next = cur;
      pre = cur;
      cur = cur -> next;
    }
    return tmp.next;
  }
};
