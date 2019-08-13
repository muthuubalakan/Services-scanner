# Service Scanner

**Running services for linux**

List all running services on the linux machine. 


You will get,
------------

- Running services name
- Designated port
- Ports protocol
- services type


| Service       |  Port      | Protocol | TYPE     |
| ------------- |:----------:| --------:|---------:|
| service 1     | 8080       | UDP      |webcahe   |
| postgres      | 5332       | UDP      |Postgres  |
| ngnix         | 80         | SCTP     |HTTP      |


TODO:
----
- Print with nice output column on the terminal

## Requirements: 
- asyncio
- psutil

__FOR LINUX__
- [Linux](https://www.linux.org/)

## Installation:

check python version.
--------------------
Requires *python* version *3.6+*

pip install -r requirements.txt

```python

pip install psutil

```

Compile
-------
Or else, you can compile the code and  execute directly from terminal.


### Usage:

```python

from portscanner import TCPScanner


# simple call
scanner = TCPScanner()
scanner.scan
   ```

Expected Error:
---------------
- Async loop error.
Such a case, open new async loop *asyncio.new_event_loop()* and run the script.