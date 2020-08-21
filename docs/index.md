Error Handling & Pickling in Python
------

Rebecca Ly  
August 19, 2020  
Foundations of Programming: Python  
Assignment 07

## Introduction
This week’s assignment introduced me to two concepts within Python called error handling and pickling. Error handling allow programmers to intercept a script when it encounters an error within the code and control the message output and can allow the script to fully run without exiting out like a script would if there was no except clause to intercept. Pickling is used to convert python objects such as lists and dictionaries into byte streams for space efficiency. Pickling also allows for easier transfer of data from one system to another.

## Error Handling
As mentioned previously, error handling allows programmers to intercept errors in order to provide their own error message or to allow the code to continue despite an error by putting the code in a try/except block. A try/except block has a segment of code in a “try” block which is the code you want to run and the “except” block will handle the error. 

In Figure 1 below, in the “try” block, I’m asking for two pieces of information from the user which are the name and age. The age variable can only accept integers and will error out if anything else is entered. I used the “ValueError” exception because I know that’s the error that will pop up if the wrong value type is entered and cannot be converted. I can print my own error message plus use Python’s error message as well. 
