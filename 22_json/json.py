# Python JSON
#* JSON is a syntax for storing and exchanging data.
#* JSON is text, written with JavaScript object notation.

#? JSON in Python
#* Python has a built-in package called 'json', which can be used to work with JSON data.
#* Import the 'json' module:
import json
#* Parse JSON - Convert from JSON to Python
#* If you have a JSON string, you can parse it by using the 'json.loads()' method.
#* Convert from JSON to Python:
#* some json
x = '{"name":"imran", "age":23, "profession":"python developer"}'
#* parse x
y = json.loads(x)
print(y["name"])



