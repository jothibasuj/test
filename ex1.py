print "welcome to git comment learning"

# This will destroy any local modifications.
# Don't do it if you have uncommitted work you want to keep.
git reset --hard 4f87f48897e13029c7826babf761ad44fe65abfc

# consider modify files no need to add with green color staus .
git reset --soft 4f87f48897e13029c7826babf761ad44fe65abfc

# consider new files need to add with red color status.
git reset 4f87f48897e13029c7826babf761ad44fe65abfc

 # Moves pointer back to previous HEAD
git reset --soft HEAD@{1}
git commit -m "Revert to 56e05fced"

#Hide permission changed files from git status
git config core.fileMode false

# Now you want to switch branches, but you don’t want to commit what you’ve been working on yet; so you’ll stash the changes. To push a new stash onto your stack, run git stash or git stash save:
$ git stash

# your changes are stored on your stack. To see which stashes you’ve stored, you can use git stash list:
$ git stash list

# if you want apply all stash use the following command.
$ git stash apply

# for particular stash use the following command
git stash apply stash@{2}

ref - https://stackoverflow.com/questions/4114095/how-to-revert-a-git-repository-to-a-previous-commit