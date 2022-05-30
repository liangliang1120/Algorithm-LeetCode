"""
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
Constraints:

[time limit] 5000ms

[input] array.character arr

0 ≤ arr.length ≤ 100
[output] array.character
"""

def reverse_helper(arr, start, end):
    while start < end:
      arr[start], arr[end] = arr[end], arr[start]
      start += 1
      end -= 1

def reverse_words(arr):
  #reverse all characters 
  n = len(arr)
  reverse_helper(arr, 0, n - 1)

  word_start = 0  
  for i in range(n + 1):
    if i == n or arr[i] == " ":   
      reverse_helper(arr, word_start, i - 1)
      word_start = i + 1
      
  return arr
