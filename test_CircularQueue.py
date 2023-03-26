# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:48:01 2023

@author: Benedikt Korbach, Niklas Pawelzik, Justus von Samson-Himmelstjerna, Alvaro Guijarro May
"""

from run import CircularQueue

### Initialization ###

# Create an empty queue
q = CircularQueue()
print("Initialization", "\n")

# Add some elements to the queue
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")

# Get initial length of the queue
print("Initial length of the queue:", len(q))  # Output: 3

# Get the element at the head of the queue
print("Current first element is:", q.first(), "\n")  # Output: "a"

### Dequeue ###

print("Deque", "\n")

# Remove an element from the head of the queue
print("Dequeued element is:", q.dequeue()) # Output: "a"

# Get first element
print("New first element is:", q.first())  # Output: "b"

# Get the current size of the queue
print("Current length of the queue:", len(q), "\n")  # Output: 2

### Enque ###

print("Enque", "\n")

# Add another element to the back of the queue
q.enqueue("d")

# Get the current size of the queue
print("Length after adding new element:", len(q), "\n")  # Output: 3

### Rotation ###

print("Rotation", "\n")

# Rotate the queue
q.rotate()

# Get the element at the head of the queue
print("New first element is:", q.first(), "\n")  # Output: "d"

### Remove all ###

print("Remove all", "\n")

# Remove all elements from the queue
while not q.is_empty():
    print("Most recent dequeue:", q.dequeue())

print("Current length of the queue is", len(q), "so the queue should be empty")