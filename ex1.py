print "welcome to git comment learning"

# This will destroy any local modifications.
# Don't do it if you have uncommitted work you want to keep.
git reset --hard 4f87f48897e13029c7826babf761ad44fe65abfc



# Resets index to former commit; replace '56e05fced' with your commit code
git reset 56e05fced 


# Moves pointer back to previous HEAD
git reset --soft HEAD@{1}
git commit -m "Revert to 56e05fced"