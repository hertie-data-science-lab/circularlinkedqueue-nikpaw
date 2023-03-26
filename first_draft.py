# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:37:22 2023

@author: Niklas Pawelzik, Justus von Samson-Himmelstjerna, Alvaro Guijarro May, Benedikt Korbach
"""
# Implement a queue as a Circular Linked List.
# Your CircularQueue should use an inner class Node.
    # Your queue should keep track of its size.
    # Your queue should implement the following methods:
        # first(self) returns the element that is currently at the head of the queue. Raises an exception if the queue is empty.
        # dequeue(self) Removes the first element of the queue.
        # enqueue(self) Adds an element to the back of the queue. Raises an exception if the queue is empty.
        # def rotate(self): Rotate the queue: effectively transfer the item at the head of the list to the tail of the list
    # You may use the template provided, or start your own implementation from scratch.


class CircularQueue:
    # Inner class "node" for creating nodes
    class Node:
        # defines inner Node class with two variables
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            # holds the data for each node in queue
            self.next = next
            # points to next node

    def __init__(self):
        # initializes the queue with a _tail variable
        self._tail = None
        # points to the last node in the list
        self._size = 0
        # keeps track of the number of elements in the queue

    def __len__(self):
        # returns the number of elements from size
        return self._size

    def is_empty(self):
        # checks if the queue is empty
        return self._size == 0

    def first(self):
        # returns the element at the head of the queue (first added)
        if self.is_empty():
            raise Exception('Queue is empty')
        head = self._tail.next
        return head.element

    def dequeue(self):
        # removes and returns the element at the head of the queue
        if self.is_empty():
            raise Exception('Queue is empty')
        oldhead = self._tail.next
        if self._size == 1:
            # checks if the queue contains only one element.
            self._tail = None
            # if yes: sets the head of the queue to None
        else:
            self._tail.next = oldhead.next
            # set next attribute of current head to
            # next attribute of the node that comes after
        self._size -= 1
        return oldhead.element

    def enqueue(self, e):
        # adds an element to the back of the queue
        newest = self.Node(e, None)
        # creates new Node object "newest" with element "e"
        if self.is_empty():
            newest.next = newest
            # sets newest as the head of the queue
            # sets its next attribute to itself
        else:
            newest.next = self._tail.next
            # sets next attribute of newest to the current head
            self._tail.next = newest
            # sets next attribute of current head of the queue to newest
        self._tail = newest
        # set newest as the new head of the queue
        self._size += 1

    def rotate(self):
        # rotates the queue by moving the element at the head to the tail
        if not self.is_empty():
            self._tail = self._tail.next


# Create an empty queue
q = CircularQueue()

# Add some elements to the queue
q.enqueue("First test")
q.enqueue("Another element")
q.enqueue("last initial element")

# Get the element at the head of the queue
print("Current first element is:", q.first())  # Output: First test

# Remove an element from the head of the queue
print(q.dequeue())

# Add another element to the back of the queue
q.enqueue("Later addition")

# Get the current size of the queue
print("Current length of the queue:", len(q))  # Output: 3

# Rotate the queue
q.rotate()

# Get the element at the head of the queue
print("New first element is:", q.first())  # Output: rotated element

# Remove all elements from the queue
while not q.is_empty():
    print("Most recent dequeue:", q.dequeue())

print("Current length of the queue is", len(q), "so the queue should be empty")
