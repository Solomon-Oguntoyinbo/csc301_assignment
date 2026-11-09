
class Queue:
    def __init__(self, max_size=5):
        self.queue = []
        self.max_size = max_size

    # ENQUEUE: Add an element to the queue
    def enqueue(self, item):
        if self.isFull():
            print("Queue is Full")
        else:
            self.queue.append(item)
            print(item, "inserted into the queue")

    # DEQUEUE: Remove an element from the queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            item = self.queue.pop(0)
            print("Deleted element:", item)

    # ISFULL: Check if the queue is full
    def isFull(self):
        return len(self.queue) == self.max_size

    # ISEMPTY: Check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # PEEK: View the first element
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front element:", self.queue[0])

    # Display all elements
    def display(self):
        print("Queue:", self.queue)


# Main program
q = Queue()

while True:
    print("\n--- QUEUE OPERATIONS ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Is Full")
    print("4. Is Empty")
    print("5. Peek")
    print("6. Display Queue")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter element to insert: ")
        q.enqueue(item)

    elif choice == "2":
        q.dequeue()

    elif choice == "3":
        print("Queue is Full" if q.isFull() else "Queue is Not Full")

    elif choice == "4":
        print("Queue is Empty" if q.isEmpty() else "Queue is Not Empty")

    elif choice == "5":
        q.peek()

    elif choice == "6":
        q.display()

    elif choice == "7":
        print("Program Terminated")
        break

    else:
        print("Invalid choice. Try again.")