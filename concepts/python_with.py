### The Lovely Python WITH

`with` is a python statement that encapsulates a class that runs a function and "tears it down". An example of this pattern would be opening and closing a file.

In longhand, this would could look like

```python
def controlled_execution(callback):
  set things up
  try:
    callback(thing)
  finally:
    tear things down

def my_function(thing):
  do something

controlled_execution(my_function)
```

This is verbose.

```python
class controlled_execution:
  def __enter__(self): # "context guard" assigns whatever __enter__ returns to the variable given by as
    set things up
    return thing

  def __exit__(self, type, value, traceback):
    tear things down

with controlled_execution() as thing:
  some code
```
In Python 2.5, the file object has been equipped with `__enter__` and `__exit__` methods. The former return the file object, and the latter closes the file.
