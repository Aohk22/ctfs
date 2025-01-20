# Basic enumeration

Looks like a site that just serves images.  
But there is a login page, registration page, and forgot password page.  
We are also given the source code.
## Database file

There is a sqlite3 database file with 1 table and no data.  
![Pasted image 20250119144527.png](images/Pasted%20image%2020250119144527.png)  
## Version disclosure

Webapp uses flask **Flask version 3.1.0** (in requirements.txt file).
## Source analysis

`users` table schema:
![Pasted image 20250119144926.png](images/Pasted%20image%2020250119144926.png)  
Code also seems to be safe from SQLI.  
### Register function

When registering, the app inserts the user provided credentials and then create admin credentials from the users input.  
![Pasted image 20250119161332.png](images/Pasted%20image%2020250119161332.png)
### Other

The flag is stored in the FLAG variable in python app:  
![Pasted image 20250119144846.png](images/Pasted%20image%2020250119144846.png)  
It seems we need to find a way to put username that starts with `admin` to get the flag.
![Pasted image 20250119154059.png](images/Pasted%20image%2020250119154059.png)  
So inorder to display the flag, we need to login as admin but password is unknown (see code above in `Register function`).  
The challenge actually shows us the admin username through this line:  
![Pasted image 20250119162327.png](images/Pasted%20image%2020250119162327.png)  
We can see that it is hidden in html source by looking at `home.html`:  
![Pasted image 20250119162428.png](images/Pasted%20image%2020250119162428.png)  

Now we have admin username:  
> `admin^123^9707f2ae4b`

# Exploit

This exploits the faulty reset mecahnism in the webapp.  
First the `/reset_password` endpoint:  
We cannot not specify admin account for password reset.  
![Pasted image 20250119162058.png](images/Pasted%20image%2020250119162058.png)  
So I went with the normal account name, in this case:
> username: 123 password: 123

After that the server gives us the reset token and we can proceed to `/forgot_password` endpoint.  
![400](images/Pasted%20image%2020250119163107.png)  
![400](images/Pasted%20image%2020250119163129.png)
In the reset page we can actually provide the admin username now (it was not intended to reset admin password but to parse admin account name to normal user and then reset the normal user's password).

Luckily for us, even the webapp parses the username correctly, the actual code that is used to update user password mistakenly takes  `request.form['username']` instead of just `username`:  
![Pasted image 20250119161859.png](images/Pasted%20image%2020250119161859.png)  
Therefore we can use user reset token to reset admin password:  
![400](images/Pasted%20image%2020250119164009.png)  
![Pasted image 20250119164028.png](images/Pasted%20image%2020250119164028.png)  

After that we can login using admin username and go to `/image/ben10` to see that flag.  
![400](images/Pasted%20image%2020250119164205.png)

`srdnlen{b3n_l0v3s_br0k3n_4cc355_c0ntr0l_vulns}`