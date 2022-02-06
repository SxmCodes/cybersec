# Task 12 - Wireshark 🦈

**Question**
1. We are given ```shark1.pcapng``` file.

**Answer**
1. Opened with wireshark ```wireshark shark1.pcapng```

2. Searched for ```200 OK``` code.

3. Found ```HTTP 1.1 200``` and it was ```GET``` request.

4. ```Followed``` it with ```HTTP``` and got this string.

```cvpbPGS{c33xno00_1_f33_h_qrnqorrs}```

5. This is ROT13 format so converted it and got the ```flag```

```picoCTF{p33kab00_1_s33_u_deadbeef}```
