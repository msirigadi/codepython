"""
Write a function in python that checks if paranthesis in the string
are balanced or not. Possible parantheses are "{}',"()" or "[]". Use
Stack class from the tutorial.
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""

from Datastructures_Stack_BasicImplementation import Stack

"""
def is_balanced(string):
    st = Stack()
    oplist = ['{', '[', '(']
    cplist = ['}', ']', ')']

    isbal = False

    for ch in string:
        if ch in oplist:
            st.push(ch)
        elif ch in cplist:
            for index, element in enumerate(cplist):
                if element == ch:
                    if st.size() != 0:
                        if st.pop() == oplist[index]:
                            isbal = True
                        else:
                            isbal = False

    return isbal
"""

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0

if __name__ == "__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))