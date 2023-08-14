#https://www.imooc.com/
#crawling all courses information on the website
#including tags：name link price
#save as csv orexcel
import requests 
from bs4 import BeautifulSoup  
import os
import time
from urllib.request import urlretrieve
import csv
from lxml import etree

def store(data):
    headers = ['course', 'link', 'price']
    if not os.path.exists(r'course data'):
        os.mkdir(r'course data')
    with open('data.csv', 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    re = requests.get('https://www.imooc.com/', headers=headers).text
    content = BeautifulSoup(re, "html.parser")
    data = content.find_all('div', attrs={'class':'list clearfix show'})
    csv_list = []
    c = data[0].find_all('a')
    # print(c[0])

    #use beautifulsoup's find to locate
    #another way is to use beautifulsoup's select to locate
    link = 'https:' + c[0]['href'].strip()
    deep_re = requests.get(link, headers=headers).text
    deep_content = BeautifulSoup(deep_re, "html.parser")
    n = deep_content.find('div', attrs={'class':'name'}).text
    # print(n)

    #use xpath to locate
    dom = etree.HTML(deep_re)
    name = dom.xpath('//*[@id="teacherInfo"]/div/div[2]/div[1]/div/div[1]')[0].text
    print(name)
        


    # print(c[0])
    # print(c[0].find('span', attrs={'class':"price l red bold"}).text)

    # print(c[0].find('p', attrs={'class':'title ellipsis2'}).text)

    # for part in data:
    #     course_list = []
    #     for course in part.find_all('a'):
    #         name = course.find('p', attrs={'class':'title ellipsis2'}).text
    #         # print(name)
    #         if course['href'].strip():
    #             cover_link = 'https:' + course['href'].strip()
    #             deep_re = requests.get(cover_link, headers=headers).text
    #             deep_content = BeautifulSoup(deep_re, "html.parser")
                
    #         else:
    #             cover_link = 'unknown'
    #         # print(cover_link)
    #         # print(course)
    #         if course.find('span', attrs={'class':"price l red bold"}):
    #             price = course.find('span', attrs={'class':"price l red bold"}).text
    #         else:
    #             price = 'unknown'
    #         course_list.append(tuple([name, cover_link, price]))
    #     csv_list.append(course_list)
    # data_list = []
    # for item in csv_list:
    #     data_list.extend(item)
    
    # store(data_list)
            

