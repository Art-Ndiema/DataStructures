top = 0
mymax = eval(input("Enter maximum size of stack (as a positive integer): "))

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def Push(stack, item):
    stack.append(item)
    print("Pushed to stack", item)

def Pop(stack):
    if isEmpty(stack):
        return "Stack underflow"
    return stack.pop()

stack = createStack()

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Quit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        if top < mymax:
            item = input("Enter any element: ")
            Push(stack, item)
            top += 1
        else:
            print("Stack overflow")
    elif ch == 2:
        print(Pop(stack))
        top -= 1
    elif ch == 3:
        print(stack)
    elif ch == 4:
        print("Exit")
        break
    else:
        print("Invalid choice. Please select a valid option.")
