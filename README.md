{% steps %} 
{% step title="Introduction" %}

Welcome to the **Guided: Git Basics** lab 🚀.

In this Guided Code Lab, you will learn the essentials of using Git, a distributed version control system that's an industry standard for managing changes to code. You will practice Git commands by working with a Python game called Pywords. During the lab, you'll initialize a new Git repository, track changes, commit them, and simulate collaborating with other developers by pushing updates.

### Pre-requisites
- Basic understanding of Python programming
- Familiarity with command-line operations

### Learning Objectives
- Initialize a new Git repository.
- Understand and use basic Git commands like `git clone`, `git status`, `git log`, `git add`, `git commit`, and `git push`.
- Create a `README.md` file and push it to the `remote-repo`.
- Add a new features and push it to the `remote-repo`.

First let's clarify what Git is and why it's so important:

Git is a version control system that helps track changes in files. When working on a project, especially in teams, it's crucial to manage different versions of your codebase efficiently. This is where Git shines, allowing multiple developers to work together without overwriting each other's contributions.

Click the arrow to move to the next step.

{% /step %} 

{% step title="Basic Setup and Configuration" %}

Before you dive into the core activities of this lab, it's essential to ensure that your Git environment is correctly set up. This involves configuring Git with your personal information, which will be used in your commits. Each commit in Git is associated with a name and an email address, and this information is crucial for collaborative work and maintaining a clear history of who did what.

### Setting Up Your Git Identity

**Configure Your Email Address**

   First, you'll need to set the email address that will be associated with your Git commits. This should be the same email address that you use for your Git repository service (like GitHub, GitLab, etc.). To set your email address globally in Git, use the following command:

   ```bash
   git config --global user.email "you@example.com"
   ```

   Replace `you@example.com` with your actual email address.

**Configure Your Username**

   Next, set your name. This name will appear as the author in each commit you make. To set your name globally in Git, use the command:

   ```bash
   git config --global user.name "Your Name"
   ```

   Replace `Your Name` with the name you want to appear in your commits.

   #### Why is this Important?

- **Commit Tracking:** Git tracks who makes each commit by using the name and email address. This is crucial in a collaborative environment where multiple people are working on the same project.
- **Accountability and Credit:** Your name and email in commits help in attributing the work to you, ensuring you get credit for your contributions.
- **Consistency Across Environments:** By setting these configurations globally, your Git identity remains consistent across all the repositories you work on your machine.

---

After completing these steps, you'll be ready to start using Git more effectively, with your identity properly established for all your contributions. This is a fundamental step in setting up a professional and organized coding environment.

Click the arrow to move to the next step.

{% /step %} 


{% step title="Hands-On: Working with Git" %}
Let's start by cloning the `remote-repo` which is where you will be adding your new code.

In the **Terminal** to your right execute:

```bash
git clone remote-repo cloned-repo
```
This command clones the `remote-repo` into your working directory and names it `cloned-repo`.

Change into your new repo with the following command:
```bash
cd cloned-repo
``` 

Check the status of your new repo with:

```bash
git status
```

You should see the following message:

```bash
On branch pywords
Your branch is up to date with 'origin/pywords'.

nothing to commit, working tree clean
```

Now that you have a working repo, let's create a new file. 

Inside the directory run the following command:

```bash
echo "This is our new README" > README.md
```

Check the status again to confirm that the files are now being tracked.

You should see the following:
```bash
On branch pywords
Your branch is up to date with 'origin/pywords'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```
Next, add your new file to staging with the following command:

```bash
git add README.md
```

Again let's check the status.
You should see the following:

```bash
On branch pywords
Your branch is up to date with 'origin/pywords'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

```

Now you can make your first commit with a message describing the changes you've made:

```bash
git commit -m "Adds README.md"
```

Check the log to see your commit:

```bash
git log
```

You should see a simlar message with your email, username, and commit message:

```bash
commit 0e44b5409da38282cdd736eabec9235c6e58d168 (HEAD -> pywords)
Author: Your Name <you@example.comgit config --global user.name Your>
Date:   Wed Nov 15 20:19:15 2023 +0000

    adds README.md
```
--- 

Click the arrow to move to the next step.

{% /step %} 

{% step title="Pushing to a Remote Repository" %}

Let's push your commits to the `pywords` branch of the remote repository with the following command:

```bash
git push origin pywords
```

You should see a similar output:

```bash
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 325 bytes | 325.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To /home/ps-user/workspace/remote-repo
   cf924b3..0e44b54  pywords -> pywords
```
---

Congratulations! You've not only learned the basics of Git, but you have also experienced a collaborative development scenario. You've added a README and a new feature to an existing game and synchronized your changes with a remote repository.

{% /step %} 
{% /steps %}





