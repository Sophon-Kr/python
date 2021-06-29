try:
    fh = open('news_file.txt','a+')
    fh.write("""Linting highlights syntactical and stylistic problems
in your Python source code, which oftentimes helps you
identify and correct subtle programming errors or 
unconventional coding practices that can lead to errors.
For example, linting detects use of an uninitialized or
undefined variable, calls to undefined functions, missing
parentheses, and even more subtle issues such as attempting
to redefine built-in types or functions. Linting is thus distinct
from Formatting because linting analyzes how the code runs and detects
errors whereas formatting only restructures how code appears.""")
    fh = open('news_file.txt','r+')
    p=fh.read()
    print(p)
except IOError:
    print("can't read file or data")
else:
    print('working successful!!')
    fh.close()