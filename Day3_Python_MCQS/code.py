# Q1: Dictionary is mutable and stores key-value pairs
my_dict = {"name": "Kaladi", "cgpa": 9.0, "mark": 85}
print(my_dict)  # Output: {'name': 'Kaladi', 'cgpa': 9.0, 'mark': 85}

# Q2: Accessing value using key
print(my_dict["name"])  # Output: Kaladi

# Q3: Duplicate key gets overwritten
dup_dict = {"name": "Subhan", "name": "Kaladi"}
print(dup_dict)  # Output: {'name': 'Kaladi'}

# Q4: Accessing nested dictionary value
student = {"name": "Kaladi", "score": {"chem": 98, "phy": 97, "math": 95}}
print(student["score"]["math"])  # Output: 95

# Q5: Dictionary keys()
print(my_dict.keys())  # Output: dict_keys(['name', 'cgpa', 'mark'])

# Q6: .get() method returns None if key doesn't exist
print(my_dict.get("age"))  # Output: None

# Q7: Adding new key-value pair
dict1 = {"a": 1, "b": 2}
dict1["c"] = 3
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Q8: Creating empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Q9: Set stores unique, immutable elements
my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}

# Q10: .add() method in set
nums = {1, 2, 3, 4}
nums.add(5)
print(nums)  # Output: {1, 2, 3, 4, 5}

# Q11: Duplicates not allowed in sets
set2 = {1, 2, 2, 2}
print(set2)  # Output: {1, 2}

# Q12: .remove() raises KeyError if element not found
set2.remove(2)
print(set2)  # Output: {1}
# set2.remove(10)  # Uncommenting this will raise KeyError

# Q13: .clear() empties the set
s = {1, 2, 3}
s.clear()
print(s)  # Output: set()

# Q14: union() method in set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))  # Output: {1, 2, 3, 4}

# Q15: intersection() method in set
print(set1.intersection(set2))  # Output: {2, 3}

# Q16: Dictionary storing meanings
dict2 = {
    "table": "a piece of furniture",
    "cat": "a small animal"
}
print(dict2["table"])  # Output: a piece of furniture

# Q17: Count unique items in list using set
subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "c"]
unique_subjects = set(subjects)
print(len(unique_subjects))  # Output: 6

# Q18: Correct way to create empty set
my_set = set()
print(my_set)  # Output: set()

# Q19: Creating and printing dictionary
myDict = {}
myDict["math"] = 90
myDict["phy"] = 85
myDict["chem"] = 88
print(myDict)  # Output: {'math': 90, 'phy': 85, 'chem': 88}

# Q20: Storing 9 and 9.0 separately in set is NOT possible (both treated same)
my_set = {9, 9.0}
print(my_set)  # Output: {9}

# Q21: .values() returns all values in dictionary
myDict2 = {"a": 1, "b": 2, "c": 3}
print(list(myDict2.values()))  # Output: [1, 2, 3]

# Q22: Accessing non-existent key with [] gives KeyError
# print(myDict2["x"])  # Uncommenting this will raise KeyError

# Q23: .pop() removes and returns an arbitrary element
nums = {1, 2, 3}
nums.pop()
print(len(nums))  # Output: 2

# Q24: intersection() keeps common elements only
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # Output: {2, 3}

# Q25: Access nested dict values
dict3 = {"name": "Kaladi", "score": {"chem": 98}}
print(dict3["score"]["chem"])  # Output: 98
