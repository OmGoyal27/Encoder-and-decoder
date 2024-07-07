import json

# Load the hash mapping from the provided JSON file
with open('hashes.json', 'r') as file:
    hash_map = json.load(file)

# Reverse the hash map for decoding
reverse_hash_map = {v: k for k, v in hash_map.items()}

def encode(data):
    """Encode the data using the provided hash mapping."""
    encoded_data = ''.join(hash_map.get(char, char) for char in data)
    return encoded_data

def decode(data):
    """Decode the data using the reverse hash mapping."""
    decoded_data = ''.join(reverse_hash_map.get(char, char) for char in data)
    return decoded_data

# Example usage
if __name__ == "__main__":
    # Sample data to encode and decode
    sample_data = "hello world"
    encoded = encode(sample_data)
    decoded = decode(encoded)

    print(f"Original: {sample_data}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
