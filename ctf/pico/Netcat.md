# NetCat 😼

1. What is Netcat ❓ 

```
 It allows you to send/receive TCP/UDP packets 😎
```

2. Example

```
# Sending ‘hello world!’ to localhost on port 12345.
$ echo 'hello world' | nc localhost 12345
```

3. Listening to incoming packages.

```
$ nc -l <PORT>
nc -l 12345 # Tell netcat to listen to port 12345 for TCP packets
```

**Sender**:
nc localhost 12345 **<** example-netcat.txt

**Receiver**:
nc -l 12345 **>** example-netcat2.txt

> You can also choose to see packets being transferred by netcat in real time by firing up programs like WireShark or tcpdump.

## Options

```
For sending command with IP = -n

then we have to assign the port like 80, 443 etc.

if we want more verbo -v is used for more information.
```
