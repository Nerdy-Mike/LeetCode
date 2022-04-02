#Runtime: 36ms top 7%
#Memory Usage: top 40%
#Time Complexity: O(n)
#Space Complexty: O(n)
class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next

class Soluion:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
            temp = ListNode()
            tail = temp
            while True:
                if list1 is None:
                    tail.next = list2
                    break
                if list2 is None:
                    tail.next = list1
                    break

                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.mext = list2
                    list2 = list2.next

            return temp.next

     


