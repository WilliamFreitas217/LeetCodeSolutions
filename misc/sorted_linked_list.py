class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_node_lists(list1, list2):
    node_list_1 = []
    node_list_2 = []
    for i in list1:
        node_list_1.append(ListNode(i))

    for i in list2:
        node_list_2.append(ListNode(i))

    for n in range(len(node_list_1[:-1])):
        node_list_1[n].next = node_list_1[n + 1]
    for n in range(len(node_list_2[:-1])):
        node_list_2[n].next = node_list_2[n + 1]
    return node_list_1, node_list_2


def sort_node_list(list1, list2):
    def get_entire_list(head):
        list_node = [head]
        node = head.next
        while node:
            list_node.append(node)
            node = node.next
        return list_node

    if list1 is None and list2 is None:
        return list1

    head_1 = list1  # weird looking code but okay
    head_2 = list2  # weird looking code but okay

    if list1 is not None and list2 is None:
        list_node1 = get_entire_list(head_1)
        list3 = [n for n in list_node1]
    elif list1 is None and list2 is not None:
        list_node2 = get_entire_list(head_2)
        list3 = [n for n in list_node2]
    else:
        list_node1 = get_entire_list(head_1)
        list_node2 = get_entire_list(head_2)
        list3 = [n for n in list_node1 + list_node2]

    list3 = sorted(list3, key=lambda node: node.val)
    for n in range(len(list3[:-1])):
        list3[n].next = list3[n + 1]
    return list3[0]
