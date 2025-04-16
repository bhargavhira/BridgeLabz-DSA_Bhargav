class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value)+"->"
            cur = cur.next
        return out[:-2]
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value
    def push(self,value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    def pop(self):
        if self.isEmpty():
            print("Empty Stack")
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.value
if __name__ == "__main__":
    stack = Stack()
    for i in range(1,11):
        stack.push(i)
    print(f"Stack:{stack}")
    print(stack.peek())
    for _ in range(1,6):
        top_value = stack.pop()
        print(f"Pop: {top_value}")
    print(f"Stack: {stack}")
