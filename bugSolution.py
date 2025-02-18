def function_with_uncommon_error_solution(x):
    try:
        x = float(x)  # Explicit type conversion
        result = 1 / x
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except (TypeError, ValueError):
        print("Error: Invalid input type. Please provide a number.")
        return None
    return result

print(function_with_uncommon_error_solution(0))
print(function_with_uncommon_error_solution(2))
print(function_with_uncommon_error_solution("abc"))
print(function_with_uncommon_error_solution(2.5))