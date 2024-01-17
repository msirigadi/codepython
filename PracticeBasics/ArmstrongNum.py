"""
Given a number x, determine whether the given number is Armstrong number or not.
A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
Example:

Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9
"""

# Solution1

def power(digit, n):
    po = 1
    while n > 0:
        po *= digit
        n -= 1

    return po

def armstrong(num):
    sum = 0
    length = len(str(num))
    n = num
    while n > 0:
        digit = n%10
        n = n//10
        #sum += power(digit, length)
        sum += digit**length
        print(sum)

    return sum == num

print(armstrong(153))
