

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()

print(s.isEmpty())

s.push(4)
s.push('dog')
print(s.peek())



def parChecker(SymbolStr):

    my_stack = Stack()
    len_str = len(SymbolStr)
    balanced = True
    idx = 0

    while idx < len_str and balanced:
        if SymbolStr[idx] == '(':
            my_stack.push(SymbolStr[idx])

        else:
            if my_stack.isEmpty():
                balanced = False
            else:
                my_stack.pop()

        idx += 1

    if balanced and my_stack.isEmpty():
        return True
    else:
        return False
#
# from pythonds.basic.stack import Stack

def parChecker2(SymbolStr):

    my_stack = Stack()
    len_str = len(SymbolStr)
    balanced = True
    idx = 0

    while idx < len_str and balanced:
        symbol = SymbolStr[idx]
        if SymbolStr[idx] in '[({':
            my_stack.push(symbol)

        else:
            if my_stack.isEmpty():
                balanced = False
            else:
                top = my_stack.pop()
                if not matches(top, symbol):
                    balanced = False

        idx += 1

    if balanced and my_stack.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker2('[{}]'))
print(parChecker2('(()()())'))


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        rem_stack.push(rem)
        decNumber = decNumber // base

    binString = ""
    while not rem_stack.isEmpty():
        binString = binString + digits[rem_stack.pop()]

    return binString


print(baseConverter(26, 26))
