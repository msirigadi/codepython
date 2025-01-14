"""
Write a function in python that can reverse a string using stack data structure.
Use Stack class from the tutorial.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
"""

from Datastructures_Stack_BasicImplementation import Stack

def reverse_string(text):
    st = Stack()

    for ch in text:
        st.push(ch)

    rstr = ""
    while not st.is_empty():
        rstr += st.pop()

    return rstr

if __name__ == '__main__':
    print("Reverse str:", reverse_string("Happy moments in life"))
