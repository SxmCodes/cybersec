# Task 14 - Buy and sell 

**Question**

1. We are given this ```nc mercury.picoctf.net 24851```


**Answer**

1. We ran it and make our coin ```1040``` by writing ```-100```

2. We got this

_Fruit flag_
```[112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 53 51 50 98 99 100 57 56 125]```

3. Wrote this python program. 

```python
s = '112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 53 51 50 98 99 100 57 56 125'

# It gets converted into a list.
l = s.split(' ')

str = ""

for i in l:
	str = str + chr(int(i))

print(str)

# Output = picoCTF{b4d_brogrammer_532bcd98}
```

4. Flag = ```picoCTF{b4d_brogrammer_532bcd98}```