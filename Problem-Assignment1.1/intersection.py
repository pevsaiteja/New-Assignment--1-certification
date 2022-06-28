# s = set("The number of students who have subscribed to the English Newspaper")
# print (s.intersection("The number of students who have subscribed to the English Newspaper"))
# set = ()
# test_list = []

set1 = {9}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set3 = {9}
set4 = {10, 1, 2, 3, 11, 21, 55, 6, 8}
print("set2 intersection set4 :",set2.intersection(set4))
print("set1 intersection set2 intersection set4 intersection set4 :",set1.intersection(set2, set3, set4))