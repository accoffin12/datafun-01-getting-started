# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:48:05 2023

@author: Tower
"""

"""
Optional bonus. See course site for details.

"""

import random

# Change the name below to a name of your choice

Joy = "Gamebot"

# Fix the code below to print the name using an f-string


print(f'{"Hello, Im Joy, your gamebot."}')
print()
print(f"""{"Let's play an animal guessing game!"}""")
print(f"""{"There are 3 animals: wolf, eagle, snake (a Python of course)."}""")
print(f"""{"The wolf scares the eagle."}""")
print(f"""{"The eagle grabs the snake."}""")
print(f"""{"The snake bites the wolf."}""")
print()
print(f"""{"I'll pick one and you pick one and we'll see who wins."}""")


# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function
print(f"{'Enter only Wolf, Eagle, or Snake as an animal.'}")
user_choice = value1 = input("Enter animal choice: ")
wolf = 3
snake = 2
eagle = 1

# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()


# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!


if user_choice > buddy_choice:
    print('User Won')
if user_choice < buddy_choice:
    print('I won.')
   
if user_choice == buddy_choice:
    print("We tied!")


# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into the
# docstring comment below.
# --------------------------------------------------------------------
"""
Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)]
Type "copyright", "credits" or "license" for more information.

IPython 7.31.1 -- An enhanced Interactive Python.

runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')

Enter animal choice: wolf

You said wolf.
I said wolf.

We tied!

runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: wolf

1

2

3

You said wolf.
I said snake.






runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: wolf

You said wolf.
I said snake.

Traceback (most recent call last):

  File "C:\Users\Tower\Documents\Data Analytics Sp 2023\Repositories\Reference Repo Sp 2023\datafun-01-getting-started\untitled0.py", line 53, in <module>
    minimum = wolf

NameError: name 'wolf' is not defined


runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: wolf

You said wolf.
I said eagle.

Snake won.
Eagle Won.

runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.

Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.

I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: wolf

You said wolf.
I said eagle.

The winner is 3

runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.

Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.

I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: wolf

You said wolf.
I said eagle.

Traceback (most recent call last):

  File "C:\Users\Tower\Documents\Data Analytics Sp 2023\Repositories\Reference Repo Sp 2023\datafun-01-getting-started\untitled0.py", line 59, in <module>
    if wolf > eagle:

TypeError: '>' not supported between instances of 'tuple' and 'int'


runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.

Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.

I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: wolf

You said wolf.
I said wolf.

The winner is 3
We tied!

snake
Out[8]: 2

runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.

Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.

I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: snake

You said snake.
I said snake.

The winner is 3
We tied!

runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.

Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.

I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: wolf

You said wolf.
I said eagle.

User Won

runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.

Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.

I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: snake

You said snake.
I said snake.

We tied!

runfile('C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started/untitled0.py', wdir='C:/Users/Tower/Documents/Data Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-01-getting-started')
Hello, Im Joy, your gamebot.

Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.

I'll pick one and you pick one and we'll see who wins.
Enter only Wolf, Eagle, or Snake as an animal.

Enter animal choice: eagle

You said eagle.
I said snake.

I won.



"""
