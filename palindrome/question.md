## Basic Palindrome Questions

Check if a given string is a palindrome.

Example: "racecar" → True, "hello" → False

Approach: Two pointers or string slicing.


Check if a number is a palindrome (without converting it to a string).

Example: 121 → True, 123 → False

Approach: Reverse half of the number and compare.


Find the longest palindromic substring in a given string.

Example: "babad" → "bab" or "aba"

Approach: Expand around center or Dynamic Programming (O(n^2)).


Find the longest palindromic subsequence.

Example: "bbbab" → "bbbb" (length = 4)

Approach: Dynamic Programming (O(n^2)).


## Palindrome Variations

Check if a string can become a palindrome by removing at most one character.

Example: "abca" → True (remove 'c' to get "aba")

Approach: Two pointers (O(n)).



Check if a string is a k-palindrome (can be made a palindrome by removing at most k characters).

Example: "abcdeca", k=2 → True

Approach: Recursion or DP (O(n^2)).


Check if a string can be rearranged into a palindrome.

Example: "civic" → True, "ivicc" → True, "hello" → False

Approach: A palindrome has at most one odd-frequency character (O(n)).


Find the minimum insertions needed to make a string a palindrome.

Example: "abc" → Insert 'b' or 'c' to get "aba" or "cbc".

Approach: DP (O(n^2)).


## Palindromes in Data Structures

Find the longest palindrome in a linked list.

Approach: Convert to a string, or use slow and fast pointers with a stack.


Check if a linked list is a palindrome.

Approach: Reverse the second half and compare (O(n) time, O(1) space).


Find all palindromic partitions of a string.

Example: "aab" → ["aa", "b"], ["a", "a", "b"]

Approach: Backtracking (O(2^n) complexity)


## Palindrome in Numbers

Check if a number is a palindrome without extra space.

Approach: Reverse half of the digits and compare (O(log n)).


Find the next smallest palindrome greater than a given number.

Example: 123 → 131, 999 → 1001

Approach: Generate candidates and check.


Find the closest palindrome to a given number.

Example: 123 → 121, 1000 → 999

Approach: Generate neighbors (O(log n)).

## Palindrome and Graphs/Advanced Topics

Find the shortest palindrome by adding characters at the beginning.

Example: "abcd" → "dcbabcd"

Approach: KMP algorithm (O(n)).


Find palindromic paths in a grid.

Given a m × n matrix, find paths that form palindromes.


Find all palindromic permutations of a string.

Example: "aabb" → ["abba", "baab"]

Approach: Backtracking.


Find the number of palindromic substrings in a string.

Example: "aaa" → 6 ("a", "a", "a", "aa", "aa", "aaa")

Approach: Expand around center (O(n^2)).



## Complexity Summary

-----------------------------------------------------------------------------------------------------------------------------------
             Problem	                                   Best Approach	          Time Complexity	          Space Complexity
-----------------------------------------------------------------------------------------------------------------------------------            
             Check if a string is a palindrome             Two Pointers	              O(n)	                         O(1)
-----------------------------------------------------------------------------------------------------------------------------------
             Check if a number is a palindrome	           Reverse half	              O(log n)	                     O(1)
-----------------------------------------------------------------------------------------------------------------------------------
             Longest palindromic substring	               Expand Around Center	      O(n^2)	                     O(1)
-----------------------------------------------------------------------------------------------------------------------------------
             Longest palindromic subsequence	           DP	                      O(n^2)	                     O(n^2)
------------------------------------------------------------------------------------------------------------------------------------
             Check if string is a k-palindrome	           Recursion/DP	              O(n^2)	                     O(n^2)
------------------------------------------------------------------------------------------------------------------------------------
             Minimum insertions to make palindrome	       DP	                      O(n^2)	                     O(n^2)
------------------------------------------------------------------------------------------------------------------------------------
             Check if a linked list is palindrome	       Reverse Second Half	      O(n)	                         O(1)
------------------------------------------------------------------------------------------------------------------------------------
             Palindromic partitioning	                   Backtracking	              O(2^n)	                     O(n)
------------------------------------------------------------------------------------------------------------------------------------
             Count palindromic substrings	               Expand Around Center	      O(n^2)	                     O(1)