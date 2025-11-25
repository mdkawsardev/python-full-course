# Join Sets
#? There are several ways to join two or more sets in Python.

"""
The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

"""

#? union()
set1 = {"apple", "banana", "watermelon"}
set2 = {"fruits", "water", "rice"}
set3 = set1.union(set2)
print(set3)

#? You can use the | operator instead of the union() method, and you will get the same result.

set4 = set1 | set2
print(set4)

#? Joining multiple sets using union()
set5 = {"a", "b", "c", "d"}
set6 = {1, 2, 3, 4, 5, 6}
set7 = {True, False}
set8 = set1.union(set5, set6, set7)
print(set8)

#? Joining multiple ses using | operator
set9 = set1 | set5 | set6 | set7
print(set9)
#! Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
#? Join a Set and a Tuple
my_set = {"a", "b", "c"}
my_tuple = (1, 2, 3)
combine = my_set.union(my_tuple)
print(combine)

#? Update
#* The update() method inserts all items from one set into another.
#* The update() changes the original set, and does not return a new set.
set10 = {"Imran", "Kawsar", "Ahmed"}
set11 = {1, 2, 3}
set10.update(set11)
print(set10)

#! Note: Both union() and update() will exclude any duplicate items.

#? Intersection
#* Keep ONLY the duplicates
#* The intersection() method will return a new set, that only contains the items that are present in both sets.
new_set1 = {"apple", "banana", "watermelon", "mango"}
new_set2 = {"apple", "melon", "mango", "orange"}
duplicates = new_set1.intersection(new_set2)
print(duplicates)
#? You can use the & operator instead of the intersection() method, and you will get the same result.
duplicates_again = new_set1 & new_set2
print(duplicates_again)
#! Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

#? intersection_update()
#* The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
new_set1.intersection_update(new_set2)
print(new_set1)

f_name = {"md", 1, "dr", 0}
l_name = {"karim", True, "rahim", False}
full_name = f_name.intersection(l_name)
print(full_name)

#? Difference
#* The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
#* Keep all items from set1 that are not in set2:
age = {23, 22, 40, 50}
child = {40, 50, 12}
get = age.difference(child)
print(get) #* Returns 22, 23
#* You can use the - operator instead of the difference() method, and you will get the same result.
getting = age - child
print(getting)
#! Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

#? The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
#* Use the difference_update() method to keep the items that are not present in both sets:
age.difference_update(child)
print(age)

#? Symmetric Differences
#* The symmetric_difference() method will keep only the elements that are NOT present in both sets.
fruits1 = {"mango", "orange", "pear", "grape"}
fruits2 = {"grape", "litchi", "pulm"}
diff = fruits1.symmetric_difference(fruits2)
print(diff)

#? You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
#* Use ^ to join two sets:
diff_again = fruits1 ^ fruits2
print(diff_again)

#! Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

#? The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
fruits1.symmetric_difference_update(fruits2)
print(fruits1)

