
'''
https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

sum = 0

print("Please enter an maximum number that you want")

N = int(input())

for i in range(1, N):
    if (i % 3 == 0) or (i % 5) == 0:
        sum += i
print(f"Sum of all multiples of 3 or 5 below {N} is {sum}")
