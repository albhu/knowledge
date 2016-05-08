## Git Fast Forward vs. Non-Fast Forward

What is the difference between `-ff` and `non-ff`?

Non-fast forward git merges keeps an explicit notion of feature branches. Each feature branch is treated as a **unit** composed of several commits. After a branch is merged, a commit (merge commit) is created making it clear when a branch was merged.

Fast forward creates a linear snapshot history. However, identifying the commits that created a feature is difficult because non merge commits were created. In most cases, a non fast-forward merge provides a more detailed history with the cost of empty commits (merge commits).
