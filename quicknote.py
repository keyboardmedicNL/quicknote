# import libraries needed in script
import sys

# define these variables before use
notefile = "quicknote.md" # full path of note file

# main script
a = str(sys.argv[1]) # pulls first argument
with open(notefile, "a") as myfile: # opens file in append mode
    myfile.write("\n") # writes blank line
    myfile.write(a + "\n") # writes argument to file
print("noting down: " + a) # log message