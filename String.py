#  Part3---- String Functions

# String ----- String is datatype that stores a escape sequence characters...

"""
To add new line and space
\n = For Nextline
\t = For Tabspace"""

print("Python is programming language \n It is very simple language")


# Properties 

# 1) Concatenation

string1 = "Hello " + "World"    
print(string1)

# 2) Length of string 

string2 = "Wresteler"
print(len(string2))
print(string2[4])     # To access single character from string

# 3) Slicing ----- Accessing parts of string

str = "Roman reigns"   #  Always index starting from '0'
print(str[1:4])        # '1' is the starting index & ''4 is the end index
#  Like str[start index : end index]

print(str[:6])    # If you not give start index it consider from '0'
print(str[1:])    # If you not give end index it consider whole sting


#  String some In-Built Functions

str1 = "this is Spartaa"

print(str1.capitalize())   # capitalize means it capitalize string 1st letter
print(str1.replace("aa","oo"))  # It replaces characters str("old","new") also for entire word
print(str1.find("s"))    # Give count of searched word or character
print(str1.count("s"))   # Count 1st occurence of string so it will give index num







