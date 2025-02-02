"""
Given a string check if it is a palindrome (ignoring cases and non-alphanumeric characters)

---->> two pointer approach
one pointer starts from the left , another from the left
compare characters and move pointer inward

Time Complexity: O(n)
Space Complexity: O(1)

"""

import re

def is_palindrome(s):

    s = re.sub(r'[^a-zA-Z0-9]','',s).lower()  ### removing non-alphanum charcters
    left, right = 0, len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("A man, a plan, a canal: Panama"))