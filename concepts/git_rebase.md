## Git Rebase

The command `git rebase` moves branches around by changing the commits they are based on. The rebase command allows branches to maintain a linear history.

Example
```
git checkout new_feature
git rebase master
```
The commits on the `new_feature` will be moved to the tip of the `master` branch. When performing a rebase, the branch that needs to be rebased should be checked out. The rebase command moves the checked out branch to the tip of the target branch e.g., `git rebase <target branch>`.

The rebase allows the integration of the most updated version of `master` without a merge commit (no fast-forward merge behavior. history looks like a railroad track instead of a straight line).

## Git Rebase (interactively)

`git rebase -i master` allows the ability to modify commits, cleaning up history.  
- rearrange commit order
- `squash` combine commit with the previous one
- `edit` amend a commit

Examples of squash

```
pick 5cf316e Add empty page in about section
squash 964e013 Add contents to about page
pick 89db9ab Add HTML page for personal bio
squash 2bda8e5 Add empty HTML page for Mary's bio
pick 915466f Add link to about section in home page
```

1. Git moves 5cf316e to the tip of master
2. Git combines the snapshots of 964e013 and 5cf316e
3. Git asks you what commit message for the combined shapshot
4. repeat

## Continue or abandon rebase

Move on with rebase `git rebase --continue`
If you messed up `git rebase --abort`

## Going fast-forward

With the rebase, the history is clean, but the final snapshot does not provide how we arrived to the current state.  

```
git checkout master
git merge new_feature
```
