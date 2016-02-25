# Implementation provided in book:
def parChecker_simple(symbol_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        current_symbol = symbol_string[index]
        if current_symbol == '(':
            s.push(current_symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
    if balanced and s.isEmpty():
        return True
    else:
        return False

# My implementation:
def par_checker_simple(symbol_string):
    s = Stack()
    for i in range(len(symbol_string)):
        if symbol_string[i] == '(':
            s.push(symbol_string[i])
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
    return True and s.isEmpty()

# Another of my implementations without using a stack:
def paren_checker_simeple_2(symbol_string):
    return symbol_string.count('(') == symbol_string.count(')')


print parChecker_simple('((()))')
print parChecker_simple('(()')
print par_checker_simple('((()))')
print par_checker_simple('(()')


def parChecker_general(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
                    index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print parChecker_general('{{([][])}()}')
print parChecker_general('[{()]')
