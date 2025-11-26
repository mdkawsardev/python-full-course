# Nested Dictionaries
#? A dictionary can contain dictionaries, this is called nested dictionaries.
#* Create a dictionary that contain three dictionaries:

our_family = {
    "Parents": {
        "Mother": "Mst Asiya Begum",
        "Father": "Md Kabir Hossain"
    },
    "Sister1": {
        "Name": "Mst Akhi Akhter",
        "Age": 28
    },
    "Sister2": {
        "Name": "Mst Ayrin Akhter",
        "Age": 26
    },
    "Sister3": {
        "Name": "Mst Shohagi Akhter",
        "Age": 20
    },
    "Myself": {
        "Name": "Md Kawsar",
        "Age": 23
    }
}
#* This is a manual printing one by one
print(our_family["Parents"]["Mother"])
print(our_family["Parents"]["Father"])
print(our_family["Sister1"]["Name"])
print(our_family["Sister1"]["Age"])
print(our_family["Sister2"]["Name"])
print(our_family["Sister2"]["Age"])
print(our_family["Sister3"]["Name"])
print(our_family["Sister3"]["Age"])
print(our_family["Myself"]["Name"])
print(our_family["Myself"]["Age"])

print("")

#* Same operation using for loop
for a, obj in our_family.items():
    for b in obj:
        print(obj[b])

#? Or, if you want to add three dictionaries into a new dictionary:
#* Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

dict1 = {
    "Name": "Kawsar",
    "Age": 23
}
dict2 = {
    "Name": "Imran",
    "Age": 24
}
dict3 = {
    "Name": "Emon",
    "Age": 25
}

students = {
    "Student1": dict1,
    "Student2": dict2,
    "Student3": dict3
}

for x, obj in students.items():
    print(x)
    for y in obj:
        print(f"{y} = {obj[y]}")