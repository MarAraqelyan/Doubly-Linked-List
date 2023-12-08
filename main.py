from DoublyLinkedList import LinkedList

def main():

    linked_list = LinkedList()


    linked_list.prepend(1)
    linked_list.append(2)
    linked_list.insert_after(1, 3)
    linked_list.insert_before(2, 4)
    linked_list.display()


if __name__ == "__main__":
    main()
