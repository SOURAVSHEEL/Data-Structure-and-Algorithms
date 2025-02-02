"""
check if a number is a palindrome without converting to string

a palindrome number reads the same forward and backward like 121, 
1331, 12321

"""
##  O(log n) or O(number of digits)
##  O(1) or constant

def checkPalindrome(n):

    reverse = 0
    temp = n
    while temp != 0:
        reverse = reverse * 10 + temp % 10
        temp = temp// 10
    return reverse == n

n = 12321
if checkPalindrome(n):
    print("true")
else:
    print('false')


"""
a more optimized approach is to reverse only half the number to avoid 
overflow and unnecesaary computations.
"""

def isPalindrome(n):

    if n < 0 or (n % 10 == 0 and n != 0):
        return False
    reversed_half = 0
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10
        n = n // 10
    return n == reversed_half or n == reversed_half // 10

print(isPalindrome(121))   
print(isPalindrome(12321))
