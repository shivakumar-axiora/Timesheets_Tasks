from typing import List

def add(a:float,b:float) -> float:
    """
    This function takes two numbers as input and returns their sum.\
    """
    return a+b

def sub(a:float,b:float) -> float:
    """
    This function takes two numbers as input and returns their difference.\
    """
    return a-b

def is_even(num: int) -> bool:
    """
    check if a number is Even
    """
    return num%2 == 0

def is_odd(num: int) -> bool:
    """
    check if a number is Odd
    """
    return num%2 != 0

def max_num(list: List[float]) -> float:
    """
    This function finds the max value in a list.
    """
    if not list:
        raise ValueError("List is empty.")
    return max(list)

def min_num(list: List[float]) -> float:
    """
    This function finds the min value in a list.
    """
    if not list:
        raise ValueError("List is empty.")
    return min(list)

def count_vowels(text: str) -> int:
    """
    This function counts the number of vowels in a string.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    vowels = "aeiouAEIOU"
    count = 0
    return sum(1 for char in text if char in vowels)

def reverse_string(text: str) -> str:
    """
    This function reverses a string.
    """
    if not isinstance(text,str):
        raise ValueError("Input must be a string.")
    return text[::-1]

def factorial(n: int) -> int:
    """
    This function calculates the factorial of a number.
    """
    if n<0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result    



