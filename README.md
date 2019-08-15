# Service Scanner

**Get running services on linux**

List all running services on the linux machine. 


**You will get**

- Running services'name
- Designated port
- Ports protocol
- services type

**same as netstat tool**

| Service       |  Port      | Protocol | TYPE     |
| ------------- |:----------:| --------:|---------:|
| service 1     | 8080       | UDP      |webcahe   |
| postgres      | 5332       | UDP      |Postgres  |
| ngnix         | 80         | SCTP     |HTTP      |

**as scanner** 
You can use it on your remote server to check for vulnerabilities

### TODO:

- Print result with nice output column on the terminal

## Requirements: 
- asyncio
- psutil
- [Linux](https://www.linux.org/)

## Installation:

#### check python version.

Requires *python* version *3.6+*

pip install -r requirements.txt

```python

pip install psutil

```


### Usage:

```python

from portscanner import TCPScanner

# If it is localhost, return running service,
# if it is remote, return open ports.
host = 'localhost'

scanner = TCPScanner(host=host, remote=False)
scanner.scan

```


#### Expected Error:

- Async loop error.

Such a case, open a new async loop *asyncio.new_event_loop()* and run the script.
