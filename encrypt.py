import requests, hashlib
from bs4 import BeautifulSoup

URL = "http://site.exemplo:p0rt4/" #URL do desafio

session = requests.Session()

def hash_md5(hash_value):
    return hashlib.md5(hash_value.encode()).hexdigest()

response = session.get(URL) #faz a requisição

soup = BeautifulSoup(response.text, 'html.parser')  # pega o code html

md5 = hash_md5(soup.h3.string)  # pega a info onde está a string requerida

flag = session.post(URL, data={'hash':md5}) # faz o post do problema

soup_flag = BeautifulSoup(flag.text, 'html.parser')
print("Flag: {}".format(soup_flag.p.string))    #imprime a flag encontrada
