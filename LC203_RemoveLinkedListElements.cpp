// Definition for singly-linked list.
struct ListNode {
    int val;
    stNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* cursor = head;

        while(true)
        {
            if(head == NULL)
                return NULL;
            if(cursor -> val != val)
                break;
            cursor = cursor->next;
            head = cursor;
        }
        while(cursor->next)
        {
            if(cursor->next->val == val)
            {
                cursor->next = cursor->next->next;
            }
            else
            {
                cursor = cursor->next;
            }
        }
        return head;
    }
};
