GitHub Guide 

1. Log into GitHub on your browser and navigate to (https://github.com/madesai22/ocean-ml)

2. Navigate to the right side of the window and click "Fork." This will save a new copy of the repository in your GitHUb account

3. Open Terminal. Decide where you want to store your GitHub resository on your computer, and navigate to that place. I made a folder in my Documents called "InternGit", and I store this respository there. 
Remember: 
* to make a directory use **mkdir /path/to/directoryname**
* to navigate to a directory use **cd /path/to/directoryname**

4. Once you're in the right location, clone the repository. This adds a local copy to your own computer, and you can make changes there! 
* In your browser, go to your GitHub account, open the repositories tab, find the forked repository, and click on the green button on the right side that says "clone or download." Copy the URL it gives you.
* In Terminal, type **git clone <url>**, where **<url>** is the URL of your forked repository that you just copied from GitHub
* Make sure you're cloning your *forked* respository, not the original. You can tell because in the top left corner, where it says the name of the repository, it will have a description that identifies where it was forked from.

5. When you clone a repository, GitHub automatically creates a remote called origin that lets you interact with the online repository and make or download changes. Type **git remote -v** in Terminal to see a list of your remotes.

6. Add me as a collaborator to your repository — that way, I'll be able to see your work and integrate it into the main repository. In your browser, under settings in your repository, visit "Collaborators & teams" and add my username (madesai22) into the "Add collaborators" box. 

7. Now, we'll add a new remote that points to the original repository — the one that you forked your own repository from. This way, if any changes are made to that original repository, you will be able to download them.
* Type git remote add upstream https://github.com/madesai22/ocean-ml
* Now, type git remote -v again. You should see two remotes: One called origin that points to your own repository, and one called upstream that points to the original. 

8. Create a new branch in your repository. This allows you to make changes to your repository (i.e. to edit Jupyter Notebooks or write new code) without changing the main, master branch.
* Type git checkout -b <branch-name>. This creates a new branch and switches you over to that new branch in git.

************************************
 ~ Break to visit climate wall ~
In pairs: pick a question
1. What are some of the impacts of climate change (local and global)?
2. What are some of the main drivers of climate change?
3. How does the information on the climate wall relate to our project?
***********************************


9. 