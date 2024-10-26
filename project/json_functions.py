import json

# Function to save (write) dictionary data to JSON
def save_to_json(data, filename='data.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Function to load (read) data from JSON
def load_from_json(filename='data.json'):
    try:
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"{filename} not found.")
        return None
    
# Function to save dictionary data to JSON
def save_to_json(data, filename='data.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)