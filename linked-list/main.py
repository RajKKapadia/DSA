class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):

        if self.head is None:
            self.head = Node(value=value)
            return
        
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(value=value)

    def reverse(self):
        
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        self.head = previous

    
    def make_cycle(self, position: int):
        if self.head is None:
            return

        current = self.head
        target_node = None
        index = 0

        while current.next is not None:
            if index == position:
                target_node = current

            current = current.next
            index += 1

        if index == position:
            target_node = current

        if target_node is not None:
            current.next = target_node

        
    def has_cycle(self):
        
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    

    def find_middle(self):
        
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next
        
        return slow


    def print(self):
        current = self.head
        while current is not None:
            print(f"{current.value} -> ", end="")
            current = current.next
        print("None")


def merge_two_linked_lists(one: LinkedList, two: LinkedList) -> LinkedList:
    cur_one = one.head
    cur_two = two.head

    merged = LinkedList()
    tail = None

    while cur_one is not None and cur_two is not None:
        if cur_one.value <= cur_two.value:
            new_node = Node(cur_one.value)
            cur_one = cur_one.next
        else:
            new_node = Node(cur_two.value)
            cur_two = cur_two.next

        if merged.head is None:
            merged.head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

    while cur_one is not None:
        new_node = Node(cur_one.value)

        if merged.head is None:
            merged.head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

        cur_one = cur_one.next

    while cur_two is not None:
        new_node = Node(cur_two.value)

        if merged.head is None:
            merged.head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

        cur_two = cur_two.next

    return merged
    

def remove_nth_element(ll: LinkedList, position: int) -> LinkedList:
    if ll.head is None:
        return ll

    length = 0
    current = ll.head

    while current is not None:
        length += 1
        current = current.next

    if position <= 0 or position > length:
        return ll

    # remove head
    if position == length:
        ll.head = ll.head.next
        return ll

    steps_to_node_before_target = length - position - 1

    current = ll.head

    for _ in range(steps_to_node_before_target):
        current = current.next

    current.next = current.next.next

    return ll


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(20)
ll.append(10)


def check_ll_is_palindrome(ll: LinkedList) -> bool:
    if ll.head is None:
        return True

    length = 0
    current = ll.head

    while current is not None:
        length += 1
        current = current.next

    # Find start of second half
    if length % 2 == 0:
        second_start_index = length // 2
    else:
        second_start_index = length // 2 + 1

    first = ll.head
    second = ll.head

    for _ in range(second_start_index):
        second = second.next

    # Reverse second half
    previous = None
    current = second

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    second = previous

    # Compare first half and reversed second half
    while second is not None:
        if first.value != second.value:
            return False

        first = first.next
        second = second.next

    return True


print(check_ll_is_palindrome(ll=ll))
