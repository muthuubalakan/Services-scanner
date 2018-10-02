# Porchecker

**vulnerability check for Linux server**

Consists of Asynchronous scanner and list of configured ports of running linux machine.

## Requirements: 
# Python3 - asyncio

Platform: Linux

Usage:

```python

from portscanner import Scanner
host = '0.0.0.0'   # Be it localhost
ports = 65839      # 0 - n

def main():
  """Run scan"""
   return Scanner(host, ports)

if __name__ == '__main__':
     main()
   ```
