import sys
from igni import call_gitignore, completion

if len(sys.argv) < 2:
    print("No argument supplied")

if sys.argv[1] == "completion":
    print(completion())
else:
    print(call_gitignore(*sys.argv[1:]))
