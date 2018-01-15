### Github setup

1. Create an account.
2. Link it to pycharm.
3. Create a separate branch to do work in.
4. Submit a PR when assignment is done.

### What is Github?

Github is a UI (user interface) built over a popular version control engine called Git.  The easiest way to understand what git does is to think of it in a senario:

You are working on a project with a team and while you are making changes to a document someone else on your team makes different changes to the same document.  Your teammate submits her changes and then you go to submit your changes.  
> How could you keep your changes and your teammates changes without knowning she was in the file as well?

**The answer is Git.**

Git is a service that keeps track of files that are being changed and keeps state for you.  For instance with the above example there would be three states of the same file.  
1. The Master - The original document before your changes or your teammates.
2. Your version - The changes you made to the document.
3. Your Teammates version - The changes she made to the document.

How does it keep track of all of this?  Well, it has one central place to refer to, the Master Document.

Example Workflow:

![Image of Github Flow Logic](https://github.com/ScottSnyder11/LearnPython2017/blob/master/Uncle%20Barnie's%20Car%20Inventory/Images/github_workflow.jpg?raw=true)



### Python

We will be utilizing Python in this class.  There are multiple programming languages and choosing the right one for the job can be certainly troubling as there are so many.  

Our reasons for choosing python are the following:
1. It's open-source offerings (fellow developers writing code to do X,Y,Z and we use it instead of writing our own.)
2. Easy syntax and format is uniform. (All python code should be formatted in a similar manner)
3. Interpeter is smart. (The thing that runs our code understands our code and data types)


### Data Types and Variables
Data types are exactly what you think it means.  How the data is represented.  For instance, is it a number? Is it text? What if it is a price for an item?  Those are all datatypes and luckily for us -- the python interpeter does most of the heavy lifting for us.

The following code:

```python
first_name = 'Scott'
```
The interpeter understands that first_name is a string (or a text data type). 
```python
age = 27
```
The Interpeter understand that age is an integer or a number data type.

Now, if you also look at the two examples first_name and age are both something called variables.  These are values that are stored in computer memory that the program can access *until the interpeter deletes them*.


