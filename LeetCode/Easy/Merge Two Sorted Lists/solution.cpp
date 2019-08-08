/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {

		if (l1 == nullptr) return l2;
		if (l2 == nullptr) return l1;

		ListNode *node = l1->val > l2->val ? l2 : l1;
		node->next = l1->val > l2->val ? mergeTwoLists(l1, l2->next) : mergeTwoLists(l1->next, l2);

		return node;

	}
};