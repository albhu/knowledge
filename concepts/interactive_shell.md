## Interactive Shell

`-i` in a bash script allows users to interact with the shell.

```
case "$-" in
*i*)  echo This shell is interactive ;;
*)  echo This shell is not interactive ;;
esac
```
