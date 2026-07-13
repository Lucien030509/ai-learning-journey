# Week 1: Simple calculator
# 处理除零错误

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Test
print(add(10, 5))       # 15
print(divide(10, 0))    # Error message
print(divide(10, 2))    # 5.0
