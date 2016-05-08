## Git Commit Amend

When staged modifications should be rolled into a previous commit or if there are no staged modifications and the previous commit's message should be changed, use `git commit --amend`.

Similar to `git reset`, do not use this command in a public repo. The amended commit is an entirely **new** commit, potentially leading to confusion when a new commit replaced a snapshotted commit, which is now gone.
