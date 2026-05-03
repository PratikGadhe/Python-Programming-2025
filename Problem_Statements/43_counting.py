"""
43. Count Lines, Words, Characters
Problem Statement:
Write a program to count lines, words, and characters in a text.
Input:
 Multi-line string
Output:
 Line count, word count, character count
Example:
Input: "Hello\nWorld"
Output: Lines = 2, Words = 2, Characters = 10
"""
string = "Hello\nWorld"
line = 0
words = 0
char = 0
for i in string:
    if(65 <= ord(i) <= 90 or 97 <= ord(i) <= 123):
        char+=1
    