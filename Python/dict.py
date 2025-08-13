# Create a dictionary
my_dict = {
    "name": "Sandhyarani",
    "age": 21,
    "city": "New York"
}

# Accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# Adding a new key-value pair
my_dict["job"] = "Software Engineer"
print("Updated dictionary:", my_dict)


# Check if a key exists
if "city" in my_dict:
    print("City is in the dictionary")

# Remove a key-value pair
my_dict.pop("age")
print("After removing age:", my_dict)
