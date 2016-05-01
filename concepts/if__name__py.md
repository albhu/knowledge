# if __name__ == '__main__'

The `if __name__ == '__main__'` is an important conditional to use when a python file is intended to be imported as a module or executed directly.  
When a py file is executed directly, the `__name__` variable is `__main__`. If the file is imported from another file, the `__name__` variable will be set to the module's name.  
The conditional allows the file to be run standalone when it's executed from the file directly and allows functions to be called and not executed directly when it is imported as a module.
