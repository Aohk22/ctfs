# Memory Forensics

*First time doing forensics, forget my misconceptions*

## #1 Nhà bảo vệ môi trường

Used volatility 2.6 to solve.  
`imageinfo` to get dump profile:  
![Pasted image 20250215151130.png](Pasted%20image%2020250215151130.png)  
First one works.  

`pstree` returned this:  
![Pasted image 20250215151309.png](Pasted%20image%2020250215151309.png)  

`procdump` to get executable:  
![Pasted image 20250215151820.png](Pasted%20image%2020250215151820.png)  
Running executable (yes on host machine :D):  
![Pasted image 20250215151924.png](Pasted%20image%2020250215151924.png)  

`envars` to check environment variables of Flag.exe:  
![Pasted image 20250215152125.png](Pasted%20image%2020250215152125.png)  

`FIA{V0lat1l1ty_1s_3ssential_f0r_m3m_4nalyse}`

## #2.1/2/3 Vạn sự khởi đầu nan

Challenge desc. notes:  
Làm ơn hãy lấy tất cả các tệp ra khỏi hệ thống.  
Theo những gì mình nhớ thì có một cửa sổ màu đen được bật lên và một chương trình được thực thi.  
Khi xảy ra sự cố, tôi nhớ step bro mình đang vẽ một cái gì đấy.  

`imageinfo`:  
![Pasted image 20250215193939.png](Pasted%20image%2020250215193939.png)

`pstree`:  
![Pasted image 20250215194208.png](Pasted%20image%2020250215194208.png)

First inspection of `memdump` of mspaint.exe didn't return anything (or maybe I just didn't see). Inspection was done by opening .dump file as raw image data in Gimp:  
(I found this method credit to https://w00tsec.blogspot.com/2015/02/extracting-raw-pictures-from-memory.html)  
![Pasted image 20250215185836.png](Pasted%20image%2020250215185836.png)    
I guess I'll lay off that for now and look at other things.

`cmdline` returns interesting result:  rar file  
![Pasted image 20250215192606.png](Pasted%20image%2020250215192606.png)  

`filescan` and findstr to get the rar file offsets:
![Pasted image 20250215192803.png](Pasted%20image%2020250215192803.png)  
After extracting all 3, it seems they're the same.

#### The rar file

> Password is NTLM hash(in uppercase) of Alissa's account passwd

`hashdump` for hash:  
```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SmartNet:1001:aad3b435b51404eeaad3b435b51404ee:4943abb39473a6f32c11301f4987e7e0:::
HomeGroupUser$:1002:aad3b435b51404eeaad3b435b51404ee:f0fc3d257814e08fea06e63c5762ebd5:::
Alissa Simpson:1003:aad3b435b51404eeaad3b435b51404ee:f4ff64c8baac57d22f22edc681055ba6:::
```
Enter the NTLM hash and we get flag  
![500](Pasted%20image%2020250215192402.png)  

`flag{w3ll_3rd_stag_was_easy}`

Part 1, 2 not solved yet.  

##### Continuing with part 1, 2 after a day:  

I was trying out some commands, `consoles` gave me this peculiar base64 string:  
![Pasted image 20250216210104.png](Pasted%20image%2020250216210104.png)  

Putting in cyberchef returned the flag.

`flag{th1s_1s_th3_1st_st4g3!!}`

Now we just need to find the second stage flag. The only clue left is that mspaint process.  
After a while found something interesting:  
![600](Pasted%20image%2020250216213108.png)  
![600](Pasted%20image%2020250216214002.png)  
0_0:  ![Pasted image 20250216214300.png](Pasted%20image%2020250216214300.png)
After messing with it for a while I got the flag:  
![Pasted image 20250216214735.png](Pasted%20image%2020250216214735.png)  
`flag{g00d_boy_good_girl}` I coudn't submit this flag for whatever reason

## 3.1 Bầu Trời Mới - Da LAB ft. Minh Tốc

Chall. desc. notes:  
khách hàng tên H của công ty đầu chữ T đuôi chữ D.  
(environmentalist).  
các ứng dụng ông ấy sử dụng là trình duyệt, trình quản lý mật khẩu.  

`iamgeinfo`:  
```
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (D:\Ctfs\shared\Lab2.raw)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf800027f20a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff800027f3d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2019-12-14 10:38:46 UTC+0000
     Image local date and time : 2019-12-14 16:08:46 +0530
```

### Keepass

`cmdline` reveals notepad used to edit `Hidden.kdbx`, it needs password.  
Discovered **[CVE-2023-32784](https://nvd.nist.gov/vuln/detail/CVE-2023-32784)** This might be helpful because:  
```
2019-12-14 10:37:56 UTC+0000
KeePass.exe pid:   3008
Command line : "C:\Program Files (x86)\KeePass Password Safe 2\KeePass.exe" "C:\Users\SmartNet\Secrets\Hidden.kdbx"
**************************************************************
2019-12-14 10:38:20 UTC+0000
notepad.exe pid:   3260
Command line : "C:\Windows\system32\NOTEPAD.EXE" C:\Users\SmartNet\Secrets\Hidden.kdbx
```  
There was a notepad process that accessed `Hidden.kdbx`, might be to add extra data so that I can't run the scripts. The challenge might be reverting these changes?  

Ran all the scripts I found on github but still no luck.  
All scripts names: BruteForce-to-KeePass, keepass-dump-masterkey, keepass-password-dumper, PoshKPBrute.  

### Browser

```
. 0xfffffa8002109b30:chrome.exe                      2296   2664     27    658 2019-12-14 10:36:45 UTC+0000
.. 0xfffffa8001cc7a90:chrome.exe                     2304   2296      8     71 2019-12-14 10:36:45 UTC+0000
.. 0xfffffa8000ea2b30:chrome.exe                     2964   2296     13    295 2019-12-14 10:36:47 UTC+0000
.. 0xfffffa8000fae6a0:chrome.exe                     2572   2296      8    177 2019-12-14 10:36:56 UTC+0000
.. 0xfffffa800230eb30:chrome.exe                     1632   2296     14    219 2019-12-14 10:37:12 UTC+0000
.. 0xfffffa8000eea7a0:chrome.exe                     2476   2296      2     55 2019-12-14 10:36:46 UTC+0000

```  
Master PID: 2296  
Using the Yara scan method I found here: https://www.eyehatemalwares.com/digital-forensics/blog-df/browser-history/  
It seems the guy accessed https://home.unicode.org/,  
fonts is something about koi8-u-html? More stuff:  
`https://www.google.com/search?q=bi0s&rlz=1C1CHBD_enIN879&oq=bi0s.in&aqs=chrome.6.69i58j69i57j0l5j69i60&sourceid=chrome&ie=UTF-8.8`  
Theres more but I don't think those will help  

### Mental reset

I will do all the basics again to see if I missed anything.  
Ok so doing `envars` on notepad process gave this string that looked off:  
![Pasted image 20250216222626.png](Pasted%20image%2020250216222626.png)  
I tested it for base64 encoding and this is what returned:  
![Pasted image 20250216222732.png](Pasted%20image%2020250216222732.png)  

`flag{w3lc0m3_T0_$T4g3_!_Of_L4B_2}`
