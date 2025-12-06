# Python JSON
#* JSON is a syntax for storing and exchanging data.
#* JSON is text, written with JavaScript object notation.

#? JSON in Python
#* Python has a built-in package called 'json', which can be used to work with JSON data.
#* Import the 'json' module:
import json
#* Parse JSON - Convert from JSON to Python
#* If you have a JSON string, you can parse it by using the 'json.loads()' method.
#? Convert from JSON to Python:
#* some json
x = '{"name":"imran", "age":23, "profession":"python developer"}'
#* parse x
y = json.loads(x)
print(y["name"])
print(x)


#? Convert from Python to JSON
#* If you have a Python object, you can convert it into a JSON string by using the 'json.dumps()' method.
#* Convert from Python to JSON:
xx = {
    "name": "Kawsar",
    "age": 22,
    "profession": "Student"
}
z = json.dumps(xx)
print(z)
print(type(z)) #* json str

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
#* Convert Python objects into JSON strings, and print the values:
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