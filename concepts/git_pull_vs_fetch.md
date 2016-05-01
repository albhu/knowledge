## Git Pull vs Git Fetch
`git pull` merges all commits from the remote branch into the current branch. `git pull` = `git fetch` + `git merge`.  
`git fetch` gathers any commits from the target branch that does not exist in your current branch and stores them in your local repository. After using `git fetch`, `git diff ...origin` can be used to see any changes.
