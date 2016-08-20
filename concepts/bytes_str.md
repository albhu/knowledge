## Bytes vs Strings
What is the `b` character I keep finding in front of quoted characters in Python? It is not so mysterious anymore after learning about how Python 2 vs 3 treats bytes and strings differently.
Python 3.x makes a clear distinction between these two types.

-`str` = `'...'` literals = a sequence of Unicode characters

-`bytes` = `b'...'` literals = a sequence of Octets

### Python 3.x
In SQL, think of `str` as `NVARCHAR` and `bytes` as `BLOB`.

You can `encode` a `str` to a `bytes` object:

```
'\uFEFF'.encode('UTF-8')
b'\xef\xbb\xbf'
```

### Python 2.x
Pre-3.0 versions of Python lacked this kind of distinction between text and binary data. Instead, there was:

-`unicode` = `u'...'` literals  = sequence of Unicode characters = `str` in Python 3.x

-`str` = '...' literals = sequence of bytes and characters
  - usually text with some unspecified coding

In order to make the transition between 2 and 3 smoother, the `b'...'` syntax was introduced to allow users to distinguish binary strings from text strings. The `b` prefix does nothing in Python 2, but allows `2to3` script not to convert it to Unicode strings in 3.x.
