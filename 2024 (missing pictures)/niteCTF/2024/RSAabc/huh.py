from Crypto.Util.number import *

lines = []
e = 65537
language = {
    'A': 'Α', 'a': 'α',
    'B': 'Β', 'b': 'β',
    'C': 'Σ', 'c': 'σ',
    'D': 'Δ', 'd': 'δ',
    'E': 'Ε', 'e': 'ε',
    'F': 'Φ', 'f': 'φ',
    'G': 'Γ', 'g': 'γ',
    'H': 'Η', 'h': 'η',
    'I': 'Ι', 'i': 'ι',
    'J': 'Ξ', 'j': 'ξ',
    'K': 'Κ', 'k': 'κ',
    'L': 'Λ', 'l': 'λ',
    'M': 'Μ', 'm': 'μ',
    'N': 'Ν', 'n': 'ν',
    'O': 'Ο', 'o': 'ο',
    'P': 'Π', 'p': 'π',
    'Q': 'Θ', 'q': 'θ',
    'R': 'Ρ', 'r': 'ρ',
    'S': 'Σ', 's': 'ς',  
    'T': 'Τ', 't': 'τ',
    'U': 'Υ', 'u': 'υ',
    'V': 'Ω', 'v': 'ω',
    'W': 'Ψ', 'w': 'ψ',
    'X': 'Χ', 'x': 'χ',
    'Y': 'Υ', 'y': 'υ',
    'Z': 'Ζ', 'z': 'ζ'
}
with open('out.txt', 'rb') as file:
	for line in file:
		lines.append(line)
N = [ int(n.strip()) for n in lines[4].decode('utf-8').strip().split(',')[:-1] ]
cts = [ int(n.strip()) for n in lines[2].decode('utf-8').strip().split(',')[:-1] ]
ascii_chars = ''.join([ chr(i) for i in range(32, 127) ])
print(ascii_chars)
		
def reverse_alphabet(char):
	if char == 'e':
		return '_'
	elif char.isupper():  
		return chr(155 - ord(char))  
	elif char.islower():  
		return chr(219 - ord(char)) 
	
# imported functions
def rsa_encrypt(message, public_key):
	# typical rsa encryption
    n, e = public_key
    message_as_int = string_to_int(message)
    ciphertext = pow(message_as_int, e, n)
    return ciphertext
	
def googly(number, position):
    mask = 1 << position
    return number ^ mask
	
def string_to_int(message):
    return int.from_bytes(message.encode('utf-8'), byteorder='big')	

# solving part
flag = lines[0].decode('utf-8').strip() # decode bytes

flag = ''.join([ reverse_alphabet(c) if ord(c) in range(65, ord('z') + 1) else c for c in flag ]) # reverse alphabet

flag = flag[:flag.find('_')] + '{' + flag[flag.find('_')+1:] # manual format
flag = flag[:flag.rfind('_')] + '}' + flag[flag.rfind('_')+1:]

print(flag)
for i in range(len(flag)):
	char = flag[i]
	if not ord(char) in range(65, 123) and not char in '{}_': 	# avoid already solved chars
		for temp_char in ascii_chars: 							# iterate over every ascii char if encrypytion matches "output.txt", take (we know N[i] already)
			e = 65537
			pubkey = (N[i], e)	
			message = temp_char
			ciphertext = rsa_encrypt(message, pubkey)
			if str(cts[i])[:20] == str(ciphertext)[:20]:		# 20 chars only cause some bits flip
				flag = flag[:i] + temp_char + flag[i+1:]		# flag[i] - e[i] - N[i] cause the thats how the cipher works
			
print(flag)				