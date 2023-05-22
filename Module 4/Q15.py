# # Can One Block Of Except statements handle  multiple excdption >?
# , one block of except statements can handle multiple exceptions. Multiple exception types can be listed in a single except statement separated by commas. For example:

# ```
# try:
#     # some code that may raise exceptions
# except (TypeError, ValueError):
#     # handle both TypeError and ValueError exceptions
# except FileNotFoundError:
#     # handle FileNotFoundError exception
# except:
#     # handle all other exceptions
# ``` 

# In this example, the first except block handles both TypeError and ValueError exceptions, the second except block handles only FileNotFoundError exception, and the third except block handles all other exceptions.