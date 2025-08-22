from LinkedList.linked_list import LinkedList

def main():
    linked_list = LinkedList()
    linked_list.prepand(-1)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    linked_list2 = LinkedList()
    linked_list2.append(2)
    linked_list2.append(10)

    linked_list.merge(linked_list2.head)
    linked_list.print()

if __name__ == "__main__":
    main()