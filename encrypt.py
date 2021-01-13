import requests, hashlib
from bs4 import BeautifulSoup

URL = "http://142.93.34.50:32402/"

session = requests.Session()

def hash_md5(hash_value):
    return hashlib.md5(hash_value.encode()).hexdigest()

response = session.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

md5 = hash_md5(soup.h3.string)

flag = session.post(URL, data={'hash':md5})

soup_flag = BeautifulSoup(flag.text, 'html.parser')
print("Flag: {}".format(soup_flag.p.string))