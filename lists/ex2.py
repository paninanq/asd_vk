# n = int(input())
# array = list(map(int, input().split()))
#
#
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, value):
#         # Если список пуст, создаем первый узел
#         if self.head is None:
#             self.head = Node(value)
#             self.tail = self.head
#         else:
#             # Иначе добавляем новый узел в конец списка
#             new_node = Node(value)
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#
#     def insert(self, index, value):
#         # Проверяем, есть ли узлы вообще
#         if self.head is None:
#             self.append(value)
#             return
#
#         # Находим узлы до и после индекса
#         current_node = self.head
#         for _ in range(index):
#             current_node = current_node.next
#
#         # Создаем новый узел
#         new_node = Node(value)
#
#         # Связываем нового узла с предыдущим и следующим
#         new_node.next = current_node
#         new_node.prev = current_node.prev
#         current_node.prev.next = new_node
#         current_node.prev = new_node
#
#     def remove(self, index):
#         # Проверяем, есть ли узлы вообще
#         if self.head is None:
#             return
#
#         # Находим узлы до и после индекса
#         current_node = self.head
#         for _ in range(index):
#             current_node = current_node.next
#
#         # Удаляем узел
#         current_node.prev.next = current_node.next
#         current_node.next.prev = current_node.prev
#
#     def __getitem__(self, index):
#         # Возвращаем значение по индексу
#         current_node = self.head
#         for _ in range(index):
#             current_node = current_node.next
#         return current_node.value
#
#     def __len__(self):
#         # Возвращаем длину списка
#         length = 0
#         current_node = self.head
#         while current_node is not None:
#             length += 1
#             current_node = current_node.next
#         return length
#
#
# # Вспомогательный класс для узла
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#
#
# # Пример использования
# list = DoubleLinkedList()
# for i in range(n):
#     list.append(array[i])
#
#
# cnt = 0
# current_node = list.head
# i = 0
# while i < n-cnt:
#     if current_node.value == 0:
#         if current_node == list.head:
#             current_node.next.prev = None
#             list.head = current_node.next
#             current_node = list.head
#         else:
#             current_node.prev.next = current_node.next
#             current_node.next.prev = current_node.prev
#             current_node = current_node.next
#         cnt += 1
#         list.append(0)
#     else:
#         current_node = current_node.next
#         i += 1
# array = []
# for i in range(n):
#     array.append(list.__getitem__(i))
# print(*array)


n = int(input())
array = list(map(int, input().split()))
i = 0
cnt = 0
while i<n-cnt:
    if array[i] == 0:
        array = array[:i]+array[i+1:]+[0]
        cnt+=1
    else: i+=1
print(*array)