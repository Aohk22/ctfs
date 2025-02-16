# Solution
There was not much information on the website so I just went for the files.

![image](https://github.com/user-attachments/assets/5afdde1f-2141-4cf4-9370-d7bd02438e7d)

Server only gives flag if: num.length == 3 and every char in num is digit.
I messed around and saw that if I send an array of 3 random numbers, num.length is still == 3.
I tested parseInt() on array in node:

![image](https://github.com/user-attachments/assets/1e51c84d-d96c-4d84-bf3b-65e5d5bcebc0)

It returns the first element in array as int.
So sending num as array of int strings, where the first string is "65536" should give the result.

![image](https://github.com/user-attachments/assets/649f76e4-8dc5-473a-a661-a0eba8319207)
