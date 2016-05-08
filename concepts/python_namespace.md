## What's a Namespace in the context of Python?

Everything in Python is an object. The way to refer to an object is often through its name.

A **namespace** is a space that holds names. Each module has its own global namespace: two classes or two functions within a module cannot have the same name.

Since each namespace is isolated, same names in two modules can refer to different objects. For example, the `Monkey` and `Grocery` module can have a function called `banana()`. This function can be accessed by `Monkey.banana()` or `Grocery.banana()`.

Whenever a python script is run, the interpreter treats the file as a module called `__main__`, which has its own namespace.

## Importing Modules

1) `import SomeModule`  

The simplest way to import a module. This import allows access to all the names in the namespace provided the module's name is used as a prefix (e.g., SomeModule.add()).
This implies the names in your program can have the same names as the imported module and both can be used.  

2) `from SomeModule import SomeName`  

This imports the SomeName's names directly into the namespace. This gives the ability to refer to a name in `SomeName` without using a prefix. Therefore, same names, those in the program and those imported, cannot be the same.  

3) `from SomeModule import *`  
This import should not really be used. All the names in the `SomeModule` are add to the program's namespace, causing **namespace pollution**.

## Scoping

Scoping refers to the region a program where a namespace can be accessed without a prefix. At any time there are many scopes for an operation: 1) scope within a function 2) scope within a module 3) scope of the Python builtins.

The nesting of scopes means that one function can't access a name in another function.

## Classes

Classes have a special relationship with namespaces because they do not have their own global namespace (the modules does). Therefore, the only way a class can access its variables or functions as names is to first refer to itself. The `self` argument is passed first for a class to access its attributes.
