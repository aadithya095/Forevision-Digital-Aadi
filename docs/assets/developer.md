# Guide for developers
This guide contains rules and regulations for all developers to follow. It is divided in three sections: 
+ Common Grounds, 
+ Frontend 
+ Backend.

The rules and regulations mentioned in the Common Grounds are for all developers to follow while those mentioned in the Frontend section and Backend section are for the specific roles to follow.

## Common Grounds
### Git Commit Message Construction
When making changes to a project using Git, it's important to write clear and concise commit messages to keep track of the changes that have been made. 
The basic structure of the message is given below:
```commandline
git commit -m [tag] [description]
```
Here are the list of tags that can be used.
```
    feat: Use this tag when you're adding a new feature to the project.
    fix: Use this tag when you're fixing a bug in the project.
    refactor: Use this tag when you're making changes to the code without introducing new feature or fixing a bug.
    patch: Use this tag when you're making changes to the code that connects the frontend and backend, but doesn't change the overall meaning of the code.
    test: Use this tag when you're writing new tests or updating existing ones.
    docs: Use this tag when you're updating or writing new documentation.
    style: Use this tag when you're making changes to the style of the code, but not changing the overall meaning of the code.
    chore: Use this tag when you're doing things like updating dependencies, cleaning up files, or removing unnecessary directories.
```
It's important to be consistent with the use of these tags in order to keep track of the changes that have been made to the project.

The description should have these informations:
+ what did you do
+ where did you do
+ why did you do

The description of the changes made should be tailored to the specific requirements of the changes. For instance, when addressing a bug, it is essential to include the reasoning behind the fix. However, when implementing a new feature that has been mutually agreed upon and is outlined in the project's scope and requirements document, the reasoning may not be necessary. It is important to note that when introducing new features independently, a clear rationale should be provided

#### Example:
```commandline
git commit -m "feat admin login interface in customadmin directory"
git commit -m "refactor navbar style in admin login interface, customadmin directory, colors were changed as per clients requirement"
```