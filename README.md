# Porchecker

**Information about ports**

## Requirements: 
python3

Linux- Debian(Recommended)

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
