
stack = []
MAX = 5

def Push():
    if len(stack) == MAX:
        print("Stack is full")
    else:
        item = int(input("Enter element: "))
        stack.append(item)
        print("Element added successfully")

def Pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Removed:", stack.pop())

def IsFull():
    print(len(stack) == MAX)

def IsEmpty():
    print(len(stack) == 0)

def Peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Is Full")
    print("4. Is Empty")
    print("5. Peek")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        Push()
    elif choice == "2":
        Pop()
    elif choice == "3":
        IsFull()
    elif choice == "4":
        IsEmpty()
    elif choice == "5":
        Peek()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
