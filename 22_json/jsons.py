# Python JSON
# * JSON is a syntax for storing and exchanging data.
# * JSON is text, written with JavaScript object notation.

# ? JSON in Python
# * Python has a built-in package called 'json', which can be used to work with JSON data.
# * Import the 'json' module:
import json
# * Parse JSON - Convert from JSON to Python
# * If you have a JSON string, you can parse it by using the 'json.loads()' method.
# ? Convert from JSON to Python:
# * some json
x = '{"name":"imran", "age":23, "profession":"python developer"}'
# * parse x
y = json.loads(x)
print(y["name"])
print(x)


# ? Convert from Python to JSON
# * If you have a Python object, you can convert it into a JSON string by using the 'json.dumps()' method.
# * Convert from Python to JSON:
xx = {
    "name": "Kawsar",
    "age": 22,
    "profession": "Student"
}
z = json.dumps(xx)
print(z)
print(type(z))  # * json str

"""
? You can convert Python objects of the following types, into JSON strings:

1. dict
2. list
3. tuple
4. string
5. int
6. float
7. True
8. False
9. None
"""
# * Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "imran", "age": 23}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

"""
? When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

!Python                   JSON
    dict     >>>>>>>>    Object
    list     >>>>>>>>    Array
    tuple    >>>>>>>>    Array
    str	     >>>>>>>>    String
    int      >>>>>>>>    Number
    float    >>>>>>>>    Number
    True     >>>>>>>>    true
    False    >>>>>>>>    false
    None     >>>>>>>>    null
"""

#? Convert a Python object containing all the legal data types:

details = {
    "name": "imran",
    "age": 23,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(details)
#* Format the Result
#* The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
#* The json.dumps() method has parameters to make it easier to read the result:
#* Use the indent parameter to define the numbers of indents:
my_json = json.dumps(details, indent=4)
print(my_json)

#* You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
#* Use the separators parameter to change the default separator:

my_json2 = json.dumps(details, indent=4, separators=(".", "="))
print(my_json2)

#? Order the Result
#* The json.dumps() method has parameters to order the keys in the result:
#* Use the 'sort_keys' parameter to specify if the result should be sorted or not:
my_json3 = json.dumps(details, indent=4, sort_keys= True)
print(my_json3)

