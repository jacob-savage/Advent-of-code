'''
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

 - If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
 - If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

'''



import hashlib

def md5_hash(string):
    # Encode the string as bytes before hashing
    string_bytes = string.encode('utf-8')
    ``
    # Create an MD5 hash object and hash the string bytes`j`
    hash_object = hashlib.md5(string_bytes)
    hash_bytes = hash_object.digest()
    
    # Convert the hash bytes to a hexadecimal string
    hash_hex = hash_bytes.hex()
    
    return hash_hex


key = 'ckczppom'

ans = None
count = 0
while ans is None:
    hash = md5_hash(key + str(count))
    if hash[:6] == '000000':
        ans = count
    count += 1

print(ans)````