## Undoing a commit

Undoing a commit does not have to be scary. Let's illustrate how to do this by example.

C is the HEAD and (F) is the state of your files.

```
   (F)
A-B-C
    ^
   (master)
```

If you want to nuke commit C, you can use `git reset --hard HEAD~1`

```
 (F)
A-B
  ^
(master)
```

Making a mistake at this step is not terrible. You can type in `git reflog` to return a list of commits. To ressurect the commit you destroyed, you can do this: `git checkout -b <newBranch> <shaYOudestroyed>`.

Ok, what if you don't want to nuke commit C but undo the commit so you can make additional changes and commit after? Leave off the --hard from the command above `git reset HEAD~1`.

```
   (F)
A-B-C
  ^
 (master)
```

If you include `--soft` in the command`, you can undo the commit and leave the files AND the index.

