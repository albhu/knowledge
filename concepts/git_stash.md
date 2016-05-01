## Git Stash
`git stash` is a convenient way to save work on a branch that is not ready for a commit before switching to a new branch  
When you want to apply a stash, you can use the following commands  
- `git stash list` - see which stashes are stored
- `git stash apply` - applies the first stash; if a specific stash is needed, use `git stash apply stash@{n}`
- alternatively, if we want the stash applied and removed, use `git stash pop` or `git stash pop stash@{n}`
