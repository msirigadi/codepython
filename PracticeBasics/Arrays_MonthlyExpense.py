"""
1.Let us say your expense for every month are listed below,

January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""

expenses = [2200, 2350, 2600, 2130, 2190]

print("Dollars spent extra compared to Jan are {}".format(expenses[1] - expenses[0]))
print("Total expenses in first quarter are {}".format(expenses[0] + expenses[1] + expenses[2]))

spent_2000 = False
for exp in expenses:
    if exp == 2000:
        spent_2000 = True
        break

if spent_2000:
    print("Spent exactly 2000 in a month")
else:
    print("Did not spent exactly 2000 in any month")
expenses.append(1980)
expenses[3] = expenses[3] - 200

print("Final expenses: ", expenses)
