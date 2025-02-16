import base64
import hashlib

from cryptography.fernet import Fernet, InvalidToken


# imported
def generate_key(password):
    # Hash the password to generate a consistent key
    password_bytes = password.encode('utf-8')
    key = hashlib.sha256(password_bytes).digest()  # SHA256 to get a 32-byte key
    return base64.urlsafe_b64encode(key)  # Fernet requires the key to be in base64 format
	

def crack_fernet(filepath, countries: list) -> bytes:
	result = b''
	with open(filepath, 'rb') as file:
		ciphertext = file.read()
	#print(ciphertext)
	#print(countries)
		
	for country in countries:
		for year in range(1, 3000):
			key_clear = str(year) + country
			key = generate_key(key_clear)
			cipher = Fernet(key)
			try:
				result = cipher.decrypt(ciphertext)
				print(f'{year=}')
				print(f'{country=}')
				print(f'The cleartext is {result.decode('utf-8')=}')
			except InvalidToken:
				continue
	
	
if __name__ == '__main__':
	with open('countries2.txt', 'r') as file: # countries.txt didn't work for friend 1
		# .replace('&', 'and')
		# .replace(' ','')
		# .replace(' ','_')
		countries = [line.strip().lower() for line in file]
		
	print(len(countries))
	crack_fernet('encrypted_friend3.txt', countries) # change file name here or just add 2 more lines