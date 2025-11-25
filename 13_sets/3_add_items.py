# Add Set Items
#? To add one item to a set use the add() method.
#* Add an item to a set, using the add() method:

set1 = {'January', 'February', 'March', 'April'}
print(set1)
set1.add('May')
print(set1)

#? To add items from another set into the current set, use the update() method.
#* Add elements from tropical into thisset:
set2 = {'year', 'month', 'week', 'day'}
set3 = {'hour', 'minute', 'second', 'milisecond'}
set2.update(set3)
print(set2)
#* The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

set4 = {"apple", "banana", "cherry"}
list1 = ["fruits", "water", "rice"]
set4.update(list1)
print(set4)