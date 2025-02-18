def function_with_uncommon_error(x):
    try:
        result = 1 / x
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid input type. Please provide a number.")
        return None
    return result

print(function_with_uncommon_error(0))
print(function_with_uncommon_error(2))
print(function_with_uncommon_error("abc"))