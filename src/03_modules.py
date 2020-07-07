"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys, platform, os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for i in dir(sys.argv):
    print(i)

# Print out the OS platform you're using:
print('\nPlatform:', platform.system())

# Print out the version of Python you're using:
print('\nPython Version:', sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('\nProcess ID:', os.getpid())

# Print the current working directory (cwd):
print('\nCurrent Working Directory:\n', os.getcwd())

# Print out your machine's login name
print('\nMachine Name:', os.environ['COMPUTERNAME'], '\n')
