def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # or handle it in a more appropriate way

result = my_function(10, 0)
print(result)  # Output: 0