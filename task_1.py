class Node:
    def __init__(self, data):
        """Ініціалізуємо вузол з заданими даними."""
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """Ініціалізуємо порожній зв'язний список."""
        self.head = None

    def append(self, data):
        """Додаємо новий вузол з заданими даними до кінця списку."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        """Виводимо вміст списку."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Для показу закінчення списку

    def reverse(self):
        """Реверсуємо список."""
        prev, current = None, self.head
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev

    def merge_sorted(self, other):
        """Об'єднуємо два відсортованих списку в один відсортований список."""
        dummy = Node(0)
        tail = dummy
        list1, list2 = self.head, other.head
        while list1 and list2:
            if list1.data <= list2.data:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        self.head = dummy.next

    def insertion_sort(self):
        """Сортуємо список за допомогою сортування вставками."""
        dummy = Node(0)
        current = self.head
        while current:
            prev = dummy
            next_node = current.next
            while prev.next and prev.next.data < current.data:
                prev = prev.next
            current.next, prev.next, current = prev.next, current, next_node
        self.head = dummy.next



def main():
    # Створення та заповнення списків
    list_one = LinkedList()
    list_one.append(1)
    list_one.append(3)
    list_one.append(5)

    list_two = LinkedList()
    list_two.append(2)
    list_two.append(4)
    list_two.append(6)

    # Виведення вмісту списків
    print("List 1:")
    list_one.display()
    print("List 2:")
    list_two.display()

    # Об'єднання та виведення об'єднаного списку
    list_one.merge_sorted(list_two)
    print("Merged & Sorted List:")
    list_one.display()

    # Реверсування об'єднаного списку
    list_one.reverse()
    print("Reverse Sorted List:")
    list_one.display()




if __name__ == "__main__":
    main()
