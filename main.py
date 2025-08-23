from LinkedList.linked_list import LinkedList

def main():
    linked_list = LinkedList()
    linked_list.append(2)
    linked_list.append(2)
    linked_list.append(0)
    linked_list.print()
    if linked_list.is_palindrom():
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()