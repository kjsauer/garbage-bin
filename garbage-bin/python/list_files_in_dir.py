# List files in current working directory cwd.
import os
cwd = os.getcwd()
os.chdir(cwd)
files = os.listdir(os.curdir)
print(files)