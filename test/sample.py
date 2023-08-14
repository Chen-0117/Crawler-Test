import requests 
from bs4 import BeautifulSoup  
import os
import time
from urllib.request import urlretrieve

def fire(headers):
    page = 0
    for i in range(0, 450, 30):
        print("start crawling page %s" %page)
        url = 'https://movie.douban.com/celebrity/1011562/photos/?type=C&start={}&sortby=like&size=a&subtype=a'.format(i)
        res = requests.get(url, headers=headers).text
        data = get_poster_url(res)
        download1(data)
        page += 1

def get_poster_url(res):
    content = BeautifulSoup(res, "html.parser")
    data = content.find_all('div', attrs={'class': 'cover'})
    picture_list  = []
    for d in data:
        plist = d.find('img')['src']
        picture_list.append(plist)
    return picture_list

def download(pic_l):
    if not os.path.exists(r'picture'):
        os.mkdir(r'picture')
    for i in pic_l:
        pic = requests.get(i)
        p_name = i.split('/')[7]
        with open('picture\\' + p_name, 'wb') as f:
            f.write(pic.content)

def download1(pic_l):
    """
    a more convenient urlretrieve
    """
    if not os.path.exists(r'picture1'):
        os.mkdir(r'picture1')
    for i in pic_l:
        p_name = i.split('/')[7]
        if os.path.exists('picture1/'+p_name):
            print("filename exists")
            pass
        urlretrieve(i, filename='picture1/'+p_name)

if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    # url = 'https://movie.douban.com/celebrity/1011562/photos/'
    # res = requests.get(url,headers=headers).text
    fire(headers)
