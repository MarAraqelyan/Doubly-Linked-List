class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
      self.head = None
      self.tail = None

    def isempty(self):
      return self.head is None

    def prepend(self,data):
      node = Node(data)

      if self.isempty():
        self.head = self.tail = node

      else:
        self.head.prev = node
        node.next = self.head
        self.head = node

    def append(self,data):
        node = Node(data)

        if self.isempty():
          self.head = self.tail = node

        else:
          current = self.head

          while current.next:
            current = current.next

          node.prev = current
          current.next = node
          self.tail = node

    def insert_after(self,target_data,data):
        node = Node(data)
        current = self.head

        while current and current.data != target_data:
            current = current.next

        if current and current.next:
          node.prev = current
          node.next = current.next
          current.next = node

        elif current:
          node.prev = current
          current.next = node

        else:
          raise ValueError("The target_data is not in list")

    def insert_before(self,target_data,data):
        node = Node(data)
        current = self.tail

        while current and current.data != target_data:
          current = current.prev

        if current and current.prev:
          node.next = current
          node.prev = current.prev
          current.prev.next = node

        elif current:
          node.next = current
          current.prev = node
          self.head = node

        else:
          raise ValueError("The target_data is not in list")

    def delete(self,data):
      if self.isempty():
        raise ValueError("The list is empty")

      current = self.head

      if self.head.data == data:
        self.head = self.head.next
        self.head.next.prev = None
        return

      while current.next and current.next.data != data:
        current = current.next

      if current.next:
        current.next = current.next.next

      else:
        raise ValueError("The data is not in list")

    def display(self):
      current = self.head
      while current:
        print(current.data,end = "<-->")
        current = current.next
      print()