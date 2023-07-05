#!/usr/bin/python3

"""dipslays the a value found in the header of the response"""

import urllib.request
import sys

<<<<<<< HEAD
def main():
    url = sys.argv[1]
=======
>>>>>>> c665bc17f91f5542471a5c96622ad2d265da4964

def main():
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
if __name__ == "__main__":
<<<<<<< HEAD
=======
    
    
>>>>>>> c665bc17f91f5542471a5c96622ad2d265da4964
    main()
