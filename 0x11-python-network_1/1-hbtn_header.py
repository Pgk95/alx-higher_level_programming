#!/usr/bin/python3

"""dipslays the a value found in the header of the response"""

import urllib.request
import sys


def main():
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
if __name__ == "__main__":
    
    
    main()
