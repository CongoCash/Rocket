Project Repo Setup
=====================

Collaborative development on GitHub is a common theme in most
organizations. GitHub has made it really simple to push, pull and merge changes
from others. There are two basic collaborative models, namely, *Fork & Pull*
and *Shared repository model.* *Fork & Pull* models has become the standard for
open source projects on GitHub and we'll walk through the model step by
step. If you are curious, read more about
[collaborative models on GitHub.](https://help.github.com/articles/using-pull-requests/)

### Roles

Let's assume that there is one project manager(PM) and a few team members
working on a single project. The PM sets up the repository that everyone is
expected to work on. The PM is also responsible for merging all changes and
making a release. Individual team members develop mostly in isolation but can
pull changes from others and make theirs available.

### Organization and project setup

Each team is expected to have one Organization and within it, one repository
per project. Some of the following instructions are only for the PM of the
team. They are labeled **(PM only)**. Others are for everyone in the team and
labeled **(Everyone)**

#### 1. Create an Organization (PM only)

* Go to your personal settings page and click on Organizations.
* Click on **New organization** button and give it a name of your choice.
* Before clicking the **Finish** button, invite your teammates to your
  organization's owners team.

#### 2. Create a project repo (PM only)

* Create a project repo by clicking the **New repository** button on your
Organization page.
* Make sure to initialize the repository with a README.

#### 3. Fork the project repo (Everyone)

* Click the **Fork** button on the project repo page and choose the fork to be
in your personal github account.
* Make sure to fork your organization's project repo and not the personal fork of a team member.
* Upon success, you'll be redirected to your forked repo's page.

#### 4. Add collaborators to your fork (PM only)

This is a notable deviation from the vanilla *Fork & Pull* model. The PM adds
collaborators to her fork, allowing teammates to push changes to it. This will
reduce additional steps that are otherwise necessary.

* In the fork page, click the settings link in the right navbar.
* In the next screen, add each of your teammates as a collaborator.

#### 5. Clone your fork on to your laptop (Everyone)

* Enter this command from an appropriate directory.

  ```
  git clone git@github.com:YOUR_USERNAME/YOUR_PROJECT_NAME.git
  ```

#### 6. Create a new branch (PM only)

You'll have at least one branch per project. The idea is to make all
necessary changes to your project in this branch. You may want to plan your
project to have a few milestones. If so, we suggest a new branch per
milestone to nicely showcase your progress.

* Create a branch in your clone. Choose a sensible name

  ```
  git checkout -b YOUR_BRANCH_NAME
  ```

#### 7. Initial commit and push (PM only)

* Update the README.md file with your project description.

  ```vim README.md # edit and save```

  ```git add README.md```

  ```git commit -m 'initial commit' README.md```

* Push the branch to your origin

  ```
  git push origin YOUR_BRANCH_NAME
  ```

#### 9. Create a pull request (PM only)

* Go to the github page of your fork and you'll see a **compare and pull request** button. Click on it.
* Click on **create pull request** button in the next screen.
* DO NOT merge the pull request you just created. You'll merge after you have
  tested and satified with intended changes for the branch.

#### 10. Pull and start working on the branch (Everyone)

* Once the pull request is created, everyone on the team should pull the branch.
* There are two commands to achieve this and they are provided in the *Pull Request* page. `https://github.com/YOUR_ORGANIZATION/YOUR_PROJECT_NAME/pulls`

  ```git checkout -b PM_USERNAME-YOUR_BRANCH_NAME master```

  ```git pull https://github.com/PM_USERNAME/YOUR_PROJECT_NAME.git YOUR_BRANCH_NAME```

* You can now start working in the branch that's just created and checked out.

#### 11. Pulling and Pushing subsequent changes (Everyone)

* Pull changes from your teammates with this command.

  ```
  git pull https://github.com/PM_USERNAME/YOUR_PROJECT_NAME.git YOUR_BRANCH_NAME
  ```

* Push changes to GitHub with this command.

  ```
  git push https://github.com/PM_USERNAME/YOUR_PROJECTS_NAME.git PM_USERNAME-YOUR_BRANCH_NAME:YOUR_BRANCH_NAME
  ```

#### 12. Merging Pull request (PM only)

* Once you are ready to merge, go to the *Pull Request* page. `https://github.com/YOUR_ORGANIZATION/YOUR_PROJECT_NAME/pulls`
* Click on **Merge pull request** button to merge it.

#### 13. Get ready for the next milestone (Everyone)

You may be done with your project with just one *Pull Request*. But what if you want to do more?

* Add a new remote (one time command)

  ```
  git remote add upstream https://github.com/YOUR_ORGANIZATION/YOUR_PROJECT_NAME.git
  ```

* Rebase your master to sync all changes to your local master branch

  ```
  git checkout master; git pull --rebase upstream master
  ```

* Go to Step 6 and repeat!
