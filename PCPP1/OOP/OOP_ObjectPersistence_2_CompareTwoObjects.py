"""
In order to compare two objects, you should start with the '==' operator as
usual. This operator compares the values of both operands and checks for value
equality. So here we witness a values comparison.

In fact, two distinct objects holding the same values could be compared, and
the result would be 'True'. Moreover, when you compare two variables
referencing the same object, the result would be also 'True'.

To check whether both operands refer to the same object or not, you should use
the 'is' operator. In other words, it responds to the question: “Are both
variables referring to the same identity?”
"""

a_string = ['10', 'days', 'to', 'departure']
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)

print()

a_string = ['10', 'days', 'to', 'departure']
b_string = ['10', 'days', 'to', 'departure']

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)