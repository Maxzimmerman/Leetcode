from LinkedList.linked_list import LinkedList

def main():
    linked_list = LinkedList()
    linked_list.prepand(-1)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.delete_first()
    linked_list.delete_first()
    linked_list.print()
    print("reverse")
    linked_list.reverse()

if __name__ == "__main__":
    main()