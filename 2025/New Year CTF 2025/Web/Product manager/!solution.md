Website allows creating barcode for an input.
Has input lookup function for a specific barcode.

Sending a POST request to `/create` endpoint gives us the barcode, looking at response HTML we see something ***sus*** (highlighted).
![[Pasted image 20250113140015.png]]
From here we can access all created product, through its barcode.
![[Pasted image 20250113140156.png|600]]
Luckily when I tried testing this first barcode (`1.png`) with the website, it gave me the flag.
Getting the barcode:
![[Pasted image 20250113140600.png]]
Getting content using `/get` endpoint:
![[Pasted image 20250113140844.png]]

`grodno{7eb13bfd35b2f61de9edb6064e40bfa5}`