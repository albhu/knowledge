## Bash Recursion

The `for` loop is a little bit different from other programming languages. Basically, it let's you iterate over a series of 'words' within a string

The `while` executes a piece of code if the control expression is true, and only stops when it is false (or a explicit break is found within the executed code.

The `until` loop is almost equal to the while loop, except that the code is executed while the control expression evaluates to false.

```
for f in /tmp/* tmp/**/* ; do
  ...
done;
```

```
i="0"

while [ $i -lt 4 ]
do
xterm &
i=$[$i+1]
done
```
