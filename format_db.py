import json
import uuid

# Read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Add UUID to each item
for item in data:
    uuid_value = str(uuid.uuid4())
    # Generate UUID and append to the first field
    # Create a new dictionary with the desired order of fields
    new_item = {'id': uuid_value,'author': f"{item['author']}"}
    # Update the item with the new fields
    new_item.update(item)
    item.clear()
    item.update(new_item)

# Save the modified data back to the original file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

db = []
with open('library.json', 'w') as file:
    json.dump(db, file, indent=2)

print("Add uuid to each entry...")