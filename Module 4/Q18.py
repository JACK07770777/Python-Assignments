# # How Do YOu Handle exceptions with try/except/finally in python
# In Python, exceptions can be handled using the `try`, `except`, and `finally` blocks.

# The `try` block is used to enclose the code that may raise an exception. If an exception is raised in the `try` block, the code in the corresponding `except` block(s) will be executed.

# The `except` block can contain one or more exception types that it will catch. If no exception types are specified, the `except` block will catch all exceptions.

# The `finally` block is optional and is always executed, regardless of whether an exception was raised or not. This block is typically used to perform cleanup operations, such as closing files or database connections.

# Here is an example of how to use `try`, `except`, and `finally` blocks in Python:

# ```
# try:
#     # code that may raise an exception
#     result = 10 / 0
# except ZeroDivisionError:
#     # handle the exception
#     print("Cannot divide by zero")
# finally:
#     # perform cleanup operations
#     print("Exiting the program")
# ```

# In this example, the `try` block tries to divide the number 10 by zero, which will raise a `ZeroDivisionError` exception. The `except` block catches