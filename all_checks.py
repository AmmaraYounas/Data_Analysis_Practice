Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python3
... import os
... import sys
SyntaxError: multiple statements found while compiling a single statement
>>> #!/usr/bin/env python3
>>> import os
... 
>>> import sys
>>> KeyboardInterrupt
>>> def check_reboot():
...     """Returns True if the computer has a pending reboot"""
...     return os.path.exists("/run/reboot-required")
... 
>>> def main():
...     if check_reboot():
...         print("pending reboot.")
...         sys.exit(1)
...     print("Everything is ok.")
...     sys.exit(0)
... 
...     
