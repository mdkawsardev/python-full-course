# Access Set Items
#? You cannot access items in a set by referring to an index or a key.
#* But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
set1 = {"January", "February", "March", "April"}
for x in set1:
    if "February" != x:
        print(x)
    else:
        print(x.upper())

#* Check if "Jun" is not present in the set:
print("Jun" not in set1)
#* Check if "April" is present in the set:
print("April" in set1)

#! Once a set is created, you cannot change its items, but you can add new items.

