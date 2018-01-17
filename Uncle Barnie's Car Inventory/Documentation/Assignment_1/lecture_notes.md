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

### Variables:

_____
 

Variables *CAN*:

1. Have an unlimited length
2. Have __ in front of their name. The __ makes them a private variable.
3. Can start with a capital letter or contain capital letters IE: ViSItoRCoUnTeR.  However, good rule is to not do something like that in your code.
4. Contain _ or - in their names.

Variables *CANNOT*:

1. Be a keyword of the python language.  Keywords are reserved words that do a specific function in the programing language. IE: in, pass, None.
2. Contain spaces.
3. start with a number.

### Keywords:

Keywords as stated above are words reserved for the python language.  This means they cannot be changed from their initial function.

The reasoning behind this is to have one particular keyword do one thing.  For instance, you wouldn't want pass in your code to mean something different than pass in someone else's.

### Private and Public variables:

> Since we are just starting on our journey of python and programming I wanted to take a moment to do a quick insert about security.  It honestly should be the first thing you think about when you develop anything on the computer.  Your code can be taken and if exploits are found your company or yourself could be seriously ruined from it.  Take the recent hacks at Sony, Home Depot, Yahoo, Equifax to heart.


There are some obvious safeguards that you can do to protect against this.  Don't put secrets inside your code!


Since we got that common sense out of the way private variables are specific to a class or function that they are created in.

Take the following code:

```python
class FooBar:
        ___secret_text = 'This should not be accessed anywhere else.'
        name = ''
        def __info(self):
           print ('I am in class FooBar')
        def hello_world(self):
           print "Hello {0}! The secret text is {1}".format(self.name,FooBar.___secret_text)
foo = FooBar()
foo.name = 'Scott'
foo.hello_world()
# foo.__info() This would result in a failure.
#So would foo.__secret_text
```

The class FooBar has a private text string 'This should not be accessed anywhere else' and also a private info function that specifies it is inside the class.
Private variables are not necessarily for security but are provided for programmers to understand what functions or variables are important to the class and others that we can call and manipulate.  

### Syntax

Syntax is the way code is formatted and read by a fellow programmer and the computer that it can be run on.

Python is very light with syntax rules let's decompose the following function.
```python
#def stands for define a function.
#function_name is the variable name for the function.
#The () are used for passing in other variables.
#The : at the end of the function states that anything indented after that line is part of the function.
def function_name():
    #Since this indented it is a part of the function.
    print('Hello there')
#This is not part of the function and can run at any time.
print('This is out of scope')
#When you want to run a function you can call it.
function_name()
```

So for syntax the rules are:

1. Whitespace is important (indentation is key!)
2. Functions start with the keyword def while classes start with class
3. Function, class, loops all begin their code block with a :


Here is a block of c++ code.
```cpp
// my first program in C++
#include <iostream>

int main()
{
  std::cout << "Hello World!";
}

```

1. White space is not important but still utilized to show where code will run
2. Every command must end with a ';'
3. All function code must be put inside { }
4. Program must contain an int main to run

As you can see there are some differences between the code however one thing remains similar.  The structure of the code where the code inside the function is indented to show that it should run inside the function.  Python just took this similarity and allowed it to be the defining way the python interpreter understands what is a part of certain function, class or logical loop.