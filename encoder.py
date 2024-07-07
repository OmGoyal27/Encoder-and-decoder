from extracter import fetch_hash

list_of_value_to_encode = list(input("Enter your value to encode: "))
encoded_list = []
alphabets = fetch_hash()
for alphabet in list_of_value_to_encode:
    encoded_list.append(alphabets[alphabet])
encoded_value = ''.join(encoded_list)

print(encoded_value)