

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def is_even(num):
    return num%2 == 0
        
    
def is_odd(num):
    return num%2 != 0

def max_num(list):
    return max(list)

def min_num(list):
    return min(list)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_string(text):
    return text[::-1]

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result    



