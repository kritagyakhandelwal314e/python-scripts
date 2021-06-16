import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError('Error fetching: ' + str(res.status_code) + ' , check the api and try again')
    return res

def get_passwords_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_passwords_leaks_count(response.text, tail)


def main(args):
    for arg in args:
        count = pwned_api_check(arg)
        if count:
            print(f"{arg} was found {count} times... you should change it")
        else:
            print(f'{arg} is good buddy')
    return 'done'

if __name__ == "__main__":
    print(main(sys.argv[1:]))