## Why all the self in Python?

Is python selfish? I dunno. Let's look at an example

```
class BearClub(object):
  dues_paid = False
  def bears_happy(self):
    if not dues_paid:
      print "bears are pleased"
```

Let's use this class.

```
x = BearClub()
```

x is the BearClub with property dues_paid and function bears_happy.

```
x.bears_happy
```

This is equivalent to

```
BearClub.bears_happy
```

`self` refers to the bound variable or object.

```
x = BearClub()
print x.dues_paid
>> False
y = BearClub()
y.dues_paid = True
print y.dues_paid
>> True
print x.dues_paid
>> False
```

In the end, the first argument of every class method is always a reference to the current instance of the class. By convention this is always `self`, but it can be named anything like `this`.
