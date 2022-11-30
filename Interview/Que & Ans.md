Git:
---
* Git add:- Add one or more files to the staging area
            git add
* Git commit:- Commit changes to head but not to the remote repository
            git commit -m "Commit messege"
* Git push:- Our file push to remote repository
            git push origin <branch name>

* Git config:- Configure the username and email address
            This command will add a username
            git config –global user.name “Your Name”

            This command will add an email id.
            git config –global user.email “Your E-mail Address”
            
* Git init:- create an empty repository while working on a project.
* Git log:- displays all of the commits in a repository's history
* Git diff:- View the changes made to the file

* Git Fetch:- Git fetch command only downloads new data from a remote repository.
            It does not integrate any of these new data into your working files.

* Git Pull:- Git pull updates the current HEAD branch with the latest changes from the remote server.
            Downloads new data and integrate it with the current working files.

* Git checkout:- The git checkout command is used to switch between branches in a repository. 
            Create a new branch
            git branch <branch_name>

            Create a new branch and switch to new branch
	        git checkout -b <branch name>  
	        Sometimes this command can be dangerous because there is no undo option available on this command.

* Git Merge:- Generally, git merge is used to combine two branches.
            The git merge command you to take the data created by git branch and integrate them into a single branch
            git merge <branch_name>

* Git Reset:- reset is the command we use when we want to move the repository back to a previous commit
            git reset

* Git Revert:- It is an undo type command. it will create a new change with the specified commit.
            If You have unfortunately delete any files by using below command it will bring up
            git revert git revert <commit_ish>  

* How to change any older commit messages?
            git commit --amend -m "New commit message"            



