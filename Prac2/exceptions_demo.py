"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when user enter the letter(qdsae) and non numerical number
2. When will a ZeroDivisionError occur?
when user enter the letter(qdsae) and non numerical number and enter zero())
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
We should use the while loop when user enter the wrong input the program allow to enter the denominator
 until user enter the numerical number
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")