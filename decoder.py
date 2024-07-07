from extracter import fetch_hash

def reverse_hash_map(hash_map):
    return {v: k for k, v in hash_map.items()}

encoded_value = input("Enter the value to decode: ")
encoded_list = list(encoded_value)
hash_map = fetch_hash()
reversed_hash_map = reverse_hash_map(hash_map)

decoded_list = [reversed_hash_map[char] for char in encoded_list]
decoded_value = ''.join(decoded_list)

print(decoded_value)
