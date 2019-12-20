# Assignment 5


# Tutorials to review

Make sure you have reviewed the following topics before starting to work on this assignment.

Dictionaries: [https://www.py4e.com/lessons/dictionary](https://www.py4e.com/lessons/dictionary)

# Description

You are writing an application that requires several inputs in order to run. Instead of using the `input` statement, you decide that the users can specify these inputs in a settings file.

You are envisioning that such a file (say `settings.txt`) will look like this:

```
# Your name
name=Joost
# Your favorite animal
animal=dog
# Encryption method
encrypt=Caesar
```

Write a program that reads `settings.txt` and creates a dictionary with key-value pairs, such that both the keys and the values are read from the file. In the above example, the keys would be 'name', 'animal' and 'encrypt', with corresponding values 'Joost', 'dog' and 'Caesar.'

Lines that start with a hash (`#`) need to be ignored. 