# import libraries needed in script
import sys

# define these variables before use
notefile = "quicknote.md"

# main script
a = str(sys.argv[1])
with open(notefile, "a") as myfile:
    myfile.write("\n")
    myfile.write(a + "\n")
print("noting down: " + a)