#WAP to check if a list contains a Palindrom of elements (hint:use copy() method)
#[1,2,3,2,1] Apna Collage[1,"abc","abc",1]

# list = [1,2,3,2,1]

# #make a copy of original list
# copy = list.copy()

# #reverse the copied list
# copy.reverse()

# #compaire with original list
# if list == copy:
#     print("The list is palindrom!" )
# else:
#     print("The list is not a palindrom.")    




lists = [1,"abc","abc",1]

copy= lists.copy()
copy.reverse()

if lists == copy:
    print("List is palindrom:")

else:
    print("List os not palindrom")    