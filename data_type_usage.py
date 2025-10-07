# Practical 1: Python Data Types and If/Else Clauses
# BIO511 Genomics - Python Introduction
# Author: (Amanda)
# Date: October 7, 2025

# -------------------------------
# Part 2.1 — Data Type Usage
# -------------------------------

# Here we create one variable for each data type

my_int = 4
my_float = 3.14
my_string = "Hello"
my_bool = True
my_none = None
my_list = [1, 2, 3]
my_dict = {"name": "Amanda", "age": 25}
my_tuple = (10, 20, 30)
my_set = {1, 2, 3}
my_range = range(5)

# Print value and type for each variable
print("=== Part 2.1: Values and Types ===")
print("Integer:", my_int, "Type:", type(my_int))
print("Float:", my_float, "Type:", type(my_float))
print("String:", my_string, "Type:", type(my_string))
print("Boolean:", my_bool, "Type:", type(my_bool))
print("NoneType:", my_none, "Type:", type(my_none))
print("List:", my_list, "Type:", type(my_list))
print("Dictionary:", my_dict, "Type:", type(my_dict))
print("Tuple:", my_tuple, "Type:", type(my_tuple))
print("Set:", my_set, "Type:", type(my_set))
print("Range:", my_range, "Type:", type(my_range))


# -------------------------------
# Part 2.2 — If/Elif/Else on data types
# -------------------------------

# 2.2.1 — Check if STRING is empty
print("\n=== 2.2.1: String check ===")
if len(my_string) == 0:
    print("empty")
else:
    print("non-empty")


# 2.2.2 — Check INTEGER: positive, zero, or negative
print("\n=== 2.2.2: Integer check ===")
if my_int > 0:
    print("positive")
elif my_int == 0:
    print("zero")
else:
    print("negative")


# 2.2.3 — Nested if: check SEQUENCE (list, tuple, or range)
print("\n=== 2.2.3: Sequence check ===")

seq = my_list  # Try changing this to my_tuple or my_range

# Outer if: type gate
if type(seq) is list or type(seq) is tuple or type(seq) is range:
    # Inner if: length check
    if len(seq) == 0:
        print("empty")
    elif len(seq) == 1:
        print("single item")
    else:
        print("multiple items")
else:
    print("wrong type for this task")