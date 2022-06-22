from collections import deque


class Stack(object):

    def __init__(self) -> None:
        self.container = deque()

    def insert(self, value):
        self.container.append(value)

    def peek(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()

    def get_length(self):
        return len(self.container)

    def is_empty(self):
        return True if self.get_length() == 0 else False


def is_match(ch1, ch2):

    match_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    return match_dict[ch1] == ch2


def is_balanced(str):
    s = Stack()

    starting_braces = ['(', '{', '[']
    ending_braces = [')', '}', ']']

    for i in str:
        if i in starting_braces:
            s.insert(i)

        if i in ending_braces:
            if s.is_empty():
                return False
            if not is_match(i, s.pop()):
                return False

    return s.is_empty()


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
