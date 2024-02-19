#  Part5----- Lists In Python

"""Lists ---- A built in data type stores set of values
It can store elements of different types like int,float,string,etc.."""

# Declaration

marks = [4,6,"Rockstar",2,3,5.86]
print(type(marks))
print(len(marks))

# Slicing In Lists

print(marks[1:4])

# Properties of lists

# 1) Append----It will add element at end 

# marks.append(90)
# print(marks)

# 2) Sorting----Sorts in ascending Order

# list = [5,7,0,2,4]
# list.sort()
# print(list)

# 3) Sorting----Sorts in discending Order

# list = [5,7,0,2,4]
# list.sort(reverse=True)
# print(list)

#  4)  Reverse ---- reverse the Lists

# marks.reverse()
# print(marks)


# 5)  Insert--- To insert elements at particular index

marks.insert(1,5)  # list.insert(index,element)


# 6)  Remove--- To remove 1st occurence of element

marks.remove(1)  # list.insert(element)

# 7)  POP--- To remove element at index

marks.pop(1)  # list.pop(index)







