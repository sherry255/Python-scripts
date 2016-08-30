from  urllib.request import urlopen
from bs4 import BeautifulSoup
import request
import datetime
import random
import re

# random.seed(datetime.datetime.now())
# companyUrl
def get_company_links(page_links):
    """得到要爬的网页中每一页的公司链接"""
    a = []
    for l in page_links:
        html = urlopen(l)
        bsOjc = BeautifulSoup(html, 'html.parser')
        for link in bsOjc.findAll(class_="position_link"):
            a.append(link.attrs['href'][2:])
            print (link.attrs['href'][2:])
    print (len(set(a)))
            # yield link


def _get_page_links():
    """得到要爬的网页"""
    for i in range(1,14):
        link = 'http://www.lagou.com/zhaopin/Python/'+ str(i) +'/'
        yield link


if __name__ == '__main__':
    get_company_links(_get_page_links())




