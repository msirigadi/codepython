"""
1. Write a function in python that can reverse a string using stack data structure.
Use Stack class from the tutorial.

reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

2. Write a function in python that checks if paranthesis in the string are balanced or not.
Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""

from DQ_CeateStack import Stack

def reverse_string(str):
    st = Stack()

    for ch in str:
        st.push(ch)

    reverse_str = ""
    while st.size() != 0:
        reverse_str += st.pop()

    return reverse_str

def is_balanced(str):
    st = Stack()

    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']

    for ch in str:
        if ch in open_list:
            st.push(ch)
        elif ch in close_list:
            pos = close_list.index(ch)
            if st.size() > 0 and (open_list[pos] == st.peek()):
                st.pop()
            else:
                return False

    if st.size() == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(reverse_string("We will conquere COVID-19"))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
