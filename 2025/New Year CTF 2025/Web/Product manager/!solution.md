Website allows creating barcode for an input.<br>
Has input lookup function for a specific barcode.<br>

Sending a POST request to `/create` endpoint gives us the barcode, looking at response HTML we see something ***sus*** (highlighted).<br>
![Pasted image 20250113140015.png](Pasted%20image%2020250113140015.png)<br>
From here we can access all created product, through its barcode.<br>
![600](Pasted%20image%2020250113140156.png)<br>
Luckily when I tried testing this first barcode (`1.png`) with the website, it gave me the flag.<br>
Getting the barcode:<br>
![Pasted image 20250113140600.png](Pasted%20image%2020250113140600.png)<br>
Getting content using `/get` endpoint:<br>
![Pasted image 20250113140844.png](Pasted%20image%2020250113140844.png)<br>

`grodno{7eb13bfd35b2f61de9edb6064e40bfa5}`