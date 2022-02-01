# Task 5

They gave us cat.jpg

Then just used command **exiftool** to get the information of that file.

```
exiftool - Read and write meta information in files

The lisence things was base64 type.
```

```
exiftool cat.jpg | grep License 

License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```

```
We just used sed command afterwards.

exiftool cat.jpg | grep License | sed -e 's/.*: //' | base64 -d  
```

**CTF**
```
picoCTF{the_m3tadata_1s_modified}
```

