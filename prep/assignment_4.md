# Assignment 4


# Tutorials to review

Make sure you have reviewed the following topics before starting to work on this assignment. 

Files: [https://www.py4e.com/lessons/files](https://www.py4e.com/lessons/files)

Lists: [https://www.py4e.com/lessons/lists](https://www.py4e.com/lessons/lists)


## Input file

The data used for this assignment can be downloaded from [cinderella.txt](cinderella.txt). Once you have downloaded the dataset, copy it to the same folder where you write your Python script.

If you are not sure in which directory Jupyter notebook is working from, you can run the following:

```python
# import the package os (operating system functions)
import os
# get the current working directory
cwd = os.getcwd()
# print it
print('Currently working in folder', cwd)
```

## Assignment

Look at the question/answer on Stackoverflow on how to read a file into a list [https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list](https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list):

Run the following code:

```python
# this assumes that the file 'cinderella.txt' is in the same folder as your ipynb script 
fname = "cinderella.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# print the first few lines
for line in content[0:5]:
	print(line)
```

The above code will read the cinderella poem into a list of strings, and will print the first 5 lines.

## Required

Adapt the code to count the following:

- the number of lines in the poem
- the number of words in the poem (use the split function to turn each line into a list of words, use Google 'python string split') 
- the number of lines that include 'Prince' 
- the number of lines that include 'cried'

Additionally, Caesar has received your reply for assignment 2 and let's you know he is interested in cultural milestones of the last 2,000 years. Write the full poem to disk (encrypted). (Google 'python write to file' for help on writing to disk.)

Note: you need to exclude the last line as it is not part of the poem.
