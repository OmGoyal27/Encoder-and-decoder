import json
import random

# Load list_of_obs.json
with open('list_of_obs.json', 'r') as file:
    list_of_obs = json.load(file)

# Load existing hashes.json
with open('hashes.json', 'r') as file:
    hashes = json.load(file)

# Get all characters that need to be encoded
all_characters = set(list_of_obs)

# Get currently used characters in the hash map
used_characters = set(hashes.values())

# Find missing mappings
missing_mappings = all_characters - set(hashes.keys())
available_characters = all_characters - used_characters

# Ensure there are enough characters to create unique mappings
if len(missing_mappings) > len(available_characters):
    raise ValueError("Not enough unique characters available to complete the hash map")

# Create new mappings for the missing characters
new_mappings = {}
for char in missing_mappings:
    new_char = random.choice(list(available_characters))
    new_mappings[char] = new_char
    available_characters.remove(new_char)

# Update the existing hashes with the new mappings
hashes.update(new_mappings)

# Save the complete hashes.json
with open('hashes.json', 'w') as file:
    json.dump(hashes, file, indent=4)

print("hashes.json has been completed successfully.")
